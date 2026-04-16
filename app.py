import streamlit as st
import os
from openai import OpenAI

from tools import debug_helper, code_explainer, prompt_improver, test_case_generator, dev_cheat_sheet

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

st.sidebar.title("🧰 AI Toolbox")
st.sidebar.markdown("A growing collection of practical AI tools")
st.sidebar.divider()

st.markdown("""
# 🚀 AI Dev Assistant

### Debug • Understand • Improve

A suite of AI-powered tools for developers.
""")

st.divider()

st.markdown("""
**What you can do:**

- 🐞 Fix bugs instantly  
- 💻 Break down code step-by-step  
- ✨ Turn rough ideas into powerful prompts  
""")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🐞 Debug Assistant",
    "💻 Code Explainer",
    "✨ Prompt Improver",
    "🧪 Test Case Generator",
    "📚 Dev Cheat Sheet"
])


with tab1:
    debug_helper.run(client)

with tab2:
    code_explainer.run(client)

with tab3:
    prompt_improver.run(client)

with tab4:
    test_case_generator.run(client)

with tab5:
    dev_cheat_sheet.run(client)