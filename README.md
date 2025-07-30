# SmartScribe: AI-Powered Research & Reporting

## Overview

**SmartScribe** is a multi-agent AI system designed to generate comprehensive research reports or blog articles on user-defined topics. It leverages **Microsoft Autogen** for orchestrating AI agents, **Groq LLM API** for fast and accurate content generation, and **Streamlit** for an intuitive user interface.

---

## Features

- **User Input**: Enter any research topic through a simple Streamlit-based web interface.
- **Agent Collaboration**: A team of five AI agents work together:
  - `UserProxy`: Accepts user input
  - `Planner`: Breaks the topic into sub-sections
  - `Researcher`: Gathers content for each sub-topic
  - `Writer`: Drafts the complete report
  - `Critic`: Reviews and finalizes the report
- **Structured Output**: Generates a well-formatted research report with the following sections:
  - Introduction  
  - Applications  
  - Benefits  
  - Challenges  
  - Future Trends  
  - Conclusion
- **PDF Download**: Download the final report as a PDF using FPDF.
- **Tech Stack**:  
  - Python  
  - Streamlit  
  - Autogen (Microsoft)  
  - Groq API  
  - FPDF

---

## Example

**Input Topic**:  
`Impact of Artificial Intelligence on Education`

**Generated Output**:  
A structured report containing:
- Introduction  
- Applications  
- Benefits  
- Challenges  
- Future Trends  
- Conclusion
- Download Option to your local pc

---

## Screenshots

![image alt](https://github.com/shahil5z/Multi-Agent-Research-Assistant/blob/32c57c100a8c7868ca39210301ad1e3cda94457f/SampleIMG/1.png)
![image alt](https://github.com/shahil5z/Multi-Agent-Research-Assistant/blob/32c57c100a8c7868ca39210301ad1e3cda94457f/SampleIMG/2.png)
![image alt](https://github.com/shahil5z/Multi-Agent-Research-Assistant/blob/32c57c100a8c7868ca39210301ad1e3cda94457f/SampleIMG/3.png)
![image alt](https://github.com/shahil5z/Multi-Agent-Research-Assistant/blob/32c57c100a8c7868ca39210301ad1e3cda94457f/SampleIMG/4.png)
