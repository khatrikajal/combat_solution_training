import streamlit as st
from tools_setup import llm, calculator_tool
from router import route_query

st.title("DAG Workflow: Calculator + Mistral LLM (OpenRouter)")

user_input = st.text_area("Enter your query:", height=120)

if st.button("Run"):
    if not user_input.strip():
        st.warning("Please enter some text")
    else:
        route = route_query(user_input)

        if route == "calc":
            try:
                
                expression = user_input.strip()
                if not expression.startswith("print("):
                    expression = f"print({expression})"
                output = calculator_tool.run(expression)
            except Exception as e:
                output = f"Calculation error: {e}"

            st.markdown("### Calculator output:")
            st.write(output)

