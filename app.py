import streamlit as st

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

st.set_page_config(page_title="Real Estate RAG", page_icon="🏠")

st.title("🏠 Real Estate RAG Chatbot")

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_store = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

question = st.text_input("Ask about a property")

if st.button("Search"):

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a Real Estate Assistant.

Use only the information below.

Property Information:
{context}

Question:
{question}

Answer:
"""

    response = llm.invoke(prompt)

    st.subheader("Answer")
    st.write(response.content)