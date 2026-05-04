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



template1 = PromptTemplate(
    template = 'Generate 5 interesting facts about {topic}',
    input_variables=['topic']
)


parser = StrOutputParser()

chain = template1 | model | parser 

result = chain.invoke({'topic' : 'cricket'})

print(result)

chain.get_graph().print_ascii()