from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda 
# runnable branch helps to execute branch on the basis of if else
# runnable lambda convert a lambda function to runnable and then we can use it as a chain
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field 
from typing import Literal


load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)



parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(description="Give the sentiment of the feedback")

parser2 = PydanticOutputParser(pydantic_object= Feedback)

prompt1 = PromptTemplate(
    template = 'Classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instructions}',
    input_variables=['feedback'],
    partial_variables= {'format_instructions' : parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template = 'write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback'],
)

prompt3 = PromptTemplate(
    template = 'write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback'],
)




branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "negative", prompt3 | model | parser),
    RunnableLambda(lambda x: 'could not fiund sentiment')
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback' : 'This is a wonderful phone'})

print(result)

chain.get_graph().print_ascii()