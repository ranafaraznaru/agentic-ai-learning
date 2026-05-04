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
print(multiply.invoke({'a' : 2, 'b' : 3}))
  # --- Metadata Inspection ---                                                                                                                
print(f"Name: {multiply.name}")                                                                                      
print(f"Description: {multiply.description}")                       
print(f"Args: {multiply.args}")                                   
  # ---------------------------

# Tool Binding  

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

llm_with_tools = llm.bind_tools([multiply])
result = llm_with_tools.invoke([HumanMessage(content="What is the product of 2 and 3?")])
print("result",result)