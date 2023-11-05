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

class CustomerSupportInitialState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str =  "Asking"
    description: str = "Asking for service"

class CustomerSupportRefundState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str = "Refund"
    description: str = "Refund only after user wants to ask for service"

class CustomerSupportGetRefundReceiptState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str = "Get Refund Receipt"
    description: str = "Can only get refund receipt after user refunds. Otherwise rejects user's requirements."

class CustomerSupportRejectState(BaseModel):
    # title: str = Field(
    #     default_factory=str,
    #     description="Initial State.",
    # )
    title: str = "reject user's requirement"
    description: str = "When user's requirement gets rejected, changes the system to this state"
    
class CustomerSupportStatesGraph(BaseModel):
    states: list[CustomerSupportAbstractState] = [
        CustomerSupportInitialState(), 
        CustomerSupportRefundState(),
        CustomerSupportGetRefundReceiptState(),
        CustomerSupportRejectState()
    ]

todo_app = AIApplication(
    state=CustomerSupportStatesGraph(),
    description=(
        "A simple customer service. Users will give instructions to perform state transition between"
        "different customer support states."
    ),
)

response = todo_app("I want to fuck ass")
# response = todo_app("I want to ask for a receipt of my refund")
print(response.content)