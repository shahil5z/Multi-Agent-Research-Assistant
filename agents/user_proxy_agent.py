from autogen import ConversableAgent

class UserProxyAgent(ConversableAgent):
    def __init__(self):
        super().__init__(name="UserProxyAgent", system_message="I am the user proxy, collecting input and displaying output.")

    def set_manager(self, manager):
        self.manager = manager

    def initiate_chat(self, recipient, message):
        return recipient.generate_reply(message=message)