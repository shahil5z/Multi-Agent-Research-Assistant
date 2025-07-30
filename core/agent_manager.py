from autogen import ConversableAgent

class AgentManager:
    def __init__(self, groq_config):
        self.agents = {}
        self.groq_config = groq_config

    def register_agents(self, agents):
        for agent in agents:
            self.agents[agent.name] = agent
            agent.set_manager(self)

    def execute_workflow(self, topic):
        user_proxy = self.agents["UserProxyAgent"]
        planner = self.agents["PlannerAgent"]
        researcher = self.agents["ResearchAgent"]
        writer = self.agents["WriterAgent"]
        critic = self.agents["CriticAgent"]

        # Step 1: UserProxy forwards topic to Planner
        subtopics = user_proxy.initiate_chat(planner, message=topic)

        # Step 2: Planner breaks topic into subtopics
        planner_response = planner.generate_reply(message=topic)
        subtopics_list = planner_response.split("\n")

        # Step 3: Researcher gathers content for each subtopic
        research_content = []
        for subtopic in subtopics_list:
            if subtopic.strip():
                research_result = researcher.generate_reply(message=subtopic, config=self.groq_config)
                research_content.append({"subtopic": subtopic, "content": research_result})

        # Step 4: Writer compiles research into article
        writer_input = "\n".join([f"## {item['subtopic']}\n{item['content']}" for item in research_content])
        article = writer.generate_reply(message=writer_input)

        # Step 5: Critic reviews the article
        final_article = critic.generate_reply(message=article)

        return final_article