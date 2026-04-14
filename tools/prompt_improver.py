import streamlit as st

def run(client):
    st.title("✨ Prompt Improver")
    st.caption("Turn rough ideas into clear, powerful AI prompts.")

    st.divider()

    st.markdown("""
<div style="
background-color: #0f172a;
padding: 15px 20px;
border-radius: 12px 12px 0 0;
border: 1px solid #1e293b;
border-bottom: none;
color: #eee;
font-weight: 600;
">
Prompt Input
</div>
""", unsafe_allow_html=True)

    prompt_input = st.text_area(
        "Paste your rough prompt or idea:",
        label_visibility="collapsed"
    )

    st.markdown("""
<div style="
height: 10px;
border: 1px solid #1e293b;
border-top: none;
border-radius: 0 0 12px 12px;
margin-top: -10px;
margin-bottom: 20px;
"></div>
""", unsafe_allow_html=True)

    if st.button("Improve Prompt", use_container_width=True):
        if not prompt_input:
            st.warning("Please enter something first.")
        else:
            with st.spinner("Improving your prompt..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"""
You are a prompt-writing assistant.

A user pasted this rough prompt or idea:
{prompt_input}

Rewrite it into a clearer, more effective AI prompt.

Make it:
1. Specific
2. Structured
3. Easy for an AI system to follow

Keep it practical and concise.
"""
                )

            result_text = str(response.output_text)

            st.divider()
            st.subheader("✨ Improved Prompt")

            st.markdown(
                f"""
<div style="background-color: #111; padding: 20px; border-radius: 10px; border: 1px solid #333; color: #eee; font-size: 15px;">
{result_text}
</div>
""",
                unsafe_allow_html=True,
            )