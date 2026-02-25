import os
from dotenv import load_dotenv

# Load variables from .env if present
load_dotenv()

class Settings:
    """
    Central configuration for the Local Technical Agent.
    Manages URLs, model names, and backend LLM parameters.
    """

    # URL of the local Ollama server
    OLLAMA_URL: str = os.getenv("OLLAMA_URL", "http://localhost:11434")

    # Default model name
    MODEL_NAME: str = os.getenv("MODEL_NAME", "llama3")

    # Maximum request timeout
    TIMEOUT: int = int(os.getenv("TIMEOUT", "60"))

settings = Settings()
