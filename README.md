
### Local-ia - sem openai

````markdown
# 🤖 Resume Matcher com IA (LLM + Embeddings + FAISS)

Este projeto utiliza inteligência artificial para classificar automaticamente currículos com base na descrição de uma vaga. Ele compara o conteúdo dos currículos com a vaga informada usando embeddings de linguagem natural e busca vetorial com FAISS.

---

## 🔀 Versões do Projeto

Este repositório possui duas versões:

- [`main`](https://github.com/nsw78/resume_matcher/tree/main) → Usa a API da OpenAI (é necessário chave e plano)
- [`local-ia`](https://github.com/nsw78/resume_matcher/tree/local-ia) → Usa modelos open-source com `sentence-transformers` (totalmente offline e gratuito)

Você pode trocar de versão com:

```bash
git checkout local-ia
````

---

## 🚀 Funcionalidades

* 🧠 Geração de embeddings com modelo da OpenAI (`text-embedding-ada-002`) ou local
* 🔍 Busca vetorial com FAISS para encontrar os candidatos mais compatíveis
* 💡 Interface interativa com Streamlit
* 📂 Leitura de currículos em `.txt`
* ✅ Projeto simples, local, fácil de rodar e escalar

---

## 📁 Estrutura do Projeto

```plaintext
resume_matcher/
├── app.py                      # Aplicação principal (Streamlit)
├── utils.py                    # Funções auxiliares (embeddings e FAISS)
├── requirements.txt            # Dependências do projeto
├── .env                        # Chave da OpenAI (não subir para o GitHub)
├── data/
│   ├── job_description.txt     # Descrição da vaga
│   └── resumes/
│       ├── resume1.txt         # Currículo 1
│       └── resume2.txt         # Currículo 2
├── embeddings/                 # Diretório para salvar FAISS index (opcional)
```

---

## ⚙️ Pré-requisitos

* Python 3.8+
* Conta na [OpenAI](https://platform.openai.com/) com chave de API (apenas para a branch `main`)
* Git (para versionamento)

---

## 🛠️ Passo a passo para rodar localmente

### 1. Clone o repositório

```bash
git clone https://github.com/nsw78/resume_matcher.git
cd resume_matcher
```

### 2. Crie e ative o ambiente virtual

Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. (Opcional) Crie o arquivo `.env` com sua chave da OpenAI

Na raiz do projeto, crie um arquivo `.env` com o seguinte conteúdo:

```
OPENAI_API_KEY=sk-...sua-chave-aqui...
```

> ⚠️ **Nunca suba sua chave para o GitHub!** Certifique-se de que o arquivo `.env` esteja no `.gitignore`.

---

## 🧪 Como usar

1. Edite `data/job_description.txt` com a descrição da vaga desejada.
2. Coloque arquivos `.txt` dos currículos em `data/resumes/`.
3. Execute o app com o Streamlit:

```bash
streamlit run app.py
```

4. Acesse no navegador: [http://localhost:8501](http://localhost:8501)

---

## 🧩 Extensões possíveis

* Suporte a arquivos PDF com `pdfplumber`
* Suporte a múltiplas vagas e filtros por cargo
* Integração com banco de dados (PostgreSQL, SQLite, etc.)
* Deploy na nuvem (Streamlit Cloud, Hugging Face Spaces, Render, etc.)

---

## 📌 Exemplo de aplicação

A IA irá analisar a compatibilidade dos currículos com a vaga e mostrar os candidatos mais próximos da descrição, com base em **similaridade semântica**.

---

## 🧠 Tecnologias utilizadas

* [Python](https://www.python.org/)
* [Streamlit](https://streamlit.io/)
* [OpenAI API](https://platform.openai.com/) (ou `sentence-transformers`)
* [FAISS](https://github.com/facebookresearch/faiss)
* [dotenv](https://pypi.org/project/python-dotenv/)

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/sua-feature`)
3. Commit suas alterações (`git commit -m 'Adiciona nova feature'`)
4. Push para a branch (`git push origin feature/sua-feature`)
5. Abra um Pull Request

---

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

---

## ✨ Autor

Feito com ❤️ por [Nelson Walcow](https://github.com/nsw78)

´´