# app.py (Fully integrated with BRD download & Dashboard)
import streamlit as st
import os
from dotenv import load_dotenv
from ai_engine import analyze_request, generate_brd, display_dashboard

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    st.error("OpenAI API key not found in environment. Please set OPENAI_API_KEY in .env")
    st.stop()

# App title
st.title("AI Business Analyst Prototype")

# Sidebar form
st.sidebar.header("Submit Business Request")

business_objective = st.sidebar.text_input(
    "Business Objective", 
    "Monitor cross-asset portfolio risk exposure for daily reporting."
)

asset_class = st.sidebar.selectbox(
    "Asset Class", ["Equities", "Fixed Income", "Multi Asset", "Private Credit"]
)

description = st.sidebar.text_area(
    "Describe the request", 
    "We need a dashboard to track portfolio exposure, generate alerts for high-risk positions, and visualize trends over time."
)

if st.sidebar.button("Analyze Request"):
    request_text = f"Business Objective: {business_objective}\nAsset Class: {asset_class}\nRequest: {description}"
    with st.spinner("Analyzing request..."):
        try:
            # Generate AI output
            ai_output = analyze_request(request_text)
            st.subheader("AI Requirement Analysis")
            st.text(ai_output)

            # Generate BRD and provide download
            brd_file = generate_brd(ai_output)
            st.download_button(
                label="Download BRD",
                data=open(brd_file, "rb").read(),
                file_name=brd_file,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )

            # Display Transformation Dashboard
            display_dashboard()

        except Exception as e:
            st.error(f"Error analyzing request: {e}")