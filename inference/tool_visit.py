import json
import os
import time
import logging
from typing import List, Union

import httpx
import tiktoken
from openai import OpenAI
from qwen_agent.tools.base import BaseTool, register_tool
from prompt import EXTRACTOR_PROMPT
from selenium_adapter import selenium_readpage, cleanup_driver

logger = logging.getLogger(__name__)

WEBCONTENT_MAXLENGTH = int(os.getenv("WEBCONTENT_MAXLENGTH", 150000))
VISIT_MAX_TOKENS = int(os.getenv("VISIT_MAX_TOKENS", 6000))


def truncate_to_tokens(text, max_tokens=95000):
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)
    if len(tokens) <= max_tokens:
        return text
    return encoding.decode(tokens[:max_tokens])


ERROR_TEMPLATE = (
    "The useful information in {url} for user goal {goal} as follows: \n\n"
    "Evidence in page: \n"
    "The provided webpage content could not be accessed. "
    "Please check the URL or file format.\n\n"
    "Summary: \n"
    "The webpage content could not be processed, and therefore, "
    "no information is available.\n\n"
)


@register_tool('visit', allow_overwrite=True)
class Visit(BaseTool):
    name = 'visit'
    description = 'Visit webpage(s) and return the summary of the content.'
    parameters = {
        "type": "object",
        "properties": {
            "url": {
                "type": ["string", "array"],
                "items": {"type": "string"},
                "minItems": 1,
                "description": "The URL(s) of the webpage(s) to visit."
            },
            "goal": {
                "type": "string",
                "description": "The goal of the visit for webpage(s)."
            }
        },
        "required": ["url", "goal"]
    }

    def call(self, params, **kwargs):
        try:
            url = params["url"]
            goal = params["goal"]
        except (KeyError, TypeError) as e:
            logger.error(f"[Visit] Invalid params: {e}")
            return "[Visit] Invalid request format: need 'url' and 'goal' fields"

        if isinstance(url, str):
            response = self.fetch_and_extract(url, goal)
        else:
            assert isinstance(url, List)
            parts = []
            start = time.time()
            for u in url:
                if time.time() - start > 900:
                    parts.append(ERROR_TEMPLATE.format(url=u, goal=goal))
                else:
                    try:
                        parts.append(self.fetch_and_extract(u, goal))
                    except Exception as e:
                        parts.append(f"Error fetching {u}: {e}")
            response = "\n=======\n".join(parts)

        logger.info(f"[Visit] Response length: {len(response)}")
        return response.strip()

    def fetch_and_extract(self, url, goal):
        """Fetch page via Selenium, validate, extract with LLM."""
        content = self._fetch_page(url)
        if not self._is_meaningful_content(content):
            return ERROR_TEMPLATE.format(url=url, goal=goal)
        return self._extract_with_llm(content, url, goal)

    def _fetch_page(self, url):
        """Fetch page via Selenium. No fallback — fails loud."""
        try:
            content = selenium_readpage(url)
            logger.info(f"[Visit] Selenium OK: {len(content)} chars from {url}")
            return content
        except Exception as e:
            logger.error(f"[Visit] Selenium FAILED on {url}: {e}")
            return ""

    def _is_meaningful_content(self, content):
        """Check if content is worth sending to LLM."""
        if not content or len(content) < 100:
            logger.info(f"[Visit] Content too short: {len(content) if content else 0} chars")
            return False

        text = content.strip()
        if len(text) < 50:
            return False

        # Error page detection
        preview = text[:500].lower()
        error_patterns = [
            "404", "not found", "page not found",
            "access denied", "403 forbidden",
            "500 internal server error",
            "503 service unavailable",
        ]
        if sum(1 for p in error_patterns if p in preview) >= 2:
            logger.info("[Visit] Content looks like an error page")
            return False

        # Text ratio check (alpha + spaces should be >30%)
        sample = text[:1000]
        visible = sum(1 for c in sample if c.isalnum() or c.isspace())
        ratio = visible / len(sample)
        if ratio < 0.3:
            logger.info(f"[Visit] Low text ratio: {ratio:.0%}")
            return False

        return True

    def _extract_with_llm(self, content, url, goal):
        """Extract evidence + summary from content using LLM."""
        max_retries = int(os.getenv('VISIT_SERVER_MAX_RETRIES', 1))

        content = truncate_to_tokens(content, max_tokens=VISIT_MAX_TOKENS)

        messages = [{"role": "user", "content": EXTRACTOR_PROMPT.format(
            webpage_content=content, goal=goal
        )}]
        raw = self.call_server(messages, max_retries=max_retries)

        # Retry with shorter content if LLM returns nothing useful
        retries_left = 3
        while len(raw) < 10 and retries_left >= 0:
            trunc = int(0.7 * len(content)) if retries_left > 0 else 25000
            logger.info(f"[Visit] LLM retry {4 - retries_left}/4, truncating to {trunc} chars")
            content = content[:trunc]
            messages = [{"role": "user", "content": EXTRACTOR_PROMPT.format(
                webpage_content=content, goal=goal
            )}]
            raw = self.call_server(messages, max_retries=max_retries)
            retries_left -= 1

        # Parse JSON
        if isinstance(raw, str):
            raw = raw.replace("```json", "").replace("```", "").strip()

        parse_attempts = 0
        while parse_attempts < 3:
            try:
                raw = json.loads(raw)
                break
            except (json.JSONDecodeError, TypeError):
                logger.warning(f"[Visit] JSON parse error, attempt {parse_attempts + 1}/3")
                raw = self.call_server(messages, max_retries=max_retries)
                parse_attempts += 1

        if parse_attempts >= 3:
            return ERROR_TEMPLATE.format(url=url, goal=goal)

        return (
            f"The useful information in {url} for user goal {goal} as follows: \n\n"
            f"Evidence in page: \n{raw['evidence']}\n\n"
            f"Summary: \n{raw['summary']}\n\n"
        )

    def call_server(self, msgs, max_retries=2):
        """Call vLLM for content extraction."""
        api_key = os.environ.get("API_KEY")
        api_base = os.environ.get("API_BASE")
        model_name = os.environ.get("SUMMARY_MODEL_NAME", "")
        client = OpenAI(
            api_key=api_key,
            base_url=api_base,
            timeout=httpx.Timeout(connect=30.0, read=None, write=30.0, pool=30.0),
            http_client=httpx.Client(
                timeout=httpx.Timeout(connect=30.0, read=None, write=30.0, pool=30.0),
                transport=httpx.HTTPTransport(
                    socket_options=[(6, 4, 1), (6, 5, 60), (6, 6, 10)]
                )
            )
        )

        for attempt in range(max_retries):
            try:
                stream = client.chat.completions.create(
                    model=model_name,
                    messages=msgs,
                    temperature=0.7,
                    max_tokens=2048,
                    stream=True,
                )
                content = ""
                for chunk in stream:
                    if chunk.choices and chunk.choices[0].delta.content:
                        content += chunk.choices[0].delta.content
                if content:
                    try:
                        json.loads(content)
                    except json.JSONDecodeError:
                        left = content.find('{')
                        right = content.rfind('}')
                        if left != -1 and right != -1 and left <= right:
                            content = content[left:right + 1]
                    return content
            except Exception as e:
                logger.warning(f"[Visit] LLM call failed (attempt {attempt + 1}): {e}")
                if attempt == max_retries - 1:
                    return ""
                continue
        return ""
