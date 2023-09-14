from marvin import ai_classifier
from enum import Enum
from flytekit import task, workflow

@ai_classifier
class CustomerIntent(Enum):
    """Classifies the incoming users intent"""
    SALES = 1
    TECHNICAL_SUPPORT = 2
    BILLING = 3
    PRODUCT_INFORMATION = 4
    RETURNS_REFUNDS = 5
    ORDER_STATUS = 6
    ACCOUNT_CANCELLATION = 7
    OPERATOR_CUSTOMER_SERVICE = 0
    NOT_RELEVANT = 8

@task
def get_response_text(prompt: str) -> str:
    # print(prompt)
    intentEnum = CustomerIntent(prompt)
    # print(intentEnum)
    if intentEnum == CustomerIntent.BILLING:
        return "Would you like a refund?"
    return "Sorry. I don't know what you are talking about you sick fuck."

# if __name__ == "__main__":
#     print(get_response_text("I cannot wait to jerk off and fuck"))