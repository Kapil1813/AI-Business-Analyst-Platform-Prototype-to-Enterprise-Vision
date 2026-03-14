# app.py
import streamlit as st
import os
from dotenv import load_dotenv
from ai_engine import analyze_request
from brd_generator import generate_brd
from similarity_engine import find_similar
from dashboard import show_dashboard

# Load environment variables from .env
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

st.set_page_config(page_title="AI Business Analyst Platform", layout="wide")
st.title("AI Business Analyst & Requirement Intelligence Platform")

st.sidebar.header("Investment Request Intake")

# Remove API key input box
# api_key = st.sidebar.text_input("OpenAI API Key", type="password")

objective = st.sidebar.text_input("Business Objective")
asset_class = st.sidebar.selectbox(
    "Asset Class",
    ["Equities","Fixed Income","Multi Asset","Private Credit"]
)
description = st.sidebar.text_area("Describe the request")
submit = st.sidebar.button("Analyze Request")

if submit:
    request_text = f"""
    Objective: {objective}

    Asset Class: {asset_class}

    Description: {description}
    """

    st.header("AI Requirement Analysis")
    ai_output = analyze_request(request_text, API_KEY)  # use API_KEY from .env
    st.write(ai_output)

    st.header("Similar Requests")
    similarity = find_similar(description)
    st.write(similarity)

    st.header("Generate BRD")
    file = generate_brd(objective, asset_class, description, ai_output)
    with open(file, "rb") as f:
        st.download_button(
            "Download BRD",
            f,
            file_name=file
        )

st.header("Transformation Dashboard")
show_dashboard()