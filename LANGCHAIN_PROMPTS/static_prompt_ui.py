from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
import os


load_dotenv()
 
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")
model = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)


st.header('research tool')

user_input = st.text_input('enter your prompt')

if st.button('Summarize'):
    result = model.invoke(user_input)
    st.write(result.content)