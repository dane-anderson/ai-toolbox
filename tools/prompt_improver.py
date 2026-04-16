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
            with st.spinner("Building production-ready plan..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"""
You are a senior software architect and product engineer.

A user wants to build this:
{prompt_input}

Turn it into a production-ready implementation plan.

Output in this exact structure:

1. Goal
- Briefly explain what is being built

2. Core Features
- Bullet list of must-have features

3. Tech Stack
- Recommend a practical stack
- Prefer Python / Streamlit / FastAPI / React only when appropriate

4. Architecture
- Explain the main parts of the system
- Mention frontend, backend, database, APIs, and background jobs if relevant

5. Edge Cases
- List important things that could break or be forgotten

6. Deployment
- Explain how this could be deployed
- Mention Render if appropriate

7. Build Steps
- Give a clear step-by-step build order

Keep it practical, concise, and builder-focused.
"""
                )

                result = response.output_text

                st.subheader("🏗 Production-Ready Plan")
                st.markdown(result)

    if starter_code:
        if not prompt_input:
            st.warning("Please enter something first.")
        else:
            with st.spinner("Generating starter code..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"""
You are a senior software engineer.

A user wants starter code for this idea:
{prompt_input}

Generate starter code that is practical and clean.

Rules:
- Default to Python unless another language is clearly better
- If this sounds like a UI tool or dashboard, prefer Streamlit
- If this sounds like an API, prefer FastAPI
- Keep the code minimal but usable
- Include comments where helpful
- Do not overbuild
- Return code only, with no explanation outside the code
"""
                )

                result = response.output_text

                st.subheader("💻 Starter Code")
                st.code(result, language="python")