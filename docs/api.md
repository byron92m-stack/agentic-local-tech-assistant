# Documentación de la API

La API del **Agente Técnico Local** está construida con FastAPI y expone endpoints locales para interactuar con el agente y sus herramientas.  
Este documento describe los endpoints actuales y los planificados para futuras versiones.

---

## 1. Endpoints actuales

### `GET /health`

**Descripción:**  
Verifica que la API esté operativa y accesible.

**Ejemplo de request:**

```bash
curl http://127.0.0.1:8000/health
```

**Ejemplo de respuesta:**

```json
{
  "status": "ok",
  "message": "Agente técnico local operativo (modo demo)."
}
```

---

## 2. Endpoints planificados

### `POST /chat`

**Estado:** planificado  
**Descripción:**  
Endpoint principal para enviar mensajes al agente y recibir respuestas generadas por el modelo local.

**Request esperado:**

```json
{
  "message": "Explica cómo funciona WSL2."
}
```

**Respuesta esperada (conceptual):**

```json
{
  "response": "WSL2 funciona mediante una máquina virtual ligera que ejecuta un kernel Linux real..."
}
```

---

### `POST /tools/fs`

**Estado:** planificado  
**Descripción:**  
Permite leer archivos locales de manera segura (solo rutas whitelisted).

**Request esperado:**

```json
{
  "path": "C:/Users/Acer/projects/config.yaml"
}
```

---

### `POST /tools/shell`

**Estado:** planificado  
**Descripción:**  
Permite ejecutar comandos whitelisted en un entorno controlado.

**Ejemplo conceptual:**

```json
{
  "command": "ls -la"
}
```

---

## 3. Ejecución local

Para iniciar la API en modo desarrollo:

```bash
uvicorn agent.api.main:app --reload
```

La API estará disponible en:

```
http://127.0.0.1:8000
```

---

## 4. Roadmap de la API

- Añadir streaming de respuestas  
- Añadir autenticación local  
- Añadir logging estructurado  
- Añadir pruebas automatizadas  
- Añadir endpoints para agentes secundarios  
- Añadir herramientas adicionales (análisis de logs, inspección de archivos, etc.)

---

Este archivo crecerá a medida que la API evolucione.
