#fitz is a PyMuPDF library for pdf to text conversion
import fitz
import re
from typing import List

def extract_text_from_pdf(path: str) -> str:
    """
    Extracts raw text from a PDF file.
    
    path: file path to the PDF
    returns: big string with all text
    """

    pdf = fitz.open(path)
    all_text = []

    for page_num, page in enumerate(pdf):
        page_text = page.get_text()
        page_text = page_text.strip()

        if len(page_text) > 0:
            all_text.append(page_text)

    #joining all the text with double newlines for better separation -> clear logic for RAG model
    full_text = "\n\n".join(all_text)

    pdf.close() 
    
    return full_text



def split_into_sentences(text: str) -> List[str]:
    """
    Splits text into sentences using punctuation.
    Uses a simple regex-based split.
    """

    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    return sentences

def chunk_text(text: str, max_chunk_size: int = 600, overlap: int = 100) -> List[str]:
    """
    Splits large text into chunks with overlap.
    """

    sentences = split_into_sentences(text)
    chunks = []
    current_chunk = ""

    if sentence in sentences:
        if len(current_chunk) + len(sentence) <= max_chunk_size:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            overlap_text = sentence[-overlap:]
            current_chunk = overlap_text + " " + sentence
    
     # Appending the final chunk
    if current_chunk.strip():
        chunks.append(current_chunk.strip())

    return chunks
