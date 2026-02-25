from fastapi import FastAPI
from pydantic import BaseModel
from agent.llm.ollama_client import ollama
from agent.prompts.system_prompt import SYSTEM_PROMPT

app = FastAPI(title="Local Technical Agent")

# -----------------------------
# Pydantic Models
# -----------------------------

class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


# -----------------------------
# Prompt Builder
# -----------------------------

def build_prompt(user_message: str) -> str:
    """
    Builds the full prompt by combining:
    - System prompt
    - Orchestrator
    - Validator
    - User message
    """

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


# -----------------------------
# Main Endpoint
# -----------------------------

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    """
    Main endpoint of the Local Technical Agent.
    """
    prompt = build_prompt(request.message)
    result = ollama.generate(prompt)
    return ChatResponse(response=result)


# -----------------------------
# Healthcheck
# -----------------------------

@app.get("/health")
def health():
    return {"status": "ok"}
