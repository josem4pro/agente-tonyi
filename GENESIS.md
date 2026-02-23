# GENESIS — Del laboratorio al producto

## La historia

agente-tonyi nace de Tonyi-DeepResearch-Trinidad, un repositorio-laboratorio donde durante 18+ sesiones
y 8 tests iterativos se descubrio algo que cambio la premisa del proyecto: **DeepResearch no es un
generador de informes. Es un motor de decision agentica.**

El repo original (github.com/josem4pro/Tonyi-DeepResearch-Trinidad) contiene toda la historia de
exploracion: 32 reportes de sesion, 7 investigaciones de 5 motores AI, scripts de diagnostico,
pruebas fallidas, y la evolucion completa del prompt system.

Este repo es el producto destilado: solo el codigo que funciona, configurado para modo agente.

---

## La tabla comparativa: 8 tests + AGENTE-001

| Test | Backend | Rounds | Tiempo | Tokens output | Resultado |
|------|---------|--------|--------|---------------|-----------|
| TEST-001 | llama.cpp GGUF 131K | 11 | 3h20m | 8,879 chars | Early-stop, reporte largo |
| TEST-002 | llama.cpp GGUF 131K | 4 | ~1h | ~2,000 chars | Timeout parcial |
| TEST-003 | vLLM AWQ 65K | 7 | 2m37s | Natural | 76x mas rapido que llama-server |
| TEST-004 | vLLM AWQ 65K | 25 | 10m | 16K chars | Prompt reescrito, reporte |
| TEST-005 | vLLM AWQ 65K | 30 | 11m18s | Grande | Bottleneck fue round-limit |
| TEST-006 | vLLM AWQ 65K | 30 | ~12m | Grande | Ajuste de parametros |
| TEST-007 | vLLM AWQ 65K | 30 | ~15m | Grande | Refinamiento prompt |
| TEST-008 | vLLM AWQ 65K | 30 | ~14m | Grande | Pre-AGENTE |
| **AGENTE-001** | **vLLM AWQ 65K** | **50** | **18m** | **Conciso** | **Ace a la primera** |

AGENTE-001 fue el punto de inflexion: 50 rounds de investigacion, respuesta directa y accionable,
sin el bloat de un reporte de 16K caracteres.

---

## La metafora de la sabana

> "Es como cuando extiendes una sabana grande sobre una cama. Si tiras de una esquina,
> la otra se levanta. Los tokens de generacion y los de contexto son las dos esquinas.
> No puedes tener ambos al maximo."

Esta metafora del operador capturo la tension fundamental del sistema:
- MAX_GENERATION_TOKENS alto (16384) = reportes largos pero menos rounds de investigacion
- MAX_GENERATION_TOKENS bajo (1500) = respuestas concisas pero mas rounds disponibles

La solucion: modo agente con generacion corta y muchos rounds. La calidad de la investigacion
viene de la profundidad de la busqueda, no de la longitud de la respuesta.

---

## Lo que se descubrio

1. **El modelo piensa mejor en rounds cortos**: Con generacion limitada a 1500 tokens, el modelo
   produce tool calls mas precisas y no desperdicia tokens en thinking innecesario.

2. **50 rounds > 15 rounds con reporte largo**: Mas busquedas = mejor informacion = mejor respuesta,
   aunque la respuesta final sea mas corta.

3. **AGENT_SYSTEM_PROMPT vs SYSTEM_PROMPT**: El prompt agentico elimina las instrucciones de
   "escribir reporte exhaustivo" y las reemplaza por "resolver un problema concreto".

4. **Early-stop es innecesario en modo agente**: El modelo aprende a cerrar cuando tiene suficiente
   informacion. EARLY_STOP_MINUTES=0 funciona bien.

5. **El preflight check es critico**: gpu_preflight.py mata parasitos de VRAM (RustDesk, Ollama),
   valida servicios, y previene lanzamientos fallidos.

---

## Conclusion

DeepResearch ya no es un generador de informes. Es un motor de decision agentica que investiga
la web y produce respuestas concretas. La diferencia no es solo de prompt: es de arquitectura
de tokens, budget de rounds, y filosofia de respuesta.

El laboratorio queda abierto para experimentacion. El producto vive aqui.

---

## Referencia

- Repo laboratorio: Tonyi-DeepResearch-Trinidad
- Modelo: Tongyi-DeepResearch-30B-A3B (Mixture of Experts, 3B activos de 30B)
- Hardware de desarrollo: RTX 3090 24GB, Intel i5-14400F, 64GB DDR5
