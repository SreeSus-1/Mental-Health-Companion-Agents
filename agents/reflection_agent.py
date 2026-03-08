from agents.base_agent import BaseAgent

class ReflectionAgent(BaseAgent):

    def analyze(self, journal_text):

        prompt = f"""
        You are a reflection agent helping someone understand their emotions.

        Analyze the journal entry below.

        Identify:
        - key emotions
        - emotional themes
        - overall tone

        Journal entry:
        {journal_text}
        """

        return self.call_ollama(prompt)