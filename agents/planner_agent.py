from autogen import ConversableAgent
from groq import Groq
from core.config import load_groq_config

class PlannerAgent(ConversableAgent):
    def __init__(self):
        with open("prompts/planner_prompt.txt", "r") as f:
            prompt = f.read()
        super().__init__(name="PlannerAgent", system_message=prompt)
        self.groq_config = load_groq_config()

    def set_manager(self, manager):
        self.manager = manager

    def generate_reply(self, message, **kwargs):
        # Initialize Groq client
        client = Groq(api_key=self.groq_config["api_key"])
        
        # Prepare prompt with the topic
        prompt = f"{self.system_message}\nTopic: {message}\nProvide 4-6 subtopics as a numbered list."
        
        # Call Groq API to generate subtopics
        try:
            response = client.chat.completions.create(
                model=self.groq_config["model"],
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )
            subtopics = response.choices[0].message.content.strip()
            return subtopics
        except Exception as e:
            # Fallback to default subtopics in case of API failure
            print(f"Error generating subtopics: {str(e)}")
            default_subtopics = [
                "Introduction to the Topic",
                "Key Applications and Use Cases",
                "Benefits and Advantages",
                "Challenges and Limitations",
                "Future Trends and Predictions",
                "Conclusion"
            ]
            return "\n".join(default_subtopics)