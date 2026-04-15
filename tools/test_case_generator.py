import streamlit as st

def run(client):
    st.title("🧪 Test Case Generator")
    st.caption("Generate smart test cases and edge cases for your code.")

    st.divider()

    # Styled input header
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

    user_input = st.text_area(
    "Paste your error or code:",
    label_visibility="collapsed",
    key="test_case_input"
    )   

    # Bottom border for input box
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

    if st.button("Generate Test Cases", use_container_width=True):
        if not user_input.strip():
            st.warning("Please enter some code first.")
        else:
            with st.spinner("Generating test cases..."):
                response = client.responses.create(
                    model="gpt-4.1-mini",
                    input=f"""
You are a software testing assistant.

A user pasted this code:
{user_input}

Generate practical test cases.

Include:
- Normal test cases
- Edge cases (boundaries, zero, negatives, large values)
- Failure cases (invalid inputs, errors if relevant)

For each test case:
- Show the input
- Show the expected output or behavior

Keep it concise and clean.
Format as bullet points.
"""
                )

            result_text = str(response.output_text)

            st.divider()
            st.subheader("🧠 Test Cases")

            st.markdown(
                f"""
<div style="
background-color: #111;
padding: 20px;
border-radius: 10px;
border: 1px solid #333;
color: #eee;
font-size: 15px;
line-height: 1.6;
">
{result_text}
</div>
""",
                unsafe_allow_html=True
            )