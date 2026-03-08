from agents.base_agent import BaseAgent

class CognitiveReframeAgent(BaseAgent):

    def reframe(self, journal_text):

        prompt = f"""
        You are a compassionate mental wellness coach.

        Provide supportive advice and a positive cognitive reframe
        for the following journal entry.

        Be encouraging and empathetic.

        Journal entry:
        {journal_text}
        """

        return self.call_ollama(prompt)