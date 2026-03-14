from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
# from langchain.schema.runnable import RunnableParallel
from langchain_core.runnables import RunnableParallel

# runnables helps to execute multiple chains parallelly 



load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEP_SEEK_API_KEY")

model1 = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

model2 = ChatOpenAI(
    api_key=DEEPSEEK_API_KEY,
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    temperature=0.7
)



prompt1 = PromptTemplate(
    template = 'Generate the simple and short notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template = 'Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document \n notes ->  {notes} and quiz',
    input_variables=['notes', 'quiz']
)


parser = StrOutputParser()

parallel_chain = RunnableParallel({'notes': prompt1 | model1 | parser, 'quiz': prompt2 | model2 | parser})

merge_chain = prompt3 | model2 | parser

chain = parallel_chain | merge_chain


result = chain.invoke({'text' : 'The quick brown fox jumps over the lazy dog.'})

print(result)

chain.get_graph().print_ascii()