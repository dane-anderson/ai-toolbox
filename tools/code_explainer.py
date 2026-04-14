import streamlit as st

def run(client):
    st.title("💻 Code Explainer")
    st.caption("Understand what your code does, step-by-step.")

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
Code Input
</div>
""", unsafe_allow_html=True)

    code_input = st.text_area(
        "Paste your code:",
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

    if st.button("Explain Code", use_container_width=True):
        if not code_input:
            st.warning("Please enter something first.")
        else:
            with st.spinner("Explaining your code..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"""
You are a helpful coding assistant.

A user pasted the following code:
{code_input}

Explain:
1. What this code does
2. How it works step-by-step
3. Any important concepts used

Be clear and beginner-friendly.
"""
                )

            result_text = str(response.output_text)

            st.divider()
            st.subheader("🧠 Result")

            st.markdown(
                f"""
<div style="background-color: #111; padding: 20px; border-radius: 10px; border: 1px solid #333; color: #eee; font-size: 15px;">
{result_text}
</div>
""",
                unsafe_allow_html=True,
            )