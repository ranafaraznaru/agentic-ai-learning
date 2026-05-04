from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.output_parsers import StructuredOutputParser, ResponseSchema


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

schema =  [
ResponseSchema(name = 'fact_1', description = 'Fact 1 about the topic'),
ResponseSchema(name = 'fact_2', description = 'Fact 2 about the topic'),
ResponseSchema(name = 'fact_3', description = 'Fact 3 about the topic')

]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template = 'Give 3 fact about {topic} \n {format_instructions}',    
    input_variables=['topic'],
    partial_variables={'format_instructions' : parser.get_format_instructions()}
)

# prompt = template.invoke({'topic':'black hole'})

# result = model.invoke(prompt)

# final_result = parser.parse(result.content) # when using chain then no need to send .content

chain = template | model | parser

result = chain.invoke({'topic':"black hole"})

print(result)