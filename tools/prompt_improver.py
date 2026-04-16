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

    col1, col2, col3 = st.columns(3)

    with col1:
        improve = st.button("Improve Prompt")

    with col2:
        production = st.button("Make Production Ready")

    with col3:
        starter_code = st.button("Generate Starter Code")

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

    if improve:
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
3. Easy for an AI model to follow
4. Optimized for a high-quality output

Keep it concise and practical.
"""
                )

                result = response.output_text

                st.subheader("✨ Improved Prompt")
                st.code(result, language="markdown")

    if production:
        if not prompt_input:
            st.warning("Please enter something first.")
        else:
            st.subheader("🏗 Production-Ready Plan")
            st.write("Coming next: system design + architecture output.")

    if starter_code:
        if not prompt_input:
            st.warning("Please enter something first.")
        else:
            st.subheader("💻 Starter Code")
            st.code("# Starter code will appear here", language="python")