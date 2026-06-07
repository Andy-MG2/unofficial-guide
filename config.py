import os
from dotenv import load_dotenv

#loads environment variable
load_dotenv()

# LLM
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
LLM_MODEL = "llama-3.3-70b-versatile"

# Documents
DOCS_PATH = "./rmp_data"

# Embeddings
EMBEDDING_MODEL = "all-MiniLM-L6-v2"

# Vector store 
CHROMA_COLLECTION = "professor_reviews"
CHROMA_PATH = "./chroma_db"

#Retrieval 
N_RESULTS = 5