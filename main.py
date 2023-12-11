import services.vertex_chat_service as vcs
import streamlit as st
import json
import os
import pandas as pd

with open("gcp.json", "w") as file:
    json.dump(st.secrets["gcp_service_account"], file, default=dict)
    file.close()

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gcp.json"

st.title("CSV Data Analyzer")

file = st.file_uploader("Choose CSV a file")

if file is not None:
    try:
        df = pd.read_csv(file)
        st.dataframe(df)
        query = st.text_area("Enter your query", max_chars=100)
        result = vcs.run(query=query, dataframe=df)
        st.text(result)
    except Exception as e:
        st.text(f"Error occured! {e}")
