from langgraph.graph import StateGraph, START, END
from typing import TypedDict,Annotated
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langgraph.graph.message import add_messages
from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3
from langchain_groq import ChatGroq


from langgraph.prebuilt import ToolNode, tools_condition
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool

import requests
import json

os.environ["LANGCHAIN_PROJECT"] = "LangGraph Chatbot"
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
ALPHA_VANTAGE_API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")


model = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)


# Tools 
search_tool = DuckDuckGoSearchRun(region ='us-en')

@tool
def calculator(first_num: float, second_num:float, operation:str) -> dict:
    """
    Perform a basic arithmetic operation on two numbers.
    Supported operations: add, sub, mul, div
    """
    try:
        if operation == 'add':
            result = first_num + second_num
        elif operation == 'sub':
            result = first_num - second_num
        elif operation == 'mul':
            result = first_num * second_num
        elif operation == 'div':
            if second_num == 0:
                return json.dumps({"error": "Division by zero is not allowed"})
            result = first_num / second_num
        else:
            return json.dumps({"error": f"Unsupported operation: {operation}"})
        return json.dumps({"first_num": first_num, "second_num": second_num, "operation" : operation, "result" : result})
    except Exception as e:
        return json.dumps({"error": str(e)})
            
@tool 
def get_stock_price(symbol: str) -> dict:
    """
    Fetch latest stock price for a given symbol (e.g. 'AAPL', 'TSLA')
    using alpha vantage with api key in the URL.
    """
    url = f"https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={symbol}&apikey={ALPHA_VANTAGE_API_KEY}"
    r = requests.get(url)
    return json.dumps(r.json())


# make tool list
tools = [get_stock_price,search_tool,calculator]

# Make the LLm tool-aware
llm_with_tools = model.bind_tools(tools)


class ChatState (TypedDict):

    messages: Annotated[list[BaseMessage], add_messages] # To append messages into list its recommended to use add_messages from langgraph instead of operator.add


# def chat_node(state: ChatState): 

#     # take user query from state
#     messages = state['messages']

#     # send to llm
#     response = model.invoke(messages)

#     # response store to state
#     return {'messages' : [response]}

# graph nodes
def chat_node(state: ChatState):
    """
    LLM node that may answer or request a tool call.
    """
    messages = state['messages']
    response = llm_with_tools.invoke(messages)
    return {"messages" : [response]}
tool_node = ToolNode(tools) # Executes tool calls


conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)  # check_same_thread means we will use same database in different threads
checkpointer = SqliteSaver(conn=conn)
graph = StateGraph(ChatState)
# add nodes
graph.add_node("chat_node", chat_node)
graph.add_node("tools", tool_node)

graph.add_edge(START, "chat_node")

# if the LLM asked for a tool, go to ToolNode; else function
graph.add_conditional_edges('chat_node', tools_condition)

graph.add_edge('tools', 'chat_node')
chatbot = graph.compile(checkpointer=checkpointer)

def retrieve_all_threads():

    all_threads = set()

    for checkpoint in checkpointer.list(None): # None means return all threads
         all_threads.add(checkpoint.config['configurable']['thread_id'])

    return list(all_threads)




# thread_id = '1'
# while True:
#     user_message = input('Type here: ')

#     print('User:', user_message)

#     if user_message.strip().lower() in ['exit','quit','bye']:
#         break

#     config= {'configurable': {'thread_id': thread_id}}
#     response = chatbot.invoke({'messages': [HumanMessage(content=user_message)]}, config=config)

#     print('AI :', response['messages'][-1].content)