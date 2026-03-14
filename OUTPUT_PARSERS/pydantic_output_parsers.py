from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
import os
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser



load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")



model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)


class Person(BaseModel):
    name : str = Field(description= 'The name of the person')
    age : int = Field(description= 'The age of the person')
    city : str = Field(description= 'Name of the city the person belongs to')

parser = PydanticOutputParser(pydantic_object= Person)

template = PromptTemplate (
    template = 'Generate the name, age and city of a fictional {place} person \n {format_instructions}',
    input_variables=['place'],
    partial_variables= {'format_instructions' : parser.get_format_instructions()}
)

# below without chains

# prompt = template.invoke({'place':'pakistan'})

# result = model.invoke(prompt)

# final_result =  (parser.parse(result.content))

# with chains

chains = template | model | parser

final_result = chains.invoke({'place':'pakistan'})

print(final_result)



