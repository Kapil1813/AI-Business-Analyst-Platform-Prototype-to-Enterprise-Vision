# ai_engine.py (Production-ready with BRD generation & dashboard support)
from openai import OpenAI
from docx import Document
import streamlit as st

# Initialize OpenAI client (reads API key from environment variable)
client = OpenAI()

def analyze_request(request_text: str) -> str:
    prompt = f"Analyze this business request and generate functional requirements, non-functional requirements, user stories, and architecture suggestions:\n{request_text}"
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def generate_brd(ai_output: str, file_name: str = "BRD_Output.docx") -> str:
    """Generates a Word document (BRD) from AI output and returns the file path."""
    doc = Document()
    doc.add_heading("Business Requirements Document (BRD)", 0)
    doc.add_paragraph(ai_output)
    doc.save(file_name)
    return file_name


def display_dashboard():
    """Displays example transformation metrics on Streamlit."""
    import pandas as pd
    import plotly.express as px

    st.subheader("Transformation Dashboard")

    # Example metrics
    data = pd.DataFrame({
        "Initiative": ["Project A", "Project B", "Project C", "Project D"],
        "Priority": [5, 3, 4, 2],
        "Status": ["Active", "Delayed", "Active", "Completed"],
        "Completion (%)": [70, 40, 60, 100]
    })

    st.table(data)

    fig = px.bar(data, x="Initiative", y="Completion (%)", color="Status", text="Completion (%)")
    st.plotly_chart(fig, use_container_width=True)