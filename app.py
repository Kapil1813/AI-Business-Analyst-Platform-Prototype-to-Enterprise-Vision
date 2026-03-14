# app.py
import streamlit as st
import os
from dotenv import load_dotenv
import openai
from ai_engine import analyze_request, generate_brd, display_dashboard

# --- Load .env ---
load_dotenv()

# --- Get OpenAI API key ---
try:
    API_KEY = st.secrets["OPENAI_API_KEY"]
except (AttributeError, KeyError):
    API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    st.error("OpenAI API key not found. Set it in .env or Streamlit secrets.")
    st.stop()

# --- Validate API key ---
openai.api_key = API_KEY
try:
    openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Say hello"}],
        max_tokens=5
    )
except Exception as e:
    st.error(f"Invalid OpenAI API key or network issue: {e}")
    st.stop()

# --- App UI ---
st.title("AI Business Analyst Prototype")

st.sidebar.header("Submit Business Request")
business_objective = st.sidebar.text_input(
    "Business Objective",
    "Monitor cross-asset portfolio risk exposure for daily reporting."
)
asset_class = st.sidebar.selectbox(
    "Asset Class", ["Equities", "Fixed Income", "Multi Asset", "Private Credit"]
)
description = st.sidebar.text_area(
    "Request Description",
    "We need a dashboard to track portfolio exposure, generate alerts for high-risk positions, and visualize trends over time."
)

if st.sidebar.button("Analyze Request"):
    request_text = f"Business Objective: {business_objective}\nAsset Class: {asset_class}\nRequest: {description}"

    with st.spinner("Generating requirements..."):
        # --- Call AI ---
        ai_output = analyze_request(request_text, api_key=API_KEY)

        # --- Display AI output ---
        st.subheader("AI Generated Requirements")
        st.text(ai_output)

        # --- Generate BRD ---
        brd_bytes, brd_filename = generate_brd(
            business_objective, asset_class, description, ai_output
        )
        st.download_button(
            label="Download BRD",
            data=brd_bytes,
            file_name=brd_filename,
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

        # --- Display Dashboard ---
        display_dashboard()