# CLAUDE.md — agente-tonyi

> Motor de decision agentica basado en Tongyi-DeepResearch-30B-A3B.
> ReAct loop + web search + LLM local. Destilado de 18+ sesiones de laboratorio.

---

## I. Radiografia (Estructura Fisica)

### Inventario de Archivos

```
agente-tonyi/                          # 4,643 LOC total (sin venv)
├── README.md                          # 72 LOC — Quick start
├── GENESIS.md                         # 84 LOC — Historia del proyecto
├── requirements.txt                   # 191 deps (30 criticas, 161 transitivas)
├── .env.example                       # 49 LOC — Template de configuracion
├── .gitignore                         # 13 LOC
│
└── inference/                         # 3,547 LOC — Todo el codigo
    ├── run_multi_react.py             # 242 LOC — ENTRY POINT principal
    ├── react_agent.py                 # 298 LOC — CORE: MultiTurnReactAgent
    ├── prompt.py                      # 158 LOC — System prompts (2 modos)
    ├── gpu_preflight.py               # 303 LOC — Validacion GPU + preflight
    ├── tool_search.py                 # 141 LOC — Web search (SearXNG)
    ├── tool_visit.py                  # 226 LOC — Page reader (Selenium+LLM)
    ├── tool_scholar.py                # 120 LOC — Academic search
    ├── tool_file.py                   # 141 LOC — File parser wrapper
    ├── searxng_adapter.py             # 137 LOC — SearXNG API adapter
    ├── selenium_adapter.py            # 180 LOC — Headless browser adapter
    ├── run_single_gpu.sh              #  49 LOC — vLLM launcher
    ├── run_llamacpp.sh                #  82 LOC — llama.cpp launcher
    ├── eval_data/
    │   └── test_agent_001.jsonl       # Dataset de prueba
    └── file_tools/                    # 1,849 LOC — Parsers de archivos
        ├── __init__.py                # vacio
        ├── file_parser.py             # 578 LOC — Multi-format parser
        ├── video_analysis.py          # 618 LOC — Video/audio analysis
        ├── video_agent.py             #  92 LOC — Video agent wrapper
        ├── idp.py                     #  89 LOC — Aliyun IDP client
        └── utils.py                   # 542 LOC — Utilidades compartidas
```

> Verify: `find inference -name '*.py' -o -name '*.sh' | wc -l` → 19 archivos

### Dependencias Criticas (30 de 191)

| Categoria | Libreria | Version | Rol |
|-----------|----------|---------|-----|
| LLM Inference | `vllm` | 0.10.1 | Servidor de inferencia principal |
| | `torch` | 2.7.1 | Motor de computo GPU |
| | `transformers` | 4.56.1 | Carga de modelos HuggingFace |
| | `openai` | 1.99.5 | Cliente API compatible con vLLM |
| | `qwen-agent` | 0.0.26 | Framework base de herramientas |
| | `tiktoken` | 0.11.0 | Conteo de tokens |
| Web Search | `selenium` | 4.26.1 | Automatizacion headless Chrome |
| | `requests` | 2.32.5 | HTTP client (SearXNG) |
| | `markdownify` | 0.14.1 | HTML a Markdown |
| File Parsing | `pdfminer.six` | 20250506 | Extraccion texto PDF |
| | `pdfplumber` | 0.11.7 | Extraccion datos PDF |
| | `python-pptx` | 1.0.2 | Parser PPTX |
| | `openpyxl` | 3.1.5 | Parser XLSX |
| | `opencv-python-headless` | 4.12.0.88 | Extraccion frames video |
| Data | `pydantic` | 2.11.9 | Validacion de datos |
| | `json5` | 0.12.1 | JSON lenient parsing |
| | `pandas` | 2.3.2 | DataFrames |
| Config | `python-dotenv` | 1.1.1 | Carga .env |

### Entry Points

1. **`inference/run_multi_react.py`** — Punto de entrada principal (CLI argparse)
2. **`inference/run_single_gpu.sh`** — Lanza vLLM server (modelo AWQ, 65K ctx)
3. **`inference/run_llamacpp.sh`** — Lanza llama.cpp server (modelo GGUF, 131K ctx)
4. **`inference/gpu_preflight.py`** — Validacion GPU standalone (`--dry-run`)

### Configuracion (.env)

| Variable | Default | Descripcion |
|----------|---------|-------------|
| `AGENT_MODE` | `true` | `true`=conciso, `false`=reporte largo |
| `LLM_LOCAL_PATH` | — | Ruta al modelo (HF o GGUF) |
| `MAX_MODEL_LEN` | `65536` | Ventana de contexto |
| `MAX_CONTEXT_TOKENS` | `45000` | Budget de tokens por run |
| `GPU_MEM_UTIL` | `0.92` | Fraccion VRAM para vLLM |
| `VLLM_PORT` | `6001` | Puerto del servidor |
| `TEMPERATURE` | `0.85` | Diversidad de sampling |
| `PRESENCE_PENALTY` | `1.1` | Supresion de repeticion |
| `MAX_WORKERS` | `1` | Workers paralelos |
| `SEARXNG_URL` | `http://127.0.0.1:8080` | URL de SearXNG |
| `MAX_LLM_CALL_PER_RUN` | `50` | Rounds maximo por pregunta |
| `MAX_GENERATION_TOKENS` | `1500` | Tokens por respuesta (1500 agente, 16384 reporte) |

> Verify: `cat .env.example | grep -c '='` → ~25 variables

---

## II. Tomografia (Analisis Semantico)

### Grafo de Simbolos

```
MultiTurnReactAgent (FnCallAgent)          ← inference/react_agent.py:49-297
├── __init__(function_list, llm)           ← Carga tokenizer, config LLM
├── _run(data, model)                      ← CORE LOOP: ReAct (146 LOC)
├── call_server(msgs, planning_port)       ← POST a vLLM /v1/chat/completions
├── count_tokens(messages)                 ← tiktoken token counting
├── sanity_check_output(content)           ← Validacion de output
└── custom_call_tool(tool_name, tool_args) ← Dispatch a TOOL_MAP

Search (BaseTool) @register_tool("search") ← inference/tool_search.py
├── call(params)                           ← Entry point
├── google_search_with_serp(query)         ← Usa SearXNG o Serper
├── search_with_serp(query)                ← Fallback Serper API
└── _format_results(results, query)        ← Markdown formatting

Visit (BaseTool) @register_tool("visit")   ← inference/tool_visit.py
├── call(params)                           ← Entry: acepta url[] + goal
├── fetch_and_extract(url, goal)           ← Orquesta fetch + extract
├── _fetch_page(url)                       ← Llama selenium_readpage()
├── _is_meaningful_content(content)        ← Valida contenido no-vacio
├── _extract_with_llm(content, url, goal)  ← LLM extrae info relevante
└── call_server(msgs, max_retries)         ← POST a vLLM para extraccion

Scholar (BaseTool) @register_tool("google_scholar") ← inference/tool_scholar.py
├── call(params)                           ← Entry point
├── google_scholar_with_serp(query)        ← SearXNG academic search
└── _format_scholar_results(results)       ← Formato academico

FileParser (BaseTool) name="parse_file"    ← inference/tool_file.py
└── call(params, file_root_path)           ← Async wrapper a SingleFileParser

SingleFileParser (BaseTool)                ← inference/file_tools/file_parser.py
├── call(params)                           ← Parsea PDF/DOCX/PPTX/XLSX/HTML/XML/ZIP
├── _prepare_file(path)                    ← Descarga o localiza archivo
├── _process_new_file(file_path)           ← Dispatch por extension
└── _cache_result(file_path, result)       ← Cache de resultados

VideoAnalysis (BaseTool) @register_tool("video_analysis") ← inference/file_tools/video_analysis.py
├── call(params)                           ← Entry: video/audio analysis
├── _extract_keyframes()                   ← OpenCV frame extraction
├── _transcribe_audio()                    ← Audio transcription
└── _analyze_media()                       ← LLM analysis de frames
```

### Grafo de Dependencias (Referencias Cruzadas)

```
run_multi_react.py
    ├──imports──→ MultiTurnReactAgent (react_agent.py:9)
    ├──imports──→ run_preflight, post_flight, PreflightError (gpu_preflight.py:10)
    └──instancia─→ test_agent = MultiTurnReactAgent(llm=llm_cfg) (line 180)

react_agent.py
    ├──imports──→ Search (tool_search.py)
    ├──imports──→ Visit (tool_visit.py)
    ├──imports──→ Scholar (tool_scholar.py)
    ├──imports──→ FileParser (tool_file.py)
    ├──imports──→ SYSTEM_PROMPT, AGENT_SYSTEM_PROMPT (prompt.py)
    └──TOOL_MAP──→ {tool.name: tool for tool in [FileParser, Scholar, Visit, Search]}

tool_search.py
    └──imports──→ searxng_search, SEARXNG_URL (searxng_adapter.py:12)

tool_visit.py
    ├──imports──→ selenium_readpage, cleanup_driver (selenium_adapter.py:11)
    └──imports──→ EXTRACTOR_PROMPT (prompt.py:10)

tool_scholar.py
    └──imports──→ searxng_scholar (searxng_adapter.py)
```

### Herencia y Framework

```
qwen_agent.FnCallAgent
    └── MultiTurnReactAgent          ← Overrides: _run(), custom_call_tool()

qwen_agent.BaseTool
    ├── Search                       ← @register_tool("search")
    ├── Visit                        ← @register_tool("visit")
    ├── Scholar                      ← @register_tool("google_scholar")
    ├── FileParser                   ← name="parse_file" (manual, no decorator)
    ├── SingleFileParser             ← @register_tool("file_parser") [comentado]
    ├── VideoAnalysis                ← @register_tool("video_analysis")
    └── VideoAgent                   ← @register_tool("VideoAgent")
```

### Patrones de Diseno Detectados

| Patron | Ubicacion | Descripcion |
|--------|-----------|-------------|
| **ReAct Loop** | `react_agent.py:_run()` | Think → tool_call → observation × N → answer |
| **Tool Registry** | `react_agent.py:35-41` | Dict comprehension: `{tool.name: tool}` |
| **Adapter Pattern** | `searxng_adapter.py`, `selenium_adapter.py` | Abstraccion sobre servicios externos |
| **Strategy Pattern** | `prompt.py` | AGENT_MODE vs REPORT_MODE cambia prompt + budget |
| **Singleton** | `selenium_adapter.py:54-55` | Driver unico thread-safe con `_driver_lock` |
| **Budget Guard** | `react_agent.py:160-268` | Triple guard: tokens + time + calls |
| **Sticky Routing** | `run_multi_react.py:138-142` | Pregunta siempre al mismo vLLM port |

### Deuda Tecnica

| Tipo | Ubicacion | Detalle |
|------|-----------|--------|
| TODO | `file_tools/utils.py:346` | `# TODO: considering audio` en extract_files |
| TODO | `file_tools/file_parser.py:176` | `# Todo: header and footer` en parse_pdf |
| TODO | `file_tools/file_parser.py:206` | `# Todo: Further analysis using font` |
| Bare except | `react_agent.py:136` | `except:` sin tipo (line 136) |
| Bare except | `react_agent.py:213` | `except:` en JSON parse de tool_call |
| Disabled tool | `react_agent.py:31-33` | PythonInterpreter comentado (SandboxFusion) |
| Disabled decorator | `tool_file.py:98` | `@register_tool` comentado |
| Disabled decorator | `file_parser.py:463` | `@register_tool` comentado |

> Verify: `grep -rn 'TODO\|FIXME\|HACK' inference/ --include='*.py'` → 3 TODOs

---

## III. Resonancia Molecular (Tree-Sitter + PageRank)

### Mapa de Simbolos por Archivo (tree-sitter)

**Archivos con alta densidad simbolica** (PageRank relevance):

| Archivo | Clases | Funciones | Metodos | Constantes | Densidad |
|---------|--------|-----------|---------|------------|----------|
| `react_agent.py` | 1 | 1 | 6 | 4 | CRITICA |
| `file_parser.py` | 3 | 22 | 7 | 5 | ALTA |
| `utils.py` | 1 | 32 | 1 | 1 | ALTA |
| `video_analysis.py` | 2 | 1 | 24 | 6 | ALTA |
| `gpu_preflight.py` | 1 | 9 | 0 | 5 | MEDIA |
| `tool_visit.py` | 1 | 1 | 6 | 3 | MEDIA |
| `tool_search.py` | 1 | 0 | 5 | 2 | MEDIA |
| `selenium_adapter.py` | 0 | 6 | 0 | 5 | MEDIA |
| `searxng_adapter.py` | 0 | 4 | 0 | 1 | BAJA |
| `tool_scholar.py` | 1 | 0 | 3 | 2 | BAJA |
| `tool_file.py` | 1 | 1 | 1 | 1 | BAJA |
| `prompt.py` | 0 | 0 | 0 | 3 | CONFIG |

### Archivos Centrales (por PageRank)

1. **`react_agent.py`** — Hub central. Importa todos los tools, define el loop.
2. **`run_multi_react.py`** — Entry point. Instancia el agente, orquesta ejecucion.
3. **`prompt.py`** — Prompts del sistema. Referenciado por react_agent y tool_visit.
4. **`file_tools/utils.py`** — Utilidades compartidas por file_tools/*.
5. **`file_tools/file_parser.py`** — Parser multi-formato mas complejo del repo.

### Clusters de Dependencia

```
CLUSTER 1: Agent Core
  react_agent.py ←→ run_multi_react.py ←→ gpu_preflight.py ←→ prompt.py

CLUSTER 2: Web Tools
  tool_search.py ←→ searxng_adapter.py
  tool_visit.py ←→ selenium_adapter.py ←→ prompt.py (EXTRACTOR_PROMPT)
  tool_scholar.py ←→ searxng_adapter.py

CLUSTER 3: File Tools
  tool_file.py → file_parser.py → idp.py
  video_agent.py → video_analysis.py
  utils.py (shared)
```

### Huerfanos (archivos sin importadores directos)

- `inference/run_single_gpu.sh` — Ejecutado manualmente (shell)
- `inference/run_llamacpp.sh` — Ejecutado manualmente (shell)
- `inference/file_tools/video_agent.py` — Registrado via `@register_tool` pero no importado directamente
- `inference/file_tools/video_analysis.py` — Registrado via `@register_tool` pero no importado directamente

> Verify: `grep -rn 'import' inference/*.py | grep -c 'from\|import'` → confirma grafo

---

## IV. Vision Holografica (Sintesis)

### Arquitectura del Sistema

```
                         ┌─────────────────────┐
                         │   Dataset (JSONL)    │
                         │   question + answer  │
                         └─────────┬───────────┘
                                   │
                         ┌─────────▼───────────┐
                         │  run_multi_react.py  │
                         │  (ThreadPoolExecutor)│
                         │  N workers parallel  │
                         └─────────┬───────────┘
                                   │
                    ┌──────────────▼──────────────┐
                    │  gpu_preflight.py            │
                    │  - Mata parasitos VRAM       │
                    │  - Valida vLLM + SearXNG     │
                    │  - Estima contexto maximo    │
                    └──────────────┬──────────────┘
                                   │
              ┌────────────────────▼────────────────────┐
              │         MultiTurnReactAgent._run()      │
              │                                         │
              │  WHILE budget > 0:                      │
              │    1. call_server(messages, port)        │──→ vLLM :6001
              │    2. parse <tool_call> or <answer>      │    /v1/chat/completions
              │    3. custom_call_tool(name, args)       │
              │    4. append <tool_response>             │
              │    5. check budget (tokens/time/calls)   │
              │                                         │
              │  TERMINATION:                            │
              │    - <answer> found                      │
              │    - token limit (MAX_CONTEXT_TOKENS)    │
              │    - call budget (MAX_LLM_CALL_PER_RUN)  │
              │    - time limit (RUN_TIMEOUT_MINUTES)    │
              │    - early-stop (EARLY_STOP_MINUTES)     │
              └───┬────────┬────────┬────────┬─────────┘
                  │        │        │        │
          ┌───────▼──┐ ┌───▼────┐ ┌─▼─────┐ ┌▼──────────┐
          │  search   │ │ visit  │ │scholar│ │ parse_file │
          │(SearXNG)  │ │(Selen.)│ │(arXiv)│ │(PDF/DOCX) │
          └───┬──────┘ └───┬────┘ └──┬────┘ └─┬─────────┘
              │            │         │         │
          ┌───▼──────┐ ┌───▼──────┐  │    ┌────▼────────┐
          │ searxng   │ │ selenium │  │    │ file_parser │
          │ _adapter  │ │ _adapter │  │    │ idp.py      │
          └──────────┘ └──────────┘  │    │ video_*.py  │
                                     │    └─────────────┘
                              ┌──────▼──────┐
                              │  searxng    │
                              │  _adapter   │
                              └─────────────┘
```

### Flujo de Datos Completo

```
INPUT:  {"question": "...", "answer": "..."} (JSONL, 1 por linea)
                    │
                    ▼
DEDUP:  Skip preguntas ya procesadas en output existente
                    │
                    ▼
PORT:   Sticky round-robin → misma pregunta siempre al mismo vLLM port
                    │
                    ▼
LOOP:   [system_prompt + question] → LLM → <tool_call> → tool result → LLM → ...
                    │
                    ▼
OUTPUT: {"question", "answer", "prediction", "termination", "messages"} (JSONL)
        → output/{model_name}_sglang/{dataset}/iterN.jsonl
```

### Mecanismo de Budget (Triple Guard)

El sistema tiene tres limites independientes que fuerzan respuesta final:

| Guard | Variable | Default | Accion al alcanzar |
|-------|----------|---------|-------------------|
| **Tokens** | `MAX_CONTEXT_TOKENS` | 45,000 | Fuerza `<answer>` inmediato |
| **Calls** | `MAX_LLM_CALL_PER_RUN` | 50 | Fuerza `<answer>` inmediato |
| **Time** | `RUN_TIMEOUT_MINUTES` | 9999 | Retorna "No answer found" |
| **Early-stop** | `EARLY_STOP_MINUTES` | 0 (off) | Fuerza `<answer>` con investigacion parcial |

### Modos de Operacion

| Aspecto | AGENT_MODE (true) | REPORT_MODE (false) |
|---------|-------------------|---------------------|
| Prompt | `AGENT_SYSTEM_PROMPT` | `SYSTEM_PROMPT` |
| Filosofia | "Resuelve un problema concreto" | "Investigacion exhaustiva" |
| Rounds | 50 (muchas investigaciones cortas) | 30 (menos, mas largas) |
| Generacion | 1,500 tokens (conciso) | 16,384 tokens (reporte largo) |
| Output | "Usa X porque Y" (1-3 parrafos) | Reporte con secciones, tablas, conclusion |
| Tiempo tipico | ~18 min | ~15-20 min |
| Insight clave | Profundidad > longitud | Exhaustividad de exposicion |

### Servicios Requeridos

| Servicio | Puerto | Rol | Arranque |
|----------|--------|-----|----------|
| **vLLM** | 6001 | Inferencia LLM | `bash inference/run_single_gpu.sh` |
| **SearXNG** | 8080 | Web search | `docker start searxng` |
| **Chrome** | — | Headless browser | Auto-detectado por Selenium |

> Alternativa: `bash inference/run_llamacpp.sh` para llama.cpp (131K ctx, mas lento)

### Hardware Target

| Componente | Spec | Notas |
|------------|------|-------|
| GPU | RTX 3090 24GB | 0.92 utilizacion = 22GB para vLLM |
| Modelo | Tongyi-DeepResearch-30B-A3B | MoE: 3B activos de 30B |
| Formato vLLM | AWQ 4-bit | KV cache fp8, 65K contexto |
| Formato llama.cpp | GGUF Q4_K_M | 8 capas MoE a CPU, 131K contexto |
| CPU | Intel i5-14400F | 12 cores para llama.cpp |
| RAM | 64GB DDR5 | — |

### Formato Tool Call/Response

```xml
<!-- LLM genera: -->
<tool_call>
{"name": "search", "arguments": {"query": ["q1", "q2"]}}
</tool_call>

<!-- Sistema inyecta: -->
<tool_response>
1. [Title](URL)
Snippet...
</tool_response>
```

### Quick Start

```bash
# 1. Setup
python3 -m venv venv && ./venv/bin/pip install -r requirements.txt
cp .env.example .env  # Editar: LLM_LOCAL_PATH, SUMMARY_MODEL_NAME

# 2. Lanzar servidor de inferencia
bash inference/run_single_gpu.sh    # vLLM (rapido, AWQ)
# o: bash inference/run_llamacpp.sh  # llama.cpp (lento, GGUF)

# 3. Lanzar SearXNG
docker start searxng

# 4. Ejecutar agente
cd inference && set -a && source ../.env && set +a
PYTHONUNBUFFERED=1 ../venv/bin/python3 run_multi_react.py \
  --dataset eval_data/test_agent_001.jsonl \
  --output ../output \
  --max_workers 1 --roll_out_count 1
```

### Convencion de Codigo

- **Python 3.10+**, sin type hints consistentes
- **snake_case** para funciones/variables, **PascalCase** para clases
- **UPPER_SNAKE_CASE** para constantes
- **Sin linter/formatter** configurado
- **Sin test suite** formal (evaluacion via JSONL datasets)
- **JSONL** para input/output de datos
- **python-dotenv** para toda la configuracion
- **`qwen-agent` BaseTool** como base para herramientas
- **`@register_tool()`** decorator para registro de herramientas

### Comandos Utiles

```bash
# Verificar GPU
nvidia-smi

# Preflight check (dry-run)
cd inference && python gpu_preflight.py --dry-run

# Ver modelos disponibles en vLLM
curl http://127.0.0.1:6001/v1/models

# Health check SearXNG
curl http://127.0.0.1:8080/healthz

# Matar parasitos GPU manualmente
pkill -f ollama; pkill -f rustdesk
```

> Verify: `cat CLAUDE.md | wc -l` → debe ser >200

---

*Generado por init-repomapper-serena-aider (3 microscopios + sintesis Opus 4.6)*
*Fecha: 2026-02-24*
