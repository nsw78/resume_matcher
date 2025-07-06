import os
import streamlit as st
from utils import embed_resumes, build_faiss_index

def load_resumes(path):
    resumes = []
    filenames = []
    for filename in os.listdir(path):
        if filename.endswith(".txt"):
            with open(os.path.join(path, filename), "r", encoding="utf-8") as f:
                resumes.append(f.read())
                filenames.append(filename)
    return resumes, filenames

def main():
    st.title("🧠 Resume Matcher (IA Local)")

    resumes, filenames = load_resumes("data/resumes")
    resume_embeddings = embed_resumes(resumes)
    index = build_faiss_index(resume_embeddings)

    st.success(f"{len(resumes)} currículos carregados.")

    query = st.text_area("📝 Cole aqui a descrição da vaga", height=200)

    if query:
        query_embedding = embed_resumes([query])
        D, I = index.search(query_embedding.astype("float32"), k=3)

        st.subheader("🔍 Melhores currículos encontrados:")
        for rank, i in enumerate(I[0]):
            st.markdown(f"**#{rank+1}: {filenames[i]}**")
            st.code(resumes[i][:1500] + "...", language="text")  # Mostra o início do currículo

if __name__ == "__main__":
    main()
