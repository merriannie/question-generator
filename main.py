from pathlib import Path

import requests
from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI()
app.mount("/static", StaticFiles(directory=str(BASE_DIR / "static")), name="static")


def build_page(results_html):
    with open(BASE_DIR / "static" / "index.html", "r", encoding="utf-8") as f:
        page = f.read()
    return page.replace("{{RESULTS}}", results_html)


def build_fallback_questions(subject: str, topic: str, count_value: int):
    templates = [
        f"What is the main idea of {topic} in {subject}?",
        f"Can you explain one important fact about {topic}?",
        f"Why is {topic} important in {subject}?",
        f"Give one example that shows {topic} in {subject}.",
    ]
    return [templates[index % len(templates)] for index in range(count_value)]


@app.get("/", response_class=HTMLResponse)
def homepage():
    return build_page("")


@app.post("/generate", response_class=HTMLResponse)
def generate(
    subject: str = Form(...),
    topic: str = Form(...),
    count: str = Form(...),
):
    count_value = int(count)
    try:
        response = requests.post(
            "https://questions.startocode.com/generate",
            json={"subject": subject, "topic": topic, "count": count_value},
            timeout=10,
        )
        response.raise_for_status()
        questions = response.json()
    except Exception:
        questions = build_fallback_questions(subject, topic, count_value)

    questions_html = f"<div class='card'><h2>{count_value} questions on \"{topic}\" ({subject})</h2>"

    for index, question in enumerate(questions[:count_value]):
        questions_html += f"""
        <div class='question-item'>
            <span class='question-number'>{index + 1}</span>
            {question}
        </div>
        """

    questions_html += "</div>"
    return build_page(questions_html)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=3003)
