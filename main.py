import services.langchain_service as ls
import streamlit as st
import json
import os

with open("gcp.json", "w") as file:
    json.dump(st.secrets["gcp_service_account"], file, default=dict)
    file.close()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp.json"

st.title("AI Code generator")

language = st.sidebar.selectbox(
    "Please select your language!", ("Python", "JavaScript", "Rust", "Dart"))

problem = st.sidebar.text_area(
    "What is your problem statement?", max_chars=100)

if (language and problem):
    response = ls.code(language=language, problem=problem)
    st.text(response)
