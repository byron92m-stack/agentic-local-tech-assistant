import requests
from agent.config import settings

class OllamaClient:
    """
    HTTP client for interacting with the local Ollama server
    in a safe, controlled, and modular way.
    """

    def __init__(self, base_url: str = None, model: str = None):
        self.base_url = base_url or settings.OLLAMA_URL
        self.model = model or settings.MODEL_NAME

    def generate(self, prompt: str) -> str:
        """
        Sends a prompt to the local LLM model and returns the generated response.
        """
        url = f"{self.base_url}/api/generate"

        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(url, json=payload, timeout=settings.TIMEOUT)
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            return f"[ERROR] Could not connect to Ollama: {e}"

        data = response.json()
        return data.get("response", "").strip()

# Global instance ready to use
ollama = OllamaClient()
