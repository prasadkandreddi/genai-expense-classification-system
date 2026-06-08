import streamlit as st

from model import llm
from parser import parser
from memory import memory
from prompt import prompt_template

st.set_page_config(
    page_title="Expense Classifier",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Generative AI Expense Classification System")

expense = st.text_input(
    "Enter Expense Description",
    placeholder="Example: Paid monthly electricity bill"
)

if st.button("Classify Expense"):

    if not expense.strip():

        st.warning(
            "Please enter an expense description."
        )

    else:

        try:

            history = memory.load_memory_variables(
                {}
            )["history"]

            prompt = prompt_template.format(
                expense=expense,
                history=history
            )

            response = llm.invoke(
                prompt
            )

            result = parser.parse(
                response.content
            )

            memory.save_context(
                {"expense": expense},
                {"result": str(result)}
            )

            st.success(
                "Classification Complete"
            )

            st.json(
                result.model_dump()
            )

            with st.expander(
                "Conversation Memory"
            ):

                st.text(
                    memory.load_memory_variables(
                        {}
                    )["history"]
                )

        except Exception as e:

            st.error(
                f"Error: {e}"
            )