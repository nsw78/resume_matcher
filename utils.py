import os
import faiss
import numpy as np
import openai
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text: str, model="text-embedding-ada-002") -> list:
    response = openai.Embedding.create(input=[text], model=model)
    return response["data"][0]["embedding"]

def embed_resumes(resume_texts):
    embeddings = [get_embedding(text) for text in resume_texts]
    return np.array(embeddings)

def build_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index
