import streamlit as st
import pandas as pd
import plotly.express as px

def show_dashboard(risks, mitigations):
    st.subheader("📊 Classificazione dei Rischi")
    df = pd.DataFrame(risks)
    st.dataframe(df)

    if not df.empty:
        fig = px.histogram(df, x="category", title="Distribuzione dei Rischi")
        st.plotly_chart(fig)

    st.subheader("🛡️ Suggerimenti di Mitigazione")
    for suggestion in mitigations:
        st.markdown(f"- {suggestion}")
