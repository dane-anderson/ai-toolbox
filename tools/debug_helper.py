import streamlit as st

def run(client):
    st.title("🐞 Debug Helper")
    st.caption("Paste an error or broken code and get a clear explanation.")

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
Debug Input
</div>
""", unsafe_allow_html=True)

    user_input = st.text_area(
        "Paste your error or code:",
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

    if st.button("Analyze", use_container_width=True):
        if not user_input:
            st.warning("Please enter something first.")
        else:
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