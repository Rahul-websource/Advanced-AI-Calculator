import streamlit as st
import math

st.title("🧮 AI-Powered Calculator")

expr = st.text_input("Enter expression")
if st.button("Evaluate"):
    try:
        result = eval(expr, {"__builtins__": None}, math.__dict__)
        st.success(f"Result = {result}")
    except Exception:
        st.error("Invalid expression")
