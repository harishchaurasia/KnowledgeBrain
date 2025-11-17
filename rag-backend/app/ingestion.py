#fitz is a PyMuPDF library for pdf to text conversion
import fitz

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

    #join all text with double newlines for better separation -> clear logic for RAG model
    full_text = "\n\n".join(all_text)

    pdf.close() 
    
    return full_text