from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import shutil
import os
import uuid
import json

from loaders.pdf_loader import load_pdf
from loaders.ppt_loader import load_ppt
from rag.vector_store import build_vector_store
from rag.retriever import get_retriever
from llm.ollama_llm import get_llm
from chains.question_chain import generate_questions
from chains.answer_chain import generate_answers
# temporarily disabled for speed
# from chains.topic_chain import generate_topics

router = APIRouter()

UPLOAD_DIR = "uploads"
RESULTS_DIR = "results"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)


# -------------------------------
# BACKGROUND TASK (HEAVY WORK)
# -------------------------------
def process_file(file_path: str, job_id: str):
    print(f"[{job_id}] 1. Processing started")

    if file_path.endswith(".pdf"):
        text = load_pdf(file_path)
    else:
        text = load_ppt(file_path)

    print(f"[{job_id}] 2. Text extracted")

    vectorstore = build_vector_store(text)
    print(f"[{job_id}] 3. Vector store built")

    retriever = get_retriever(vectorstore)
    llm = get_llm()

    questions = generate_questions(llm, retriever)
    print(f"[{job_id}] 4. Questions generated")

    answers = generate_answers(llm, questions, retriever)
    print(f"[{job_id}] 5. Answers generated")

    result = {
        "questions": questions,
        "answers": answers,
        "topics": "disabled for speed optimization"
    }

    result_path = os.path.join(RESULTS_DIR, f"{job_id}.json")

    with open(result_path, "w", encoding="utf-8") as f:
        json.dump(result, f, indent=2)

    print(f"[{job_id}] 6. Processing finished")


# -------------------------------
# FAST UPLOAD ENDPOINT
# -------------------------------
@router.post("/upload")
def upload_file(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    job_id = str(uuid.uuid4())
    file_path = os.path.join(UPLOAD_DIR, f"{job_id}_{file.filename}")

    print(f"[{job_id}] Upload received")

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    background_tasks.add_task(process_file, file_path, job_id)

    print(f"[{job_id}] Response returned")

    return {
        "job_id": job_id,
        "status": "processing"
    }


# -------------------------------
# RESULT POLLING ENDPOINT
# -------------------------------
@router.get("/result/{job_id}")
def get_result(job_id: str):
    result_path = os.path.join(RESULTS_DIR, f"{job_id}.json")

    if not os.path.exists(result_path):
        return {"status": "processing"}

    with open(result_path, "r", encoding="utf-8") as f:
        return json.load(f)
