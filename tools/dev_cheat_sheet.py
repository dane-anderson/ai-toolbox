import streamlit as st

def run(client):
    st.subheader("Dev Cheat Sheet")
    st.caption("Fast reference for reusable commands, snippets, and fixes.")

    st.divider()

    st.markdown("### AI Integration")
    st.code(
        '''from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what this code does"
)

print(response.output_text)''',
        language="python"
    )
    st.caption("Basic OpenAI client setup and response call.")

    st.code(
        '''import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)''',
        language="python"
    )
    st.caption("Use environment variables for API key setup.")

    st.divider()

    st.markdown("### Deployment")
    st.code(
        '''git add .
git commit -m "your message"
git push''',
        language="bash"
    )
    st.caption("Push to GitHub. Render auto-deploys the latest commit.")

    st.code(
        '''# After pushing:
# 1. Wait for Render to deploy
# 2. Refresh the live app
# 3. Hard refresh if needed (Cmd + Shift + R)''',
        language="bash"
    )
    st.caption("Basic deploy/update flow for your live app.")

    st.divider()

    st.markdown("### Terminal Commands")
    st.code(
        '''streamlit run app.py''',
        language="bash"
    )
    st.caption("Run your app locally.")

    st.code(
        '''pip install -r requirements.txt''',
        language="bash"
    )
    st.caption("Install project dependencies.")

    st.code(
        '''git pull --rebase origin main''',
        language="bash"
    )
    st.caption("Pull latest changes cleanly before pushing.")

    st.divider()

    st.markdown("### Common Fixes")
    st.code(
        '''Duplicate element error
→ Add a unique key= to the Streamlit component''',
        language="text"
    )

    st.code(
        '''Git push rejected
→ Run git pull --rebase origin main
→ Then git push''',
        language="text"
    )

    st.code(
        '''Changes not showing live
→ Save file
→ git add / commit / push
→ Wait for Render deploy
→ Hard refresh browser''',
        language="text"
    )

    st.code(
        '''Local app works, live app doesn’t
→ Check if GitHub has the latest code
→ Confirm Render finished deploying''',
        language="text"
    )