from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os


load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
model = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)

chat_history =[]

while True:
    user_input = input('you: ')
    chat_history.append({'role':'user','message':user_input})
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ", chat_history)    

print("Fine: ", result.content)    