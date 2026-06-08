from langchain.prompts import PromptTemplate
from parser import parser

prompt_template = PromptTemplate(
    template="""
You are an intelligent expense classification assistant.

Your task is to classify an expense description.

Previous Conversation:
{history}

Rules:
1. Use only the text provided.
2. Do not assume missing information.
3. If the description is ambiguous, keep the category broad.
4. expense_type must be:
   - Essential
   - Non-Essential

{format_instructions}

Expense Description:
{expense}
""",
    input_variables=["expense", "history"],
    partial_variables={
        "format_instructions":
        parser.get_format_instructions()
    }
)