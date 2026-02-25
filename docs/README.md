# Documentación del Proyecto

Este directorio contiene la documentación técnica del **Agente Conversacional Técnico Local**, un sistema diseñado para operar 100% en entorno local (Windows + WSL), utilizando modelos LLM locales, una API propia y un diseño cognitivo modular.

La documentación está organizada para que cualquier desarrollador, empleador o colaborador pueda entender el proyecto sin necesidad de leer el código fuente.

---

## Contenido

### 📌 1. Arquitectura  
`architecture.md`  
Describe la arquitectura física y lógica del agente, incluyendo:

- API local (FastAPI)  
- Backend LLM (Ollama u otro)  
- Módulo de prompts  
- Roles internos (Orchestrator, Validator)  
- Flujo de ejecución  
- Diagrama ASCII  
- Roadmap técnico  

---

### 📌 2. API  
`api.md`  
Documenta los endpoints actuales y planificados:

- `/health`  
- `/chat` (planificado)  
- `/tools/fs` (planificado)  
- `/tools/shell` (planificado)  

Incluye ejemplos de request/response y guía de ejecución local.

---

### 📌 3. Diseño de Prompts  
`../agent/prompts/system_prompt.md`  
Define el comportamiento cognitivo del agente:

- System prompt  
- Reglas de interacción  
- Orchestrator  
- Validator  
- Formato de respuesta  
- Límites y seguridad  

---

### 📌 4. Roadmap  
`roadmap.md`  
Lista de mejoras planificadas:

- Integración con Ollama  
- Herramientas locales (FS, shell seguro, análisis de logs)  
- Agentes secundarios  
- Interfaz web  
- Pruebas automatizadas  
- Streaming de respuestas  

---

### 📌 5. Ejemplos  
`examples.md` (pendiente)  
Mostrará ejemplos reales de interacción con el agente, casos de uso y pruebas manuales.

---

## Objetivo de esta documentación

- Explicar el diseño técnico y cognitivo del agente  
- Facilitar la comprensión del proyecto para empleadores  
- Servir como base para futuras extensiones  
- Mantener claridad y reproducibilidad en el desarrollo  

---

La documentación crecerá a medida que el proyecto evolucione.
