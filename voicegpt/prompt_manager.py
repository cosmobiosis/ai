from marvin.prompts.library import System, User, ChainOfThought
from marvin.engine.language_models import chat_llm
from typing import Optional
import asyncio
import random
from marvin import AIApplication
from marvin.tools import tool
from marvin import ai_fn

# class ExpertSystem(System):
#     content: str = (
#         "You are a world-class expert on {{ topic }}. "
#         "When asked questions about {{ topic }}, you answer correctly. "
#         "You only answer questions about {{ topic }}. "
#     )
#     topic: Optional[str]

# class CustomerSupport(System):
#     content: str = (
#         "When you give a sentence, you modulate your response that rephrases "
#         "the sentence in a more natural, sincere and detailed way as a customer support. "
#         "Your customer's name is {{ name }}. "
#     )
#     name: str = "not provided"

# model = chat_llm()

# def llm_rephrase(user_name: str, user_paragraph: str):
#     prompt = ( ExpertSystem()
#                 | CustomerSupport()
#                 | User(user_paragraph)
#                 | ChainOfThought())
    
#     print(prompt.dict(topic="rephrase"))
#     # return response.content

@ai_fn
def rephrase_as_customer_support(original_sentence: str) -> str:
    """Generates rephrased sentence with a more detailed, natural and profesional way 
    as an expert of customer support, based on the input of original sentence.
    Parameters include the original sentence ('original_sentence').
    """

if __name__ == "__main__":
    result = rephrase_as_customer_support("Sorry, would you like a refund?")
    print(result) 