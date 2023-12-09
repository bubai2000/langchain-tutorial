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
    "Please select your language!", ("C", "Python", "Java", "C++", "C#", "JavaScript", "PHP", "VB.NET", "Assembly Language", "Classic Visual Basic", "Fortran", "R", "Ruby", "Go", "Swift", "MATLAB", "Rust", "Kotlin", "Objective-C", "Scala", "Perl", "Prolog", "COBOL", "Delphi/Object Pascal", "Lua", "Haskell", "Erlang", "Groovy", "Julia", "Visual Basic", "Ada", "Eiffel", "F#", "Dart", "CLIPS", "OCaml", "Nim", "Elm", "Scratch", "TypeScript", "VHDL", "Verilog", "Pike", "Swift (Android)", "Kotlin (JVM)", "Ceylon", "Crystal", "Ballerina", "CMake"
                                     ))

problem = st.sidebar.text_area(
    "What is your problem statement?", max_chars=100)

if (language and problem):
    response = ls.code(language=language, problem=problem)
    st.text(response)
