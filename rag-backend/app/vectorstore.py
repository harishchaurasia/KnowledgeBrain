# app/vectorstore.py

import faiss
import numpy as np
from app.embeddings import model

#FAISS index dimension must match the embedding dimension.
embedding_dim = model.get_sentence_embedding_dimension()

#Create a simple L2 index.
#IndexFlatL2 = basic Euclidean distance search.

#Later: you can upgrade to IVF or HNSW for huge datasets.
index = faiss.IndexFlatL2(embedding_dim)

#Store text chunks + metadata alongside FAISS vectors.
docstore = []


def add_embeddings(chunks: list[str], embeddings: np.ndarray, metadata: dict):
    """
    Adds embeddings + corresponding chunks into FAISS + docstore.

    chunks: list of text chunks
    embeddings: numpy array of shape (N, dim)
    metadata: metadata to store for each chunk
    """

    #adding to FAISS index
    index.add(embeddings)

    #adding to docstore
    for chunk in chunks:
        docstore.append({
            "text": chunk,
            "metadata": metadata
        })


def search(query_embedding: np.ndarray, top_k: int = 3):
    """
    Returns top_k similar chunks from docstore based on vector similarity.
    """

    #querying the index
    #Query FAISS (D = distances, I = indices)
    D, I = index.search(query_embedding, top_k)

    results = []

    # I is a 2D array; we want the first row
    
    for i in I[0]: 
        if i < len(docstore):
            results.append(docstore[i])

    return results
