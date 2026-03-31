from langchain_community.document_loaders import TextLoader
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



loader = TextLoader('dollar.txt', encoding= 'utf-8')

docs = loader.load()

# print(docs)
# print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'topic' : docs[0].page_content})
print('result',result)