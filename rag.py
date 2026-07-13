from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load ChromaDB
vector_store = Chroma(
    persist_directory="vector_db",
    embedding_function=embeddings
)

# Create retriever
retriever = vector_store.as_retriever(
    search_kwargs={"k": 2}
)

print("Retriever loaded successfully!")

# Load Ollama Llama 3.2
llm = ChatOllama(
    model="llama3.2"
)

while True:
    query = input("\nAsk about a property (or type 'exit'): ")

    if query.lower() == "exit":
        print("Goodbye!")
        break

    # Retrieve documents
    docs = retriever.invoke(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are a Real Estate Assistant.

Use only the information below to answer.

Property Information:
{context}

Question:
{query}

Answer:
"""

    response = llm.invoke(prompt)

    print("\nAnswer:\n")
    print(response.content)