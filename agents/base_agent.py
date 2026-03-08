import requests

class BaseAgent:

    def __init__(self, model="phi3"):
        self.model = model

    def call_ollama(self, prompt):

        try:

            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                },
                timeout=300
            )

            response.raise_for_status()

            return response.json()["response"]

        except Exception as e:

            return f"ERROR: {str(e)}"