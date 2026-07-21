import os

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def build_vector_database():

    print("Loading Business Knowledge...")

    documents = []

    folder = "data/documents"

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            loader = TextLoader(
                os.path.join(folder, file),
                encoding="utf-8"
            )

            documents.extend(loader.load())

    print(f"Loaded {len(documents)} document(s)")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    print(f"Created {len(docs)} chunks")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating FAISS Vector Database...")

    vector_db = FAISS.from_documents(
        docs,
        embeddings
    )

    vector_db.save_local("data/vectorstore")

    print("✅ FAISS Database Created Successfully!")


if __name__ == "__main__":

    build_vector_database()