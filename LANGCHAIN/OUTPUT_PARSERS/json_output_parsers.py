from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import JsonOutputParser


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

parser = JsonOutputParser()

template = PromptTemplate(
    template= 'Give me the name, age and city of a functional person {format_instructions}',
    input_variables=[],  
    partial_variables={'format_instructions' : parser.get_format_instructions()} 
    # with the help of partials variables we are telling we need in json format
)

# below three lines are without using chains

# prompt = template.format()


# result = model.invoke(prompt)

# final_result = parser.parse(result.content)

chain = template | model | parser

final_result = chain.invoke({})

print(final_result)

