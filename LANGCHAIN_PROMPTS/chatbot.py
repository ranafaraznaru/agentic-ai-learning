from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from langchain_core.messages import SystemMessage,HumanMessage,AIMessage



load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
model = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)

chat_history =[SystemMessage (content ='You are a helpful assistant')]

while True:
    user_input = input('you: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content = result.content))
    print("AI: ", result.content)    

print("Fine: ", chat_history)    