from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)


#first prompt > detailed report

template1 = PromptTemplate(
    template = 'write a detailed report on {topic}',
    input_variables=['topic']
)

#second prompt > summary

template2 = PromptTemplate(
    template = 'write a five lines summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser #  This is basically how pipelines are formed and chains looks like

result = chain.invoke({'topic' : 'attention is all you need'})

print(result)