from marvin import ai_classifier
from enum import Enum

@ai_classifier
class CustomerIntent(Enum):
    """Classifies the incoming users intent"""
    SALES = 1
    TECHNICAL_SUPPORT = 2
    BILLING_ACCOUNTS = 3
    PRODUCT_INFORMATION = 4
    RETURNS_REFUNDS = 5
    ORDER_STATUS = 6
    ACCOUNT_CANCELLATION = 7
    OPERATOR_CUSTOMER_SERVICE = 0

if __name__ == "__main__":
    print(CustomerIntent("hi I would like to ask some questions about recent billing"))