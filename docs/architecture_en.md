# System Architecture — Local Technical Agent

This document describes the architecture of the **Local Technical Agent**, a modular system designed to run entirely on local hardware (Windows + WSL), using local LLM models, structured prompts, and a clean API layer.

---

## 1. Overview

The Local Technical Agent is built with the following goals:

- 100% local execution  
- Full privacy and security  
- Modular and maintainable architecture  
- Clear cognitive structure (Orchestrator → Validator)  
- Easy debugging and extension  
- Integration with local tools (filesystem, shell, logs)  

The system combines:

- **FastAPI** as the local API layer  
- **Ollama** as the local LLM backend  
- **Structured prompts** defining cognitive behavior  
- **Documentation** for employers and clients  
- **Future tools** (safe filesystem access, shell, log analysis)

---

## 2. Main Components

### 2.1. API Layer (FastAPI)
- Exposes local endpoints  
- Handles requests and validation  
- Provides a clean interface for external tools  
- Ensures separation between UI and cognitive logic  

### 2.2. Local LLM Backend (Ollama)
- Executes the language model locally  
- No external dependencies  
- Deterministic and reproducible  
- Isolated from the API layer  

### 2.3. Prompt Module
Defines the agent’s cognitive behavior:

- **System prompt**  
- **Orchestrator** (planning)  
- **Validator** (review and correction)  
- Response formatting rules  

### 2.4. Documentation Layer
Includes:

- Architecture  
- API specification  
- Roadmap  
- Examples  
- Cognitive design  

This allows employers to understand the system without reading code.

---

## 3. Execution Flow

1. The user sends a request to the API.  
2. The API builds the full prompt (system + user).  
3. The LLM processes the request.  
4. The agent applies:  
   - **Orchestrator** → proposes a plan  
   - **Validator** → reviews and corrects  
5. The final answer is returned to the user.

---

## 4. High-Level Architecture Diagram

```
                ┌──────────────────────────┐
                │          User            │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │       API        │
                    │    (FastAPI)     │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     Prompt Module        │
                │  - System Prompt         │
                │  - Orchestrator          │
                │  - Validator             │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │    Local LLM     │
                    │     (Ollama)     │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Future Local Tools     │
                │  - Safe FS Access        │
                │  - Whitelisted Shell     │
                │  - Log Analysis          │
                └──────────────────────────┘
```

---

## 5. Cognitive Flow Diagram (Orchestrator → Validator)

```
                ┌──────────────────────────┐
                │          User            │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   User Message   │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │       Orchestrator       │
                │  - Proposes a plan       │
                │  - Breaks down steps     │
                │  - Identifies risks      │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │        Validator         │
                │  - Reviews coherence     │
                │  - Fixes inconsistencies │
                │  - Ensures clarity       │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   Final Answer   │
                    └──────────────────┘
```

---

## 6. API → LLM Flow Diagram

```
                ┌──────────────────────────┐
                │          User            │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   API (FastAPI)  │
                    │   /chat endpoint │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     Prompt Module        │
                │  - System Prompt         │
                │  - Orchestrator          │
                │  - Validator             │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │    Local LLM     │
                    │     (Ollama)     │
                    └─────────┬────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Generated Response     │
                └─────────────┬────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │   API → User     │
                    └──────────────────┘
```

---

## 7. Windows ↔ WSL ↔ Ollama Interaction Diagram

```
                   ┌──────────────────────────┐
                   │        Windows 11        │
                   │  - PowerShell            │
                   │  - VSCode                │
                   │  - Git                   │
                   └─────────────┬────────────┘
                                 │
                                 │ Local calls
                                 ▼
                   ┌──────────────────────────┐
                   │          WSL2            │
                   │  Ubuntu Linux            │
                   │  - API (FastAPI)         │
                   │  - Agent Code            │
                   │  - Prompts               │
                   └─────────────┬────────────┘
                                 │
                                 │ LLM requests
                                 ▼
                   ┌──────────────────────────┐
                   │         Ollama           │
                   │  - Local LLM models      │
                   │  - Isolated execution    │
                   └─────────────┬────────────┘
                                 │
                                 ▼
                   ┌──────────────────────────┐
                   │     Final Response       │
                   └──────────────────────────┘
```

---

## 8. Design Principles

- **Modularity**  
- **Reproducibility**  
- **Local security**  
- **Cognitive clarity**  
- **Future extensibility**  
- **Layer isolation**  
- **Windows + WSL compatibility**

---

## 9. Roadmap Summary

- Ollama integration  
- Local tools (FS, shell, logs)  
- Secondary agents  
- Web interface  
- Automated tests  
- Streaming responses  
- Local authentication  

---

This document will evolve as the project grows.
