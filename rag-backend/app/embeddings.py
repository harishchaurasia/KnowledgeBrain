from sentence_transformers import SentenceTransformer
import numpy as np
from typing import List

#Loading the embedding model once at startup.
# MiniLM is small, fast, and perfect for local dev.
# Later we can replace with "BAAI/bge-large-en" or "thenlper/gte-large" for better performance.
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed_text(text: str) -> np.ndarray:
    """
    Embeds a single piece of text into a vector.
    Returns a numpy array of shape (1, embedding_dim).
    """

    #[] because model expects a list
    embedding = model.encode([text])
    embedding = np.array(embedding).astype("float32")
    return embedding


def embed_chunks(chunks: List[str]) -> np.ndarray:
    """
    Embeds a list of text chunks.
    Returns a 2D numpy array: (num_chunks, embedding_dim)
    """

    embeddings = model.encode(chunks, batch_size=16, show_progress_bar=False)
    embeddings = np.array(embeddings).astype("float32")
    
    return embeddings