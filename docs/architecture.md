# Arquitectura del Agente Técnico Local

Este documento describe la arquitectura del **Agente Conversacional Técnico Local**, un sistema modular diseñado para operar 100% en entorno local (Windows + WSL), utilizando modelos LLM locales, prompts estructurados y una API propia.

---

## 1. Visión general

El agente está diseñado para:

- Ejecutarse completamente en hardware local  
- Mantener seguridad y privacidad total  
- Ser modular, extensible y fácil de depurar  
- Integrarse con herramientas locales (filesystem, shell, logs, etc.)  
- Servir como asistente técnico especializado en arquitectura, ML, DevOps y troubleshooting  

La arquitectura combina:

- **API local (FastAPI)**
- **Backend LLM local (Ollama u otro)**
- **Módulo de prompts con roles internos**
- **Documentación técnica y cognitiva**
- **Futuras herramientas locales (FS, shell, análisis)**

---

## 2. Componentes principales

### 2.1. API (FastAPI)
- Expone endpoints locales.
- Permite integrar el agente con herramientas externas.
- Facilita pruebas, automatización y extensibilidad.
- Actúa como capa de seguridad y validación.

### 2.2. Backend LLM (Ollama u otro)
- Ejecuta el modelo local.
- No depende de servicios externos.
- Permite razonamiento seguro y reproducible.
- Aísla la lógica cognitiva del resto del sistema.

### 2.3. Módulo de Prompts
Define el comportamiento del agente mediante:

- **System prompt**
- **Orchestrator** → propone plan
- **Validator** → revisa coherencia
- Reglas de interacción
- Formato de respuesta

### 2.4. Documentación
Incluye:

- Arquitectura
- API
- Roadmap
- Ejemplos
- Diseño cognitivo

Permite que un empleador entienda el proyecto sin leer código.

---

## 3. Flujo de ejecución

1. El usuario envía una consulta a la API.  
2. La API construye el contexto (system prompt + mensaje del usuario).  
3. El backend LLM procesa la solicitud.  
4. El agente aplica:
   - **Orchestrator** → propone plan  
   - **Validator** → revisa coherencia  
5. La respuesta final se devuelve al usuario.

---

## 4. Diagrama de arquitectura general (ASCII)

```
                ┌──────────────────────────┐
                │        Usuario           │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │      API         │
                    │   (FastAPI)      │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Módulo de Prompts      │
                │  - System prompt         │
                │  - Orchestrator          │
                │  - Validator             │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   LLM Local      │
                    │    (Ollama)      │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Herramientas futuras   │
                │  - FS seguro             │
                │  - Shell whitelisted     │
                │  - Análisis de logs      │
                └──────────────────────────┘
```

---

## 5. Diagrama del flujo cognitivo (Orchestrator → Validator)

```
                ┌──────────────────────────┐
                │        Usuario           │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Mensaje User   │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │      Orchestrator        │
                │  - Propone plan          │
                │  - Descompone pasos      │
                │  - Identifica riesgos    │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │        Validator         │
                │  - Revisa coherencia     │
                │  - Ajusta el plan        │
                │  - Garantiza claridad    │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ Respuesta Final  │
                    └──────────────────┘
```

---

## 6. Diagrama del flujo API → LLM

```
                ┌──────────────────────────┐
                │        Usuario           │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   API (FastAPI)  │
                    │  /chat (futuro)  │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Módulo de Prompts      │
                │  - System Prompt         │
                │  - Orchestrator          │
                │  - Validator             │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   LLM Local      │
                    │    (Ollama)      │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │  Respuesta generada por  │
                │         el LLM           │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  API → Usuario   │
                    └──────────────────┘
```

---

## 7. Diagrama de interacción Windows ↔ WSL ↔ Ollama

```
                   ┌──────────────────────────┐
                   │        Windows 11        │
                   │  - PowerShell            │
                   │  - VSCode                │
                   │  - Git                   │
                   └─────────────┬────────────┘
                                 │
                                 │ Llamadas locales
                                 ▼
                   ┌──────────────────────────┐
                   │          WSL2            │
                   │  Ubuntu Linux            │
                   │  - API (FastAPI)         │
                   │  - Código del agente     │
                   │  - Prompts               │
                   └─────────────┬────────────┘
                                 │
                                 │ Llamadas al modelo
                                 ▼
                   ┌──────────────────────────┐
                   │         Ollama           │
                   │  - Modelos LLM locales   │
                   │  - Ejecución aislada     │
                   └─────────────┬────────────┘
                                 │
                                 ▼
                   ┌──────────────────────────┐
                   │   Respuesta generada     │
                   └──────────────────────────┘
```

---

## 8. Principios de diseño

- **Modularidad**  
- **Reproducibilidad**  
- **Seguridad local**  
- **Claridad cognitiva**  
- **Extensibilidad futura**  
- **Aislamiento entre capas**  
- **Compatibilidad Windows + WSL**  

---

## 9. Roadmap

- Integración con Ollama  
- Herramientas locales (filesystem, shell seguro, análisis de logs)  
- Agentes secundarios  
- Interfaz web  
- Pruebas automatizadas  
- Streaming de respuestas  
- Autenticación local  

---

Este documento crecerá a medida que el proyecto evolucione.
