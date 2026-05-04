from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
import os

load_dotenv()

huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")


llm= HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task = "text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN")

)

model = ChatHuggingFace(llm=llm)

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





prompt1 = template1.invoke({'topic':'black hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text',result.content})

result1 = model.invoke(prompt2)

print(result1.content)