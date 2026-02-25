# Documentación de la API

La API del **Agente Técnico Local** está construida con FastAPI y expone endpoints locales para interactuar con el agente y sus herramientas.

---

## 1. Endpoints actuales

### `GET /health`

**Descripción:**  
Verifica que la API esté operativa.

**Respuesta:**

```json
{
  "status": "ok",
  "message": "Agente técnico local operativo (modo demo)."
}
```