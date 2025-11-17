# rag-backend/app/main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"Status":"OK"}



@app.get("/ingest/pdf")
async def ingest_pdf(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "PDF file", "filename": file.filename, "uploaded successfully."}


@app.get("/ingest/docx")
async def ingest_docx(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "DOCX file", "filename": file.filename, "uploaded successfully."}


@app.get("/ingest/txt")
async def ingest_txt(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "TXT file", "filename": file.filename, "uploaded successfully."}


@app.get("/ingest/csv")
async def ingest_csv(file: UploadFile = File(...)):
    file_path = f"data/docs/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "CSV file", "filename": file.filename, "uploaded successfully."}


@app.get("/ingest/audio")
async def ingest_audio(file: UploadFile = File(...)):
    file_path = f"data/audio/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())
    return {"message": "Audio file", "filename": file.filename, "uploaded successfully."}



@app.post("/ask")
async def ask_question(question: str):
    return {"question": question, "answer": "RAG ANSWER HERE"}

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    return {"message": "Audio transcription will be added later"}