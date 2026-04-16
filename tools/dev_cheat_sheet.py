import streamlit as st

def run(client):
    st.title("📚 Dev Cheat Sheet")
    st.caption("Your reusable commands and code snippets.")

    st.divider()

    st.subheader("🖥️ Terminal Commands")

    st.code("""streamlit run app.py
python3 -m streamlit run app.py
git add .
git commit -m "your message"
git pull --rebase origin main
git push
""")

    st.subheader("🧩 Streamlit Snippets")

    st.code("""st.text_area(
    "Paste your code:",
    label_visibility="collapsed",
    key="unique_key"
)
""", language="python")

    st.subheader("🐞 Debug Patterns")

    st.markdown("""
- Duplicate element error → add `key=`
- Git push rejected → `git pull --rebase`
- Yellow warning → variable mismatch
""")