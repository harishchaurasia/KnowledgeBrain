# app/query.py

from app.embeddings import embed_text
from app.vectorstore import search
from typing import List

def retrieve_relevant_chunks(question: str, top_k: int = 3) -> List[dict]:
"""
    Full retrieval pipeline:
    - embed question
    - search FAISS index
    - return top-k chunks with metadata
    """

    #Embedding the user's question
    query_vec = embed_text(question)

    #searching the FAISS index
    results = search(query_vec, top_k=top_k)

    return results

