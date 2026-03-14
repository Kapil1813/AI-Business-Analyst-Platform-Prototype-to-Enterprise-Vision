import pandas as pd
import plotly.express as px
import streamlit as st

def show_dashboard():

    data = {
        "Initiative":[
            "Portfolio Risk Dashboard",
            "Trading Data Integration",
            "Multi Asset Analytics",
            "ESG Reporting Engine"
        ],
        "Priority":[
            "High",
            "Medium",
            "High",
            "Low"
        ],
        "Status":[
            "In Progress",
            "Planning",
            "Development",
            "Completed"
        ]
    }

    df = pd.DataFrame(data)

    st.subheader("Active Transformation Initiatives")

    st.dataframe(df)

    fig = px.pie(df, names="Priority", title="Project Priority Distribution")

    st.plotly_chart(fig)