from autogen import ConversableAgent

class WriterAgent(ConversableAgent):
    def __init__(self):
        with open("prompts/writer_prompt.txt", "r") as f:
            prompt = f.read()
        super().__init__(name="WriterAgent", system_message=prompt)

    def set_manager(self, manager):
        self.manager = manager

    def generate_reply(self, message, **kwargs):
        # Simulated article composition
        sections = message.split("## ")[1:]  # Split by subtopic headers
        article = "# Research Report\n\n"
        article += "## Introduction\nThis report explores the given topic in detail.\n\n"
        for section in sections:
            article += f"## {section}\n"
        article += "## Conclusion\nThis report has covered key aspects of the topic.\n"
        return article