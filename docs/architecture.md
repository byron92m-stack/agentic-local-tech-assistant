\# Arquitectura del Agente Técnico Local



Este documento describe la arquitectura del \*\*Agente Conversacional Técnico Local\*\*, un sistema modular diseñado para operar 100% en entorno local (Windows + WSL), utilizando modelos LLM locales y una API propia.



---



\## 1. Componentes principales



\### 1.1. API (FastAPI)

\- Expone endpoints locales.

\- Permite integrar el agente con herramientas externas.

\- Facilita pruebas, automatización y extensibilidad.



\### 1.2. Backend LLM (Ollama u otro)

\- Ejecuta el modelo local.

\- No depende de servicios externos.

\- Permite razonamiento seguro y reproducible.



\### 1.3. Módulo de Prompts

\- Define el comportamiento del agente.

\- Incluye:

&nbsp; - System prompt

&nbsp; - Roles internos (Orchestrator, Validator)

&nbsp; - Reglas de interacción



\### 1.4. Documentación

\- Describe arquitectura, decisiones técnicas y diseño cognitivo.

\- Permite que un empleador entienda el proyecto sin leer código.



---



\## 2. Flujo de ejecución



1\. El usuario envía una consulta a la API.

2\. La API construye el contexto (system prompt + mensaje del usuario).

3\. El backend LLM procesa la solicitud.

4\. El agente aplica:

&nbsp;  - Orchestrator → propone plan

&nbsp;  - Validator → revisa coherencia

5\. La respuesta final se devuelve al usuario.



---



\## 3. Principios de diseño



\- Modularidad

\- Reproducibilidad

\- Seguridad local

\- Claridad cognitiva

\- Extensibilidad futura (agentes múltiples, herramientas, pipelines)



---



\## 4. Roadmap



\- Integración con Ollama

\- Añadir herramientas (filesystem, shell seguro, analizador de logs)

\- Añadir agentes secundarios

\- Añadir interfaz web

\- Añadir pruebas automatizadas



---



Este documento crecerá a medida que el proyecto evolucione.

