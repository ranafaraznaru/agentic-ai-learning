import json
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
import requests
from langchain_openai import ChatOpenAI
from langchain_core.tools import InjectedToolArg
from typing import Annotated


load_dotenv()
EXCHANGE_RATE_API_KEY = os.getenv("EXCHANGE_RATE_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")


# llm = ChatGoogleGenerativeAI(
#     model="gemini-2.5-flash",
#     google_api_key=GOOGLE_API_KEY
# )
llm = ChatOpenAI(
      api_key=DEEPSEEK_API_KEY,
      base_url="https://api.deepseek.com",
      model="deepseek-chat",
)

# Tool Create

@tool

def get_currency_conversion(base_currency:str, target_currency:str) -> float : 
    """This function fetches the currency conversion factor between a given base currency and a target currency""" # description
    url = f"https://v6.exchangerate-api.com/v6/{EXCHANGE_RATE_API_KEY}/pair/{base_currency}/{target_currency}"

    response = requests.get(url)
    return response.json()
result = get_currency_conversion.invoke({"base_currency": "USD", "target_currency": "PKR"})

import json
# print(json.dumps(result, indent=2))


@tool

#Injection Strategy:

#Incorrect: "LLM, do not try to fill this argument."

#Correct: "I (the developer/runtime) will inject this value after running earlier tools."

def convert(base_currency:int, conversion_rate: Annotated[float,InjectedToolArg]) -> float :  
    """Given a currency conversion rate this function calculates the target currency value from a given base currency value""" # description

    return base_currency * conversion_rate
currencyResult = convert.invoke({"base_currency": 10, "conversion_rate": 279.0})
# print('currencyResult',currencyResult)

# Tool Binding

llm_with_tools = llm.bind_tools([get_currency_conversion,convert])
messages = [HumanMessage('What is the conversion factor between usd and pkr, and based on that can you convert 10 usd to pkr')]

aiMessage = llm_with_tools.invoke(messages)
messages.append(aiMessage)
# print('aiMessage',aiMessage.tool_calls)
# print(json.dumps(aiMessage.model_dump(), indent=2, default=str))

for tool_call in aiMessage.tool_calls:
    # execute the 1st tool and get the value of conversion rate
    if tool_call['name'] == 'get_currency_conversion':
       tool_message1 = get_currency_conversion.invoke(tool_call)
    # Fetch the conversion rate
    conversion_rate = ('tool_message1.content',json.loads(tool_message1.content)['conversion_rate'])
    # Append this tool message to messages list  
    messages.append(tool_message1) 
    # execute the 2nd tool using the conversion rate from tool 1
    if tool_call['name'] == 'convert':
    # fetch the correct arguement 
       tool_call['args']['conversion_rate'] = conversion_rate
       tool_message2 = convert.invoke(tool_call)
       messages.append(tool_message2) 

# print('messages',messages)


llmResponse = llm_with_tools.invoke(messages)
print('llmResponse',llmResponse.content)