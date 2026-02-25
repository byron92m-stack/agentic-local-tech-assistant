# Project Roadmap — Local Technical Agent

This roadmap outlines the planned evolution of the **Local Technical Agent**, focusing on modularity, local execution, cognitive clarity, and extensibility.  
The goal is to build a production‑grade, fully local AI system that employers and clients can easily understand, evaluate, and extend.

---

## 1. Phase 1 — Core Foundations (Completed)

### ✔ Architecture & Structure
- Modular folder layout (`agent/api`, `agent/llm`, `agent/prompts`)
- Clean separation between API, LLM backend, and cognitive logic
- English documentation for employers and clients

### ✔ System Prompt & Cognitive Flow
- Orchestrator → Validator → Final Answer
- Deterministic, structured reasoning
- Clear formatting rules

### ✔ API Layer
- `/chat` endpoint
- `/health` endpoint
- Pydantic request/response models
- Prompt builder function

### ✔ Local LLM Integration
- Ollama client wrapper
- `.env` configuration
- Local-only execution

---

## 2. Phase 2 — Enhanced LLM Integration (In Progress)

### 🔄 Improve Prompting & Cognitive Behavior
- Add memory‑less deterministic mode
- Add “analysis mode” for technical debugging
- Add “explain mode” for educational output

### 🔄 Add Streaming Support
- Server‑sent events (SSE)
- Token‑by‑token streaming from Ollama

### 🔄 Add Model Switching
- Allow selecting different local models
- Add `/models` endpoint to list available models

---

## 3. Phase 3 — Local Tools (Upcoming)

The agent will gain controlled access to local system capabilities.

### 🗂 Filesystem Tools (Safe)
- Read‑only file inspection
- Directory listing
- Log file parsing
- JSON/YAML/TOML inspection

### 🖥 Shell Tools (Whitelisted)
- Only safe commands allowed
- No destructive operations
- Full audit logging

### 📊 System Diagnostics
- CPU, RAM, disk usage
- WSL performance metrics
- Network status

---

## 4. Phase 4 — Multi‑Agent Architecture

### 🤖 Secondary Agents
- “Research Agent” (local file analysis)
- “Debug Agent” (WSL, Docker, Python issues)
- “Ops Agent” (system monitoring)
- “Prompt Engineer Agent” (prompt refinement)

### 🧠 Orchestrator Controller
- Route tasks to the correct agent
- Validate outputs
- Merge responses

---

## 5. Phase 5 — Developer Experience (DX)

### 🧪 Automated Testing
- Unit tests for API
- Mocked LLM responses
- Integration tests

### 📝 Logging & Observability
- Rich‑based structured logs
- Request/response tracing
- Error reporting

### 🧰 CLI Tool
- `agentctl` command
- Start/stop server
- Run diagnostics
- Inspect logs

---

## 6. Phase 6 — User Interface

### 🌐 Web Dashboard
- Chat interface
- System metrics
- File explorer (read‑only)
- Logs viewer

### 🪟 Windows Integration
- Tray icon
- Quick actions
- Local notifications

---

## 7. Phase 7 — Security & Hardening

### 🔐 Authentication
- Local token‑based auth
- Role‑based access for tools

### 🛡 Sandboxing
- Strict isolation for shell tools
- Read‑only filesystem by default

### 📜 Audit Logs
- Every tool call logged
- Full traceability

---

## 8. Phase 8 — Packaging & Distribution

### 📦 Installer
- Windows installer (MSI)
- Auto‑start service
- WSL environment validation

### 🧩 Plugin System
- Add new tools without modifying core
- Hot‑reload capabilities

---

## 9. Long‑Term Vision

The Local Technical Agent becomes:

- A **fully local AI assistant**
- A **developer productivity tool**
- A **system debugging companion**
- A **WSL/Linux/Windows expert**
- A **modular multi‑agent platform**
- A **private alternative to cloud AI tools**

---

This roadmap will evolve as the project grows and new requirements emerge.
