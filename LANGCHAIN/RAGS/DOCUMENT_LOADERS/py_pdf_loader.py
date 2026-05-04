from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")


model= ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)

prompt = PromptTemplate(
    template= 'Write a detailed report on {topic}',
    input_variables=['topic']
)

parser = StrOutputParser()



loader = PyPDFLoader('file-example.pdf')

docs = loader.load()

# print(docs)
print(docs[0].page_content)
print(docs[1].metadata)