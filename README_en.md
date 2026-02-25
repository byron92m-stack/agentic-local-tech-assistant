# Local Technical Agent — Fully Local AI System

The **Local Technical Agent** is a modular, privacy‑focused AI system designed to run entirely on local hardware (Windows + WSL2).  
It provides a structured cognitive engine, a clean API layer, and a foundation for future local tools such as filesystem inspection, shell utilities, and system diagnostics.

This project is built for employers, clients, and engineers who need a **fully local**, **secure**, and **extensible** AI assistant.

---

## 🚀 Key Features

- **100% local execution** (no cloud dependencies)
- **FastAPI** backend with clean, documented endpoints
- **Ollama** as the local LLM engine
- **Structured cognitive flow**  
  - Orchestrator → Validator → Final Answer
- **Modular architecture** for long‑term maintainability
- **English documentation** for professional review
- **Future‑ready design** for tools, agents, and UI extensions

---

## 🧠 Cognitive Architecture

The agent follows a deterministic reasoning structure:

1. **Orchestrator**  
   - Analyzes the user message  
   - Proposes a plan  
   - Breaks down steps  

2. **Validator**  
   - Reviews the plan  
   - Fixes inconsistencies  
   - Ensures clarity  

3. **Final Answer**  
   - Clean, validated output  

This structure ensures reliability, transparency, and predictable behavior.

---

## 🏗 Project Structure

```
agent/
  api/
    main.py              → FastAPI endpoints
  llm/
    ollama_client.py     → Local LLM wrapper
  prompts/
    system_prompt.md     → Cognitive design (markdown)
    system_prompt.py     → Python constant for API
  config.py              → Environment configuration

docs/
  architecture_en.md     → System architecture
  api_en.md              → API specification
  roadmap_en.md          → Development roadmap
  examples_en.md         → Usage examples
  README_en.md           → Documentation index

.env                      → Local configuration
requirements.txt          → Python dependencies
README_en.md              → Main project README (this file)
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone <your-repo-url>
cd agentic-local-tech-assistant
```

### 2. Install dependencies

```
pip install -r requirements.txt
```

### 3. Start the API

```
python -m uvicorn agent.api.main:app --reload
```

### 4. Open the interactive docs

```
http://localhost:8000/docs
```

---

## 🔌 API Endpoints

### **POST `/chat`**
Main interaction endpoint.

**Request**
```json
{
  "message": "Explain WSL2 architecture."
}
```

**Response**
```json
{
  "response": "WSL2 uses a real Linux kernel with virtualization..."
}
```

### **GET `/health`**
Healthcheck endpoint.

---

## 🧩 LLM Backend (Ollama)

The agent communicates with a local LLM through:

```
http://localhost:11434/api/generate
```

Configured via `.env`:

```
OLLAMA_URL=http://localhost:11434
MODEL_NAME=llama3
TIMEOUT=60
```

---

## 🛣 Roadmap (High‑Level)

- Streaming responses  
- Model switching  
- Local filesystem tools  
- Whitelisted shell tools  
- System diagnostics  
- Multi‑agent architecture  
- Web dashboard  
- Authentication & sandboxing  
- Packaging & installer  

Full roadmap available in `docs/roadmap_en.md`.

---

## 🎯 Purpose of This Project

This project demonstrates:

- Engineering clarity  
- Modular system design  
- Local AI integration  
- Cognitive architecture design  
- Documentation quality  
- Production‑ready structure  

It is suitable for:

- Technical interviews  
- Portfolio demonstration  
- Client evaluation  
- Local AI experimentation  

---

## 📄 License

This project is currently private and intended for professional evaluation and personal development.

---

If you are reviewing this project as part of a hiring process, feel free to explore the architecture, API, and documentation to understand the engineering principles behind the Local Technical Agent.
