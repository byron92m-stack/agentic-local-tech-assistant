<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-orange" />
  <img src="https://img.shields.io/badge/WSL2-Ubuntu%2022.04-yellow" />
  <img src="https://img.shields.io/badge/Architecture-Agentic%20AI-purple" />
  <img src="https://img.shields.io/badge/License-MIT-lightgrey" />
</p>

<h1 align="center">Agentic Local Tech Assistant</h1>

<p align="center">
  A fully local, agentic AI assistant running on top of <b>FastAPI</b> and <b>Ollama</b>, designed for clean cognitive architecture, reproducibility, and real-world technical workflows.
</p>

<p align="center">
  <img src="docs/demo.gif" alt="API demo" width="650" />
</p>

---

## 🧩 Overview

This project implements a specialized **technical AI agent** with a modular, role‑based cognitive architecture:

- **Orchestrator** – analyzes user intent and plans the response  
- **Validator** – checks the plan and corrects inconsistencies  
- **Final Answer** – produces a clean, safe, and useful output  

The system runs entirely **locally** using **Ollama**, ensuring:

- full privacy  
- zero external dependencies  
- low latency  
- reproducibility  

This repository demonstrates strong engineering practices, agent architecture design, local LLM integration, and clean API development.

---

## 🧱 Architecture

The system is structured into clear layers:

```text
                          ┌──────────────────────────────┐
                          │        User / Client         │
                          └───────────────┬──────────────┘
                                          │ HTTP (FastAPI)
                                          ▼
                          ┌──────────────────────────────┐
                          │          API Layer           │
                          │        FastAPI / Uvicorn     │
                          └───────────────┬──────────────┘
                                          │
                                          ▼
                          ┌──────────────────────────────┐
                          │      Cognitive Engine        │
                          │ ───────────────────────────── │
                          │ 1. Orchestrator               │
                          │ 2. Validator                  │
                          │ 3. Final Answer               │
                          └───────────────┬──────────────┘
                                          │
                                          ▼
                          ┌──────────────────────────────┐
                          │        LLM Backend           │
                          │        Ollama (Local)        │
                          │   Qwen2.5‑Coder / Llama3     │
                          └───────────────┬──────────────┘
                                          │
                                          ▼
                          ┌──────────────────────────────┐
                          │      Local Hardware (WSL2)   │
                          │   Ubuntu + Python + venv     │
                          └──────────────────────────────┘
```

---

## ⚙️ Technologies Used

- FastAPI  
- Uvicorn  
- Ollama  
- Qwen2.5‑Coder 7B  
- Python 3.12  
- WSL2 + Ubuntu  
- OpenAPI / Swagger  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/byron92m-stack/agentic-local-tech-assistant
cd agentic-local-tech-assistant
```

### 2. Create a virtual environment (WSL)

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

```bash
cp .env.example .env
```

Set your model and Ollama endpoint:

```
MODEL_NAME=qwen2.5-coder:7b
OLLAMA_URL=http://localhost:11434
```

### 5. Start the backend

```bash
uvicorn agent.api.main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🚀 Usage

Open the API documentation:

```
http://localhost:8000/docs
```

Test the `/chat` endpoint with:

```json
{
  "message": "Explain your internal architecture."
}
```

---

## 🎥 Demo GIF (placeholder)

To add a real demo:

1. Install Peek (WSL):
   ```bash
   sudo apt install peek
   ```
2. Open `http://localhost:8000/docs`
3. Record a short interaction
4. Save as `docs/demo.gif`
5. Commit and push

The README will display it automatically.

---

## 🧠 Skills Demonstrated

- Agent design with explicit reasoning roles  
- Modular architecture and controlled reasoning  
- Local LLM integration with Ollama  
- Backend development with FastAPI  
- Engineering best practices (venv, .env, reproducibility)  
- Advanced debugging across Windows and WSL  
- Professional documentation  
- API design with OpenAPI  
- Practical use of LLMs in local environments  

---

## 🔐 Security

- No API keys or sensitive data are exposed  
- `.env` is ignored by Git  
- All inference runs locally  
- Full privacy by design  

---

## 👤 About Me

I am a technical architect specialized in **local AI systems**, **agentic architectures**, and **modular backend design**.  
My work focuses on building **fully local, privacy‑preserving AI assistants** with clean cognitive flows and reproducible engineering practices.

### What I bring to a team

- Strong architectural thinking  
- Clean, maintainable code  
- Experience with LLM orchestration  
- Deep understanding of WSL2, Linux, and local environments  
- Ability to design systems that scale  
- Clear documentation and communication  

### What I enjoy building

- Local AI agents  
- Cognitive architectures  
- FastAPI backends  
- ML pipelines  
- Developer tools  
- Automation systems  

---

## 🎤 Technical Pitch

This project demonstrates my ability to design and implement a **fully local agentic AI system** with a clean cognitive architecture and a production‑ready API layer.

I built a modular reasoning engine composed of:

- an **Orchestrator** that interprets intent  
- a **Validator** that ensures logical consistency  
- a **Final Answer** module that produces safe, structured output  

The system runs entirely on **local hardware** using **Ollama** as the LLM backend, ensuring privacy, reproducibility, and zero cloud dependency.

The backend is implemented with **FastAPI**, following clean architectural boundaries and extensible design principles.

---

## 📝 License

MIT License (recommended)