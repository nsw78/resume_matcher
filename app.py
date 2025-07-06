import os
import streamlit as st
from utils import get_embedding, embed_resumes, build_faiss_index
import numpy as np
import faiss

# Carregar currículos
resume_dir = "data/resumes"
resumes = []
resume_names = []
for fname in os.listdir(resume_dir):
    with open(os.path.join(resume_dir, fname), "r", encoding="utf-8") as f:
        resumes.append(f.read())
        resume_names.append(fname)

# Carregar descrição da vaga
with open("data/job_description.txt", "r", encoding="utf-8") as f:
    job_description = f.read()

# Embeddings
st.title("🔍 Classificador de Currículos com IA")
st.write("Comparando candidatos com a descrição da vaga...")

resume_embeddings = embed_resumes(resumes)
index = build_faiss_index(resume_embeddings)

# Embed da vaga
job_embedding = get_embedding(job_description)
job_embedding = np.array([job_embedding]).astype("float32")

# Busca por similaridade
k = min(5, len(resumes))
distances, indices = index.search(job_embedding, k)

# Resultados
st.subheader("🔝 Candidatos mais compatíveis:")
for i, idx in enumerate(indices[0]):
    st.markdown(f"**{i+1}. {resume_names[idx]}** - Similaridade: {round(1 - distances[0][i], 2)}")
    st.code(resumes[idx], language="text")
