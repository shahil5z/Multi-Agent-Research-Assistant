from autogen import ConversableAgent
from groq import Groq
from core.config import load_groq_config

class ResearchAgent(ConversableAgent):
    def __init__(self):
        with open("prompts/research_prompt.txt", "r") as f:
            prompt = f.read()
        super().__init__(name="ResearchAgent", system_message=prompt)
        self.groq_config = load_groq_config()

    def set_manager(self, manager):
        self.manager = manager

    def generate_reply(self, message, config=None):
        client = Groq(api_key=self.groq_config["api_key"])
        prompt = self.system_message.replace("{{subtopic}}", message)
        response = client.chat.completions.create(
            model=self.groq_config["model"],
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content