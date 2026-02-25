# API Specification — Local Technical Agent

This document describes the API layer of the **Local Technical Agent**, implemented using FastAPI and designed for local execution only.  
The API acts as the interface between the user (or external tools) and the cognitive engine powered by a local LLM (Ollama).

---

## 1. Overview

The API provides:

- A clean and minimal interface  
- A `/chat` endpoint for interacting with the agent  
- A `/health` endpoint for diagnostics  
- Input validation using Pydantic  
- A clear separation between API logic and cognitive logic  

The API does **not** expose any external network access and is intended for **local use only**.

---

## 2. Endpoints

### **2.1. POST `/chat`**

Main endpoint for interacting with the agent.

#### **Request Body**

```json
{
  "message": "Your question or instruction"
}
```

#### **Response Body**

```json
{
  "response": "Agent's final answer"
}
```

#### **Description**

- Receives a user message  
- Builds the full prompt (System Prompt + Orchestrator + Validator + User Message)  
- Sends the prompt to the local LLM through the Ollama client  
- Returns the final validated answer  

#### **Example Request**

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain the difference between WSL1 and WSL2"}'
```

#### **Example Response**

```json
{
  "response": "WSL2 uses a real Linux kernel with virtualization..."
}
```

---

### **2.2. GET `/health`**

Simple healthcheck endpoint.

#### **Response**

```json
{
  "status": "ok"
}
```

Used to verify that the API is running.

---

## 3. Internal Flow

The `/chat` endpoint follows this sequence:

1. Receive the user message  
2. Build the full prompt using:  
   - System Prompt  
   - Orchestrator section  
   - Validator section  
   - User message  
3. Send the prompt to the local LLM via `ollama.generate()`  
4. Return the final answer  

---

## 4. Code Structure

The API is implemented in:

```
agent/api/main.py
```

Key components:

- **FastAPI app instance**  
- **Pydantic models** (`ChatRequest`, `ChatResponse`)  
- **Prompt builder function**  
- **Ollama client integration**  
- **Endpoints**  

---

## 5. Example: `main.py` Structure

```python
from fastapi import FastAPI
from pydantic import BaseModel
from agent.llm.ollama_client import ollama
from agent.prompts.system_prompt import SYSTEM_PROMPT

app = FastAPI(title="Local Technical Agent")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

def build_prompt(user_message: str) -> str:
    return f"""
{SYSTEM_PROMPT}

## Orchestrator
Analyze the user's message and propose a detailed plan.

User message:
\"\"\"{user_message}\"\"\"

## Validator
Review the Orchestrator's plan, correct errors, and validate the final answer.

## Final Answer
"""

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    prompt = build_prompt(request.message)
    result = ollama.generate(prompt)
    return ChatResponse(response=result)

@app.get("/health")
def health():
    return {"status": "ok"}
```

---

## 6. Design Principles

- Minimal surface area  
- Local-only execution  
- Clear separation of concerns  
- Deterministic behavior  
- Easy to extend with new endpoints  

---

## 7. Future Extensions

- `/analyze` endpoint for system diagnostics  
- `/tools/fs` for safe filesystem operations  
- `/tools/shell` for whitelisted commands  
- `/stream` for streaming LLM responses  
- Authentication for multi-user environments  

---

This API specification will evolve as new capabilities are added.
