
import os
from dotenv import load_dotenv

from langsmith import traceable  # any function which we want to trace by langsmith simply we will use @traceable decorator on the top of it because by default langsmith trace only chains and runnables

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq




load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
HUGGINGFACE_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ['LANGCHAIN_PROJECT'] = 'RAG Chatbot'


# Set HF token if available (improves download speed/rate limits)
if HUGGINGFACE_API_TOKEN:
    os.environ["HF_TOKEN"] = HUGGINGFACE_API_TOKEN

PDF_PATH = "islr.pdf"  # change to your file

# ---------- traced setup steps ----------
@traceable(name="load_pdf") # @traceable are called decorators
def load_pdf(path: str):
    loader = PyPDFLoader(path)
    return loader.load()  # list[Document]

@traceable(name="split_documents")
def split_documents(docs, chunk_size=1000, chunk_overlap=150):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )
    return splitter.split_documents(docs)

@traceable(name="build_vectorstore", tags=['embedding', 'vectorstore'], metadata={'embedding-model': 'all-MiniLM-L6-v2'})
def build_vectorstore(splits):
    # HuggingFace embeddings - using local model
    emb = HuggingFaceEmbeddings(
        model_name="all-MiniLM-L6-v2"
    )
    # FAISS.from_documents internally calls the embedding model:
    vs = FAISS.from_documents(splits, emb)
    return vs

# You can also trace a “setup” umbrella span if you want:
@traceable(name="setup_pipeline")
def setup_pipeline(pdf_path: str):
    docs = load_pdf(pdf_path)
    splits = split_documents(docs)
    vs = build_vectorstore(splits)
    return vs

# ---------- pipeline ----------
llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)

prompt = ChatPromptTemplate.from_messages([
    ("system", "Answer ONLY from the provided context. If not found, say you don't know."),
    ("human", "Question: {question}\n\nContext:\n{context}")
])

def format_docs(docs):
    return "\n\n".join(d.page_content for d in docs)

# Build the index under traced setup
vectorstore = setup_pipeline(PDF_PATH)
retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 4})

parallel = RunnableParallel({
    "context": retriever | RunnableLambda(format_docs),
    "question": RunnablePassthrough(),
})

chain = parallel | prompt | llm | StrOutputParser()

# ---------- run a query (also traced) ----------
print("PDF RAG ready. Ask a question (or Ctrl+C to exit).")
q = input("\nQ: ").strip()

# Give the visible run name + tags/metadata so it’s easy to find:
config = {
    "run_name": "pdf_rag_query"
}

ans = chain.invoke(q, config=config)
print("\nA:", ans)
