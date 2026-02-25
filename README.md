# Local Technical AI Agent  
A modular technical agent with controlled reasoning, FastAPI backend, and local LLM inference via Ollama.

## Overview

This project implements a specialized **technical AI agent** designed with a modular architecture based on explicit roles:

- **Orchestrator** – analyzes user intent and plans the response  
- **Validator** – checks the plan and corrects inconsistencies  
- **Final Answer** – delivers a clear, safe, and useful output  

The agent runs entirely **locally** using **Ollama** as the inference engine, ensuring:

- full privacy  
- zero external dependencies  
- low latency  
- reproducibility  

This project demonstrates strong engineering practices, agent architecture design, local LLM integration, and clean API development.

## Technologies Used

- FastAPI  
- Uvicorn  
- Ollama  
- Qwen2.5‑Coder 7B  
- Python 3.12 (WSL)  
- WSL2 + Ubuntu  
- OpenAPI / Swagger  

## Agent Architecture

User Input → Orchestrator → Validator → Final Answer → Ollama (Qwen2.5‑Coder)

## Installation

1. Clone the repository  
   git clone https://github.com/yourusername/agentic-local-tech-assistant  
   cd agentic-local-tech-assistant  

2. Create a virtual environment (WSL)  
   python3 -m venv venv  
   source venv/bin/activate  

3. Install dependencies  
   pip install -r requirements.txt  

4. Create a .env file with model configuration  
   MODEL_NAME=qwen2.5-coder:7b  
   OLLAMA_URL=http://localhost:11434  

5. Start the backend  
   uvicorn agent.api.main:app --reload --host 0.0.0.0  

## Usage

Open the API documentation in your browser:  
http://localhost:8000/docs  

Test the /chat endpoint by sending a message such as:  
{ "message": "Explain your internal architecture." }

## Skills Demonstrated

- Agent design with explicit reasoning roles  
- Modular architecture and controlled reasoning  
- Local LLM integration with Ollama  
- Backend development with FastAPI  
- Engineering best practices (venv, .env, reproducibility)  
- Advanced debugging across Windows and WSL  
- Professional documentation  
- API design with OpenAPI  
- Practical use of LLMs in local environments  

## Security

This project does not expose any keys or sensitive data.  
The model runs locally, ensuring full privacy.  
It is recommended to keep the .env file out of version control.

## License

You may use any license you prefer (MIT, Apache 2.0, etc.).  
If unsure, MIT is a safe and widely used option.
