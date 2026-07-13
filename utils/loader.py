from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    BSHTMLLoader,
)

from langchain_core.documents import Document


def load_documents(data_folder: str):
    """
    Load PDF, DOCX and HTML documents
    """
    documents = []

    data_path = Path(data_folder)

    for file in data_path.rglob("*"):

        if file.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file))

        elif file.suffix.lower() == ".docx":
            loader = Docx2txtLoader(str(file))

        elif file.suffix.lower() in [".html", ".htm"]:
            loader = BSHTMLLoader(str(file))

        else:
            continue

        docs = loader.load()

        for doc in docs:
            doc.metadata["source"] = str(file)

        documents.extend(docs)

    return documents