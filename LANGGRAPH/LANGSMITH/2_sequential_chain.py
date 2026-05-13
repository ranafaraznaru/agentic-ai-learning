from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq


import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ['LANGCHAIN_PROJECT'] = 'Sequential App'

prompt1 = PromptTemplate(
    template='Generate a detailed report on {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a 5 pointer summary from the following text \n {text}',
    input_variables=['text']
)

model = ChatGoogleGenerativeAI(
    # model="gemini-2.5-flash",
    model="gemini-2.5-flash-lite",
    google_api_key=GOOGLE_API_KEY
)
model2 = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
parser = StrOutputParser()

chain = prompt1 | model | parser | prompt2 | model2 | parser

config = {
    'run_name' : 'sequential chain',
    "tags" : ['llm app', 'report generation', 'summarization'],
    'metadata' : {'model1' :'gemini-2.5-flash', 'model2' : 'llama-3.3-70b-versatile', 'parser' : 'StrOutputParser'} 
}

result = chain.invoke({'topic': 'Unemployment due to AI in software engineeing'}, config=config)

print(result)
