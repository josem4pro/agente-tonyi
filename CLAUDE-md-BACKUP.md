# CLAUDE.md — agente-tonyi

## Que es esto

Motor de decision agentica basado en Tongyi-DeepResearch-30B-A3B. No es un generador de informes.
Le das una pregunta concreta, investiga la web con busqueda + visita de paginas + Google Scholar,
y devuelve una respuesta directa, accionable y respaldada por evidencia.

Nacio del laboratorio Tonyi-DeepResearch-Trinidad despues de 18+ sesiones y 8 tests iterativos.

---

## Arquitectura

```
Pregunta → react_agent.py → (search/visit/scholar) x N rounds → <answer> conciso
                ↑                        ↑
          prompt.py (AGENT_SYSTEM_PROMPT)  tool_*.py (SearXNG + Selenium)
```

Pipeline:
1. `run_multi_react.py` lee dataset JSONL, lanza workers
2. `gpu_preflight.py` valida GPU, mata parasitos VRAM, chequea servicios
3. `react_agent.py` ejecuta loop ReAct: think → tool_call → observation → repeat
4. Herramientas: `search` (SearXNG), `visit` (Selenium+LLM extractor), `google_scholar`, `parse_file`
5. Terminacion: `<answer>` tags, budget agotado, timeout, o context limit

---

## Las 30 variables (.env) — 7 capas

### Capa 1: Modo de operacion
| Variable | Default | Funcion |
|----------|---------|---------|
| `AGENT_MODE` | `true` | `true`=respuesta concisa, `false`=reporte exhaustivo |

### Capa 2: Modelo e inferencia
| Variable | Default | Funcion |
|----------|---------|---------|
| `LLM_LOCAL_PATH` | (requerido) | Path al modelo HF o GGUF |
| `MAX_MODEL_LEN` | `65536` | Ventana de contexto del servidor |
| `MAX_CONTEXT_TOKENS` | `45000` | Limite de tokens por run |
| `KV_CACHE_DTYPE` | `fp8` | Tipo de KV cache (fp8/auto) |
| `GPU_MEM_UTIL` | `0.92` | Fraccion de VRAM para vLLM |
| `SUMMARY_MODEL_NAME` | (requerido) | Nombre del modelo en /v1/models |

### Capa 3: Servidor
| Variable | Default | Funcion |
|----------|---------|---------|
| `VLLM_PORT` | `6001` | Puerto del servidor de inferencia |
| `VLLM_PORTS` | `6001` | Puertos separados por coma (multi-GPU) |
| `API_KEY` | `dummy` | API key (dummy para local) |
| `API_BASE` | `http://127.0.0.1:6001/v1` | Base URL del servidor |

### Capa 4: Generacion
| Variable | Default | Funcion |
|----------|---------|---------|
| `TEMPERATURE` | `0.85` | Temperatura de sampling |
| `PRESENCE_PENALTY` | `1.1` | Penalidad de repeticion |
| `MAX_GENERATION_TOKENS` | `1500` | Tokens max por generacion (agente) |

### Capa 5: Budget y control
| Variable | Default | Funcion |
|----------|---------|---------|
| `MAX_LLM_CALL_PER_RUN` | `50` | Max rounds de tool calls |
| `RUN_TIMEOUT_MINUTES` | `9999` | Hard timeout global |
| `EARLY_STOP_MINUTES` | `0` | 0=desactivado, N=forzar respuesta a N min del final |
| `MAX_WORKERS` | `1` | Workers paralelos |
| `ROLLOUT_COUNT` | `1` | Rollouts por pregunta |

### Capa 6: Herramientas
| Variable | Default | Funcion |
|----------|---------|---------|
| `SEARXNG_URL` | `http://127.0.0.1:8080` | URL de SearXNG |
| `USE_SEARXNG` | `true` | Usar SearXNG vs Serper |
| `SELENIUM_BROWSER` | `chrome` | Browser para visita de paginas |
| `SELENIUM_HEADLESS` | `true` | Headless mode |
| `SELENIUM_TIMEOUT` | `30` | Timeout de carga de pagina |
| `VISIT_SERVER_TIMEOUT` | `200` | Timeout del servidor de extraccion |
| `WEBCONTENT_MAXLENGTH` | `150000` | Max chars de contenido web |
| `VISIT_MAX_TOKENS` | `4000` | Max tokens para extraccion |

### Capa 7: Sistema
| Variable | Default | Funcion |
|----------|---------|---------|
| `OPENAI_CLIENT_TIMEOUT` | `7200` | Timeout global del cliente OpenAI |
| `CUDA_HOME` | `/usr/local/cuda-12.8` | Path a CUDA toolkit |
| `USE_IDP` | `False` | Alibaba IDP parser (requiere credenciales) |

---

## Las 5 variables criticas

Estas son las que determinan si funciona o no:

1. **`SUMMARY_MODEL_NAME`** — Debe coincidir exactamente con lo que devuelve `/v1/models`
2. **`AGENT_MODE`** — `true` para agente, `false` para reportes
3. **`MAX_GENERATION_TOKENS`** — 1500 para agente, 16384 para reportes
4. **`MAX_LLM_CALL_PER_RUN`** — Cuantos rounds de investigacion
5. **`API_BASE`** — URL del servidor de inferencia

---

## Como lanzar un test

### Prerequisitos
- Servidor de inferencia corriendo en puerto 6001 (vLLM o llama-server)
- SearXNG corriendo en puerto 8080
- Chrome instalado (para Selenium)

### Verificar servicios
```bash
curl -s http://127.0.0.1:6001/health
curl -s http://127.0.0.1:6001/v1/models | python3 -m json.tool
curl -s http://127.0.0.1:8080/healthz
```

### Lanzar test agentico
```bash
cd /home/ubuntu/Repositorios/agente-tonyi/inference
set -a && source ../.env && set +a

PYTHONUNBUFFERED=1 ../venv/bin/python3 run_multi_react.py \
  --dataset eval_data/test_agent_001.jsonl \
  --output ../output \
  --max_workers 1 \
  --roll_out_count 1 \
  --temperature 0.85 \
  --presence_penalty 1.1
```

### Antes de lanzar
```bash
# Matar procesos zombie
pkill -f run_multi_react 2>/dev/null
sleep 2
```

---

## Reglas operativas

### NO hacer
- NO relanzar el servidor de inferencia sin necesidad (tarda en cargar modelo)
- NO lanzar multiples instancias de run_multi_react.py
- NO interrumpir una generacion en progreso (puede tardar minutos)
- NO cambiar parametros del servidor mientras hay un test corriendo

### SI hacer
- Verificar `/v1/models` antes de cada test
- Monitorear con `tail -f /tmp/llama-server.log` o logs de vLLM
- Esperar al menos 10 minutos antes de declarar que un test se colgo

---

## Rendimiento esperado (RTX 3090)

| Backend | Prefill 12K tok | Decode | GPU util |
|---------|----------------|--------|----------|
| vLLM AWQ | ~2s | ~150 tok/s | 90%+ |
| llama.cpp GGUF | ~90s | 8-13 tok/s | 1-5% (MoE en CPU) |

---

## Notas de voz del operador

Cuando el usuario escriba **"nota"**, significa que grabo una nota de voz.
Protocolo:
1. Leer el archivo `.txt` mas reciente de la carpeta de notas
2. Interpretar la transcripcion como instrucciones
3. Confirmar antes de actuar
