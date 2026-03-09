# we use ChatPromptTemplate to create multiple dynamic chat prompt

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate



load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
model = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)

chat_template = ChatPromptTemplate([
    SystemMessage (content ='You are a helpful {domain} expert'),
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain the simple terms, what is {topic}'),
])

prompt = chat_template.invoke({"domain" : "cricket", "topic" : "dusra"})


print (prompt)
