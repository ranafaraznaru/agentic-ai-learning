from dotenv import load_dotenv
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI


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

question = "what is open route?"
retrieved_docs = retriever.invoke(question)
context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
# print('context_text',context_text)

final_prompt = prompt.invoke({"context":context_text, "question":question})
print('final_prompt',final_prompt)

#Step 4
#Generation
answer = llm.invoke(final_prompt)
print('answer',answer)
