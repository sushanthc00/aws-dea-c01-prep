"""AWS DEA-C01 Mock Exam Simulator — Flask Backend."""

import json
import os
from pathlib import Path
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
QUESTIONS_DIR = Path(__file__).parent / "questions"


def load_exam(exam_id: str) -> dict:
    """Load exam questions from JSON file."""
    filepath = QUESTIONS_DIR / f"{exam_id}.json"
    if not filepath.exists():
        return None
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


@app.route("/")
def index():
    """Exam selection page."""
    exams = []
    for f in sorted(QUESTIONS_DIR.glob("*.json")):
        data = json.loads(f.read_text(encoding="utf-8"))
        exams.append({
            "id": f.stem,
            "title": data.get("title", f.stem),
            "question_count": len(data.get("questions", [])),
            "time_minutes": data.get("time_minutes", 170),
        })
    return render_template("index.html", exams=exams)


@app.route("/exam/<exam_id>")
def exam(exam_id: str):
    """Exam taking page."""
    data = load_exam(exam_id)
    if not data:
        return "Exam not found", 404
    return render_template("exam.html", exam_id=exam_id, exam=data)


@app.route("/api/exam/<exam_id>")
def api_exam(exam_id: str):
    """API endpoint for exam data (used by JS)."""
    data = load_exam(exam_id)
    if not data:
        return jsonify({"error": "Exam not found"}), 404
    # Strip answers and explanations for exam mode
    questions = []
    for q in data.get("questions", []):
        questions.append({
            "id": q["id"],
            "domain": q["domain"],
            "topic": q["topic"],
            "difficulty": q["difficulty"],
            "type": q["type"],
            "text": q["text"],
            "options": q["options"],
        })
    return jsonify({
        "title": data["title"],
        "time_minutes": data.get("time_minutes", 170),
        "questions": questions,
    })


@app.route("/api/exam/<exam_id>/answers")
def api_answers(exam_id: str):
    """API endpoint for answers and explanations (used after submission)."""
    data = load_exam(exam_id)
    if not data:
        return jsonify({"error": "Exam not found"}), 404
    answers = {}
    for q in data.get("questions", []):
        answers[q["id"]] = {
            "correct": q["correct"],
            "explanation": q["explanation"],
            "domain": q["domain"],
            "topic": q["topic"],
            "difficulty": q["difficulty"],
        }
    return jsonify(answers)


if __name__ == "__main__":
    print("Starting AWS DEA-C01 Mock Exam Simulator...")
    print("Open http://localhost:5000 in your browser")
    app.run(debug=True, port=5000)
