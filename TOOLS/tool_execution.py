from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
import requests
from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI


load_dotenv()


# Tool Create

@tool

def multiply(a:int, b:int) -> int : 
    """Given two numbers a and b this tool return their product""" # description
    return a * b
# print(multiply.invoke({'a' : 2, 'b' : 3}))
  # --- Metadata Inspection ---                                                                                                                
# print(f"Name: {multiply.name}")                                                                                      
# print(f"Description: {multiply.description}")                       
# print(f"Args: {multiply.args}")                                   
  # ---------------------------
query = HumanMessage("can you multiply 3 with 10")
messages=[query]
# Tool Binding  

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

llm_with_tools = llm.bind_tools([multiply])
result = llm_with_tools.invoke(messages)
messages.append(result)
# print('result',result)
tool_result = multiply.invoke(result.tool_calls[0])
messages.append(tool_result)
# print("tool_result",tool_result)
# print('messages',messages)
# LLM never calls the tool by itself instead it give the suggestion in response.
llmResponse = llm_with_tools.invoke(messages)
print('llmResponse',llmResponse.content)