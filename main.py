from qna import get_answer
from explanation_module import explain_topic
from summary_module import summarize_text
from quiz_module import generate_quiz
from learning_path import get_learning_path
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI(title="EduGenie")

BASE_DIR = Path(__file__).resolve().parent

app.mount(
    "/static",
    StaticFiles(directory=BASE_DIR / "static"),
    name="static"
)


@app.get("/", response_class=HTMLResponse)
async def home():
    html_file = BASE_DIR / "templates" / "index.html"

    return html_file.read_text(encoding="utf-8")


@app.post("/qa")
async def qa(data: dict):
    question = data.get("question", "")

    answer = get_answer(question)

    return {
        "answer": answer
    }


@app.post("/explain")
async def explain(data: dict):
    topic = data.get("topic", "")

    explanation = explain_topic(topic)

    return {
        "explanation": explanation
    }


@app.post("/quiz")
async def quiz(data: dict):
    topic = data.get("topic", "")

    result = generate_quiz(topic)

    return result


@app.post("/summarize")
async def summarize(data: dict):
    text = data.get("text", "")
    summary = summarize_text(text)
    return {"summary": summary}


@app.post("/learn/recommendations")
async def learning_recommendations(data: dict):
    topic = data.get("topic", "")
    recommendations = get_learning_path(topic)
    return {"recommendations": recommendations}
    