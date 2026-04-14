import streamlit as st
from openai import OpenAI

# This will connect to OpenAI later
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.title("🧰 AI Debug Helper")

user_input = st.text_area("Paste your error or code:")

if st.button("Analyze"):
    if user_input:
        with st.spinner("Analyzing your code..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=f"""
You are a helpful debugging assistant.

A user pasted the following error or code:
{user_input}

Explain:
1. What the issue likely means
2. Why it happened
3. How to fix it

Be clear and beginner-friendly.
"""
            )

        st.subheader("🧠 Explanation")
        st.write(response.output_text)