import streamlit as st
from agents.user_proxy_agent import UserProxyAgent
from agents.planner_agent import PlannerAgent
from agents.research_agent import ResearchAgent
from agents.writer_agent import WriterAgent
from agents.critic_agent import CriticAgent
from core.agent_manager import AgentManager
from core.config import load_groq_config
import os
from fpdf import FPDF
import datetime

# Streamlit page configuration
st.set_page_config(page_title="SmartScribe: AI-Powered Research & Reporting", page_icon="🧠", layout="wide")

# Initialize session state for report and status
if 'report' not in st.session_state:
    st.session_state.report = None
if 'status' not in st.session_state:
    st.session_state.status = "Idle"

# Streamlit UI
st.title("SmartScribe: AI-Powered Research & Reporting")
st.markdown("Enter a research topic, and our AI team will generate a comprehensive report.")

# Input form
with st.form(key="research_form"):
    topic = st.text_input("Enter Research Topic", placeholder="e.g., Impact of Artificial Intelligence on Education")
    submit_button = st.form_submit_button(label="Generate Report")

# Initialize agents
groq_config = load_groq_config()
agent_manager = AgentManager(groq_config)

# Process submission
if submit_button and topic:
    st.session_state.status = "Processing..."
    st.info("Generating report. Please wait...")

    try:
        # Create agents
        user_proxy = UserProxyAgent()
        planner = PlannerAgent()
        researcher = ResearchAgent()
        writer = WriterAgent()
        critic = CriticAgent()

        # Register agents
        agent_manager.register_agents([user_proxy, planner, researcher, writer, critic])

        # Execute workflow
        final_report = agent_manager.execute_workflow(topic)

        # Store report in session state
        st.session_state.report = final_report
        st.session_state.status = "Completed"

        # Display report
        st.markdown("## Generated Report")
        st.markdown(final_report)

        # Save report to file
        os.makedirs("outputs", exist_ok=True)
        report_path = os.path.join("outputs", "generated_report.txt")
        with open(report_path, "w", encoding="utf-8") as f:
            f.write(final_report)

        # Generate PDF
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, final_report.encode('latin-1', 'replace').decode('latin-1'))
        pdf_output_path = os.path.join("outputs", f"report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf")
        pdf.output(pdf_output_path)

        # Provide download button
        with open(pdf_output_path, "rb") as f:
            st.download_button(
                label="Download Report as PDF",
                data=f,
                file_name=os.path.basename(pdf_output_path),
                mime="application/pdf"
            )

    except Exception as e:
        st.session_state.status = "Error"
        st.error(f"An error occurred: {str(e)}")

# Display status
st.write(f"Status: {st.session_state.status}")