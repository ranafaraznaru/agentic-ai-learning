from dotenv import load_dotenv
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser


load_dotenv()



GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
SERPAPI_API_KEY = os.getenv("SERPAPI_API_KEY")

# STEP 1
# Docuement loader
video_id = "fjd2hm6-qtMh" # only the ID, not full URL

params = {
    "api_key":  SERPAPI_API_KEY,
    "engine" : "youtube_video_transcript",
    "v" : video_id,
    "type" :"asr"
}

search = requests.get("https://serpapi.com/search",params=params)
response =search.json()
# print('response',response)

try:
    # If you don't care which language, this returns the "best" one
    # transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript_list = response["transcript"]
    

    # Flatten it to plain text
    # transcript = " ".join(chunk["text"] for chunk in transcript_list)
    transcript = " ".join(item["snippet"] for item in transcript_list)
    # print(transcript,'transcript')

except TranscriptsDisabled:
    print("No captions available for this video.")

# Indexing 
# Text Splitting 
splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=0)
chunks = splitter.create_documents([transcript])
print(len(chunks))
# print(chunks[1].page_content)

# Embedding Generation and Storing in Vector Store

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vector_store = FAISS.from_documents(chunks, embeddings)
vector_store.index_to_docstore_id


# STEP 2
#Retrieval
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})
# result = retriever.invoke('what is open route?')
# print('result',result)

# STEP 3
# Augmentation

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GOOGLE_API_KEY
)

prompt = PromptTemplate(
    template= """
    you are a helpful assistant.
    Answer ONLY from the provided transcript context.
    If the context is insufficient, just say you dont know.

    {context}
    Question: {question}
    """,
    input_variables=["context", "question"]
)

question = "what is open router?"
retrieved_docs = retriever.invoke(question)
def format_docs(retrieved_docs):
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    return context_text

parallel_chain = RunnableParallel({
    'context' : retriever | RunnableLambda(format_docs), # Retrieving the docuement from store and then using format_docs to get only context text, with the help of runnable parallel its easy for using for chains
    'question' : RunnablePassthrough()
})
result = parallel_chain.invoke(question)
# print('result',result)
parser = StrOutputParser()
main_chain = parallel_chain | prompt | llm | parser
answer = main_chain.invoke(question)
print('answer',answer) 