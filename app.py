import os
from dotenv import load_dotenv
import streamlit as st

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Read API Key
google_api_key = os.getenv("GOOGLE_API_KEY")

# Streamlit Page
st.set_page_config(
    page_title="🏠 Real Estate RAG",
    page_icon="🏠"
)

st.title("🏠 Real Estate RAG Chatbot")

# Load Embedding Model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load Vector Database
vector_store = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

# Load Gemini Model
llm = ChatGoogleGenerativeAI(
   model="gemini-3.5-flash",
    temperature=0,
    google_api_key=google_api_key
)

# User Input
question = st.text_input("Ask about a property")

if st.button("Search"):

    if not question.strip():
        st.warning("Please enter a question.")
    else:

        docs = retriever.invoke(question)

        context = "\n\n".join(
            [doc.page_content for doc in docs]
        )

        prompt = f"""
You are a Real Estate Assistant.

Answer ONLY using the information below.

Property Information:
{context}

Question:
{question}

Answer:
"""

        response = llm.invoke(prompt)

        st.subheader("Answer")
        st.write(response.content)

        with st.expander("Retrieved Context"):
            st.write(context)