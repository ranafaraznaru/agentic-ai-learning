from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

url = 'https://www.apple.com/macbook-pro/'
load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")


model= ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)

prompt = PromptTemplate(
    template= 'Answer the following question \n {question} about {text}',
    input_variables=['question', 'text']
)

parser = StrOutputParser()



loader = WebBaseLoader(url)

docs = loader.load()

# print(docs)
print(docs[0].page_content)

chain = prompt | model | parser

result = chain.invoke({'question':'which product is not listed','text' : docs[0].page_content})
print('result',result)