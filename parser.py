from pydantic import BaseModel, Field
from langchain.output_parsers import PydanticOutputParser


class ExpenseOutput(BaseModel):

    expense_category: str = Field(
        description="Category of the expense"
    )

    expense_type: str = Field(
        description="Essential or Non-Essential"
    )

    confidence_note: str = Field(
        description="Reason for classification"
    )


parser = PydanticOutputParser(
    pydantic_object=ExpenseOutput
)
