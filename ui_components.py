import streamlit as st

def custom_css():
    st.markdown("""
    <style>
    html, body {
        background: #0f172a;
        color: #e5e7eb;
        font-family: Segoe UI;
    }
    .app-title {
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
    }
    .card {
        padding: 1.2rem;
        border-radius: 10px;
        background: rgba(15,23,42,0.7);
        margin-bottom: 1.5rem;
        border: 1px solid #1e293b;
    }
    </style>
    """, unsafe_allow_html=True)
