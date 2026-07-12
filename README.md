#  Real Estate RAG Assistant

A Generative AI based Real Estate Question Answering system using **Retrieval Augmented Generation (RAG)**.

This project allows users to ask questions about real estate properties and get answers using information retrieved from property documents.

##  Project Overview

This application uses RAG architecture:

1. User asks a question
2. Relevant documents are retrieved from Vector Database
3. Retrieved information is passed to LLM
4. AI generates an accurate answer based only on provided data

##  Technologies Used

* Python
* LangChain
* ChromaDB
* HuggingFace Embeddings
* Ollama (Llama 3.2)
* Streamlit
* Vector Database
* RAG Architecture

##  Project Structure

```
Real_Estate_RAG/
│
├── app.py                 # Streamlit Web Application
├── rag.py                 # RAG chatbot logic
├── ingest.py              # Document processing and vector creation
├── config.py              # Configuration
│
├── data/                  # Property documents
│   ├── pdf/
│   ├── docx/
│   └── txt/
│
├── utils/
│   ├── loader.py          # Document loading
│   ├── splitter.py        # Text chunking
│   └── prompts.py         # Prompt templates
│
└── vector_db/             # Chroma vector database
```

##  Installation

Clone the repository:

```bash
git clone https://github.com/Kowmudi-karra/Real_Estate_RAG.git
```

Go to project folder:

```bash
cd Real_Estate_RAG
```

Install dependencies:

```bash
pip install -r requriments.txt
```

##  Environment Setup

Create `.env` file:

```
GOOGLE_API_KEY=your_api_key
```

Do not share API keys publicly.

##  Create Vector Database

Run:

```bash
python ingest.py
```

This will:

* Load documents
* Split documents into chunks
* Create embeddings
* Store vectors in ChromaDB

## Run RAG Chatbot

Run:

```bash
python rag.py
```

Example questions:

```
Which property is available in Hyderabad?

What are the amenities of Luxury Villa?

Tell me about apartment prices.
```

## Run Web Application

Run:

```bash
streamlit run app.py
```

The application will open in browser.

##  RAG Architecture

```
Documents
    |
    ↓
Document Loader
    |
    ↓
Text Splitter
    |
    ↓
HuggingFace Embeddings
    |
    ↓
Chroma Vector Database
    |
    ↓
Retriever
    |
    ↓
Ollama Llama 3.2
    |
    ↓
Final Answer
```

##  Features

✅ Ask questions about properties
✅ Document based answers
✅ Local LLM using Ollama
✅ Vector similarity search
✅ Streamlit user interface

##  Author

**Kowmudi Karra**

Generative AI | RAG | Python
