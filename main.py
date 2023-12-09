import services.langchain_service as ls
import streamlit as st

st.title("AI Code generator")

language = st.sidebar.selectbox(
    "Please select your language!", ("Python", "JavaScript", "Rust", "Dart"))

problem = st.sidebar.text_area(
    "What is your problem statement?", max_chars=100)

if (language and problem):
    response = ls.code(language=language, problem=problem)
    st.text(response)
