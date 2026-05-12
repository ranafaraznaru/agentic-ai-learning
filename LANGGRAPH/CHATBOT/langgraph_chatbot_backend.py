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
from langchain_core.messages import HumanMessage


load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")

model = ChatGoogleGenerativeAI(
    # model="gemini-2.5-flash",
    model="gemini-2.5-flash-lite",
    google_api_key=GOOGLE_API_KEY
)

class ChatState (TypedDict):

    messages: Annotated[list[BaseMessage], add_messages] # To append messages into list its recommended to use add_messages from langgraph instead of operator.add


def chat_node(state: ChatState): 

    # take user query from state
    messages = state['messages']

    # send to llm
    response = model.invoke(messages)

    # response store to state
    return {'messages' : [response]}


conn = sqlite3.connect(database='chatbot.db', check_same_thread=False)  # check_same_thread means we will use same database in different threads
checkpointer = SqliteSaver(conn=conn)
graph = StateGraph(ChatState)

# add nodes
graph.add_node('chat_node', chat_node)
graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)
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