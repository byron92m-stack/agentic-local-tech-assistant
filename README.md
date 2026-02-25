# Agente Conversacional Técnico Local

El **Agente Conversacional Técnico Local** es un asistente especializado en arquitectura, troubleshooting y diseño de sistemas, diseñado para ejecutarse **100% en entorno local** (Windows + WSL) utilizando modelos LLM locales y una API propia.

Este proyecto funciona como una pieza de **infraestructura cognitiva personal**, capaz de razonar sobre entornos técnicos reales sin depender de servicios externos.

---

## 🚀 Objetivos del proyecto

- Proveer un agente técnico capaz de razonar sobre:
  - Arquitectura de sistemas  
  - Pipelines de datos  
  - Entornos híbridos Windows + WSL  
  - Troubleshooting y debugging  
- Mantener todo el flujo en **local**, sin enviar datos a la nube.  
- Servir como base para un sistema **multi-agente** en el futuro.  
- Documentar el diseño cognitivo y técnico de forma clara y profesional.

---

## 🧠 Arquitectura general

El agente está compuesto por:

- **API local (FastAPI)**  
- **Backend LLM local (Ollama u otro)**  
- **Módulo de prompts** con roles internos:
  - Orchestrator  
  - Validator  
- **Documentación técnica** (arquitectura, API, roadmap, ejemplos)

La arquitectura completa se detalla en `docs/architecture.md`.

---

## 📂 Estructura del repositorio

```
agent/
  api/
    main.py
  prompts/
    system_prompt.md

docs/
  README.md
  api.md
  architecture.md
  roadmap.md
  examples.md (pendiente)

README.md
requirements.txt
```

---

## 🛠️ Tecnologías utilizadas

- Python  
- FastAPI  
- Uvicorn  
- LLM local (Ollama u otro backend)  
- WSL2 (Ubuntu)  

---

## ▶️ Ejecución local (modo desarrollo)

1. Instalar dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecutar la API:

```bash
uvicorn agent.api.main:app --reload
```

3. Probar el endpoint de salud:

```
http://127.0.0.1:8000/health
```

---

## 📌 Estado actual

El proyecto se encuentra en la **Fase 1 completada**:

- Estructura base  
- API mínima  
- System prompt inicial  
- Documentación técnica  
- Roadmap definido  

Las próximas fases incluyen:

- Integración con Ollama  
- Herramientas locales (FS, shell seguro, análisis de logs)  
- Interfaz web  
- Sistema multi-agente  

Más detalles en `docs/roadmap.md`.

---

## 📄 Licencia

Proyecto personal — uso libre para revisión técnica y portfolio.

---

Este repositorio evolucionará a medida que el agente crezca.
