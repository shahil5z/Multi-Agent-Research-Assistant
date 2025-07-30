from autogen import ConversableAgent

class CriticAgent(ConversableAgent):
    def __init__(self):
        with open("prompts/critic_prompt.txt", "r") as f:
            prompt = f.read()
        super().__init__(name="CriticAgent", system_message=prompt)

    def set_manager(self, manager):
        self.manager = manager

    def generate_reply(self, message, **kwargs):
        # Simulated review logic
        return f"{message}\n\n**Critic Review**: The article is well-structured and complete. Approved."