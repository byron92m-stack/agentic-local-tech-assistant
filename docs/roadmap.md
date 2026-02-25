\# Roadmap del Agente Técnico Local



Este documento describe la evolución planificada del proyecto, organizada en fases claras y progresivas.



---



\## Fase 1 — Fundamentos (estado: completado)

\- Estructura mínima del repositorio

\- API base con FastAPI

\- System prompt inicial

\- Documentación de arquitectura

\- Roadmap inicial



---



\## Fase 2 — Integración con LLM local

\- Integrar backend Ollama

\- Crear wrapper interno para llamadas al modelo

\- Añadir manejo de contexto (system + user)

\- Implementar roles Orchestrator y Validator en flujo real



---



\## Fase 3 — Herramientas del agente

\- Añadir herramienta de filesystem seguro (lectura controlada)

\- Añadir herramienta de shell seguro (comandos whitelisted)

\- Añadir herramienta de análisis de logs

\- Añadir herramienta de inspección de archivos de configuración



---



\## Fase 4 — Interfaz y experiencia

\- Endpoint `/chat` con streaming

\- Interfaz web mínima (HTML/JS)

\- Logging estructurado

\- Modo verbose / modo compacto



---



\## Fase 5 — Extensión multi-agente

\- Agente analista (razonamiento técnico profundo)

\- Agente ejecutor (acciones controladas)

\- Agente documentador (genera documentación técnica)

\- Orquestador central (LangGraph)



---



\## Fase 6 — Integración con proyectos reales

\- Auditoría de entornos Windows + WSL

\- Análisis de pipelines ETL

\- Integración con ClickHouse (lectura de metadatos)

\- Integración con repos locales



---



\## Fase 7 — Publicación y portfolio

\- Documentación completa

\- Ejemplos de uso

\- Casos reales

\- Demo grabada



---



Este roadmap evolucionará a medida que el proyecto crezca.

