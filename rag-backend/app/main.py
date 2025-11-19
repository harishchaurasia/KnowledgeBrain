# rag-backend/app/main.py

from fastapi import FastAPI, File, UploadFile
from app.ingestion import extract_text_from_pdf





app = FastAPI()

#---------------------------------ENDPOINTS---------------------------------
#Get Endpoints
#---------------------------------------------------------------------------

#test endpoint
@app.get("/test/pdf")
def test_pdf():
    text = extract_text_from_pdf("data/docs/Harish_AIML.pdf")
    return {"text_sample": text[:500]}


@app.get("/")
def root():
    return {"Status":"OK"}


@app.get("/ingest/pdf")
async def ingest_pdf(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    info = ingest_pdf_file(file_path)
    
    return {
        "message": "PDF ingested successfully",
        "filename": file.filename,
        "chunks_created": info["chunks_created"]
    }


@app.get("/ingest/docx")
async def ingest_docx(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "DOCX file uploaded successfully.", "filename": file.filename}


@app.get("/ingest/txt")
async def ingest_txt(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "TXT file uploaded successfully.", "filename": file.filename}


@app.get("/ingest/csv")
async def ingest_csv(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "CSV file uploaded successfully.", "filename": file.filename}


@app.get("/ingest/audio")
async def ingest_audio(file: UploadFile = File(...)):
    file_path = f"data/audio/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "Audio file uploaded successfully.", "filename": file.filename}


#---------------------------------ENDPOINTS---------------------------------
#Post Endpoints
#---------------------------------------------------------------------------

@app.post("/ask")
async def ask_question(question: str):
    return {"question": question, "answer": "RAG ANSWER HERE"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    return {"message": "Audio transcription will be added later"}