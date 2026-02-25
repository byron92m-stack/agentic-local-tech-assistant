# Roadmap del Agente Técnico Local

Este documento describe la evolución planificada del proyecto, organizada en fases progresivas y diseñadas para construir un agente conversacional técnico completamente local, modular y extensible.

---

## Visión general del roadmap

El objetivo del proyecto es construir un agente técnico local capaz de:

- Ejecutarse 100% en hardware local  
- Integrarse con herramientas del sistema (FS, shell, logs)  
- Razonar mediante roles internos (Orchestrator + Validator)  
- Exponer una API limpia y extensible  
- Evolucionar hacia un sistema multi-agente  
- Servir como pieza de portfolio profesional  

El roadmap está dividido en fases con dependencias claras.

---

## Fase 1 — Fundamentos (estado: completado)

**Objetivo:** establecer la base del proyecto.

**Incluye:**
- Estructura mínima del repositorio  
- API base con FastAPI  
- System prompt inicial  
- Documentación de arquitectura  
- Roadmap inicial  

**Criterio de completitud (DoD):**
- El proyecto puede ejecutarse localmente  
- La API responde `/health`  
- La documentación inicial está disponible  

---

## Fase 2 — Integración con LLM local

**Objetivo:** conectar el agente con un modelo local.

**Incluye:**
- Integración con Ollama  
- Wrapper interno para llamadas al modelo  
- Manejo de contexto (system + user)  
- Implementación real de Orchestrator y Validator  

**Dependencias:** Fase 1 completada.

**Riesgos:**
- Latencia del modelo  
- Manejo de contexto extenso  

---

## Fase 3 — Herramientas del agente

**Objetivo:** permitir que el agente interactúe con el entorno local de forma segura.

**Incluye:**
- Herramienta de filesystem seguro (lectura controlada)  
- Herramienta de shell seguro (comandos whitelisted)  
- Analizador de logs  
- Inspección de archivos de configuración  

**Criterio de completitud:**
- Cada herramienta tiene validación y sandboxing  

---

## Fase 4 — Interfaz y experiencia

**Objetivo:** mejorar la interacción con el agente.

**Incluye:**
- Endpoint `/chat` con streaming  
- Interfaz web mínima (HTML/JS)  
- Logging estructurado  
- Modo verbose / modo compacto  

**Dependencias:** Fase 2 completada.

---

## Fase 5 — Extensión multi-agente

**Objetivo:** permitir razonamiento distribuido.

**Incluye:**
- Agente analista (razonamiento técnico profundo)  
- Agente ejecutor (acciones controladas)  
- Agente documentador (genera documentación técnica)  
- Orquestador central (LangGraph)  

**Riesgos:**
- Complejidad cognitiva  
- Sincronización entre agentes  

---

## Fase 6 — Integración con proyectos reales

**Objetivo:** aplicar el agente a entornos técnicos reales.

**Incluye:**
- Auditoría de entornos Windows + WSL  
- Análisis de pipelines ETL  
- Integración con ClickHouse (lectura de metadatos)  
- Integración con repos locales  

---

## Fase 7 — Publicación y portfolio

**Objetivo:** presentar el proyecto profesionalmente.

**Incluye:**
- Documentación completa  
- Ejemplos de uso  
- Casos reales  
- Demo grabada  
- Preparación para GitHub público  

---

Este roadmap evolucionará a medida que el proyecto crezca.
