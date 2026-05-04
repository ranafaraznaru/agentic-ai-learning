# Below we did semantic search
# from langchain_openai import OpenAIEmbeddings
from sentence_transformers import SentenceTransformer
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import os


load_dotenv()

# DEESEEK_KEY = os.getenv("DEEP_SEEK_API_KEY")
model = SentenceTransformer('all-MiniLM-L6-v2')



# embedding = OpenAIEmbeddings(model = 'text-embedding-ada-002', dimensions=300)

paragraphs = [
    "The advancement of artificial intelligence has revolutionized how we interact with technology, moving from simple rule-based systems to complex neural networks that can process natural language with remarkable fluency.",
    "Deep-sea exploration remains one of the final frontiers on Earth, as scientists utilize advanced submersibles to study unique ecosystems that thrive in complete darkness near hydrothermal vents.",
    "Sustainable urban planning focuses on creating walkable cities with efficient public transit systems and green spaces, aiming to reduce carbon footprints while improving the quality of life for residents.",
    "The history of ancient civilizations often reveals sophisticated engineering feats, such as the construction of the Great Pyramids or the intricate irrigation systems developed by the Indus Valley people.",
    "Modern culinary arts blend traditional techniques with molecular gastronomy, allowing chefs to experiment with textures and temperatures to create innovative dining experiences that engage all the senses."
]

query = 'artificial intelligence'
# doc_embeddings = embedding.embed_documents(paragraphs)
# query_embeddings = embedding.embed_query(query)
doc_embeddings = model.encode(paragraphs)
query_embeddings = model.encode([query])

# scores = cosine_similarity([query_embeddings],doc_embeddings)[0]
scores = cosine_similarity(query_embeddings, doc_embeddings)[0]
index, score =(sorted(list(enumerate(scores)),key= lambda x:x[1])[-1])

print(query)
print(paragraphs[index])
print("similarity score is:",score)