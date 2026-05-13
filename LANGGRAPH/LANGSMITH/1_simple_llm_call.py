from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
import os

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Simple one-line prompt
prompt = PromptTemplate.from_template("{question}")

model = ChatGoogleGenerativeAI(
    # model="gemini-2.5-flash",
    model="gemini-2.5-flash-lite",
    google_api_key=GOOGLE_API_KEY
)
parser = StrOutputParser()

# Chain: prompt → model → parser
chain = prompt | model | parser

# Run it
result = chain.invoke({"question": "What is the capital of Pakistan?"})
print(result)
