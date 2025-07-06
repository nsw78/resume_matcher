import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Baixa o modelo uma vez e carrega localmente
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text: str) -> list:
    return model.encode(text)

def embed_resumes(resume_texts):
    embeddings = [get_embedding(text) for text in resume_texts]
    return np.array(embeddings)

def build_faiss_index(embeddings):
    dim = len(embeddings[0])
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings).astype("float32"))
    return index
