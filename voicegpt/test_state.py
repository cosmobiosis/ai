from datetime import datetime
from pydantic import BaseModel
from marvin import AIApplication

class CustomerSupportAbstractState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str
    description: str
    in_current_state: bool

class CustomerSupportInitialState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str =  "Asking"
    description: str = "Asking for service"
    in_current_state: bool = False

class CustomerSupportRefundState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str = "Refund"
    description: str = "Refund only after user wants to ask for service"
    in_current_state: bool = False

class CustomerSupportStatesGraph(BaseModel):
    states: list[CustomerSupportAbstractState] = [CustomerSupportInitialState(), CustomerSupportRefundState()]

todo_app = AIApplication(
    state=CustomerSupportStatesGraph(),
    description=(
        "A simple customer service. Users will give instructions to perform state transition between"
        "different customer support states"
    ),
)

response = todo_app("I want to ask for refund")
print(response.content)
print(todo_app.state)