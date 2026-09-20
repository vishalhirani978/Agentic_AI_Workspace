import os

# pyrefly: ignore [missing-import]
from src.data_loader import load_all_documents
# pyrefly: ignore [missing-import]
from src.vectorstore import FaissVectorStore
# pyrefly: ignore [missing-import]
from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")

    # Index pehli baar khud ban jayega, uske baad seedha load hoga
    if not os.path.exists("faiss_store/faiss.index"):
        store.build_from_documents(docs)
    store.load()

    rag_search = RAGSearch()
    query = "What is time complexity?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)