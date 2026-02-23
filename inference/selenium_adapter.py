"""
Selenium Web Page Reader — Jina Reader replacement.

Reads web pages using a headless browser and converts HTML to Markdown.
Module-level functions (no classes), thread-safe driver reuse.
Pattern: same as searxng_adapter.py (functions, not classes).
"""

import os
import time
import shutil
import logging
import threading
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

# Selenium imports
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import (
        TimeoutException,
        WebDriverException,
        InvalidArgumentException,
    )
    from selenium.webdriver.chrome.options import Options as ChromeOptions
    from selenium.webdriver.chrome.service import Service as ChromeService
    from selenium.webdriver.firefox.options import Options as FirefoxOptions
    from selenium.webdriver.firefox.service import Service as FirefoxService
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.firefox import GeckoDriverManager
    SELENIUM_AVAILABLE = True
except ImportError:
    SELENIUM_AVAILABLE = False
    logger.warning("[Selenium] not installed — pip install selenium webdriver-manager")

# HTML to Markdown
try:
    from markdownify import markdownify
    _MARKDOWNIFY = True
except ImportError:
    _MARKDOWNIFY = False
    logger.warning("[Selenium] markdownify not installed — pip install markdownify")

# Config
SELENIUM_BROWSER = os.getenv("SELENIUM_BROWSER", "chrome").lower()
SELENIUM_HEADLESS = os.getenv("SELENIUM_HEADLESS", "true").lower() in ("true", "1", "yes")
SELENIUM_TIMEOUT = int(os.getenv("SELENIUM_TIMEOUT", "30"))

# Driver management (module-level, thread-safe)
_driver = None
_driver_lock = threading.Lock()


def _create_driver():
    """Create a headless browser with en-US locale."""
    if SELENIUM_BROWSER == "firefox":
        opts = FirefoxOptions()
        if SELENIUM_HEADLESS:
            opts.add_argument("--headless")
        opts.set_preference("intl.accept_languages", "en-US, en")
        opts.set_preference("intl.locale.requested", "en-US")
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service, options=opts)
    else:
        opts = ChromeOptions()
        if SELENIUM_HEADLESS:
            opts.add_argument("--headless=new")
        opts.add_argument("--disable-dev-shm-usage")
        opts.add_argument("--disable-gpu")
        opts.add_argument("--no-sandbox")
        opts.add_argument("--window-size=1920,1080")
        opts.add_argument("--lang=en-US")
        opts.add_experimental_option("prefs", {
            "intl.accept_languages": "en-US,en",
        })
        # Find Chrome binary
        for name in ("google-chrome", "chromium-browser", "chromium"):
            path = shutil.which(name)
            if path:
                opts.binary_location = path
                break
        service = ChromeService(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=opts)

    driver.set_page_load_timeout(SELENIUM_TIMEOUT)
    logger.info(f"[Selenium] Created {SELENIUM_BROWSER} driver (headless={SELENIUM_HEADLESS})")
    return driver


def _is_alive(driver):
    """Check if the driver is still responsive."""
    try:
        driver.current_url
        return True
    except Exception:
        return False


def _get_driver():
    """Get or create driver (thread-safe, reuses if alive)."""
    global _driver
    with _driver_lock:
        if _driver is None or not _is_alive(_driver):
            if _driver is not None:
                try:
                    _driver.quit()
                except Exception:
                    pass
            _driver = _create_driver()
        return _driver


def _html_to_markdown(html):
    """Convert HTML to Markdown."""
    if _MARKDOWNIFY:
        return markdownify(html, heading_style="ATX")
    return html


def selenium_readpage(url):
    """
    Read a web page and return its content as Markdown.

    Args:
        url: HTTP/HTTPS URL to read.

    Returns:
        str: Page content in Markdown.

    Raises:
        ImportError: If selenium is not installed.
        InvalidArgumentException: If URL is invalid.
        TimeoutException: If page load times out.
        WebDriverException: For other browser errors.
    """
    if not SELENIUM_AVAILABLE:
        raise ImportError("selenium not installed")

    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        raise ValueError(f"Invalid URL scheme: {url}")

    driver = _get_driver()
    start = time.time()

    driver.get(url)

    try:
        WebDriverWait(driver, min(SELENIUM_TIMEOUT, 10)).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
    except Exception:
        logger.warning(f"[Selenium] Timeout waiting for <body> on {url}")

    # Brief wait for JS rendering
    time.sleep(1.5)

    html = driver.page_source
    content = _html_to_markdown(html)

    elapsed = time.time() - start
    logger.info(f"[Selenium] {url} — {len(content)} chars in {elapsed:.1f}s")
    return content


def cleanup_driver():
    """Clean up the browser. Call at shutdown."""
    global _driver
    with _driver_lock:
        if _driver is not None:
            try:
                _driver.quit()
            except Exception:
                pass
            _driver = None
            logger.info("[Selenium] Driver cleaned up")
