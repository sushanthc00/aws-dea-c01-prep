# AWS DEA-C01 Mock Exam Simulator

A local web application that simulates the AWS certification exam environment.

## Features
- Timed exam simulation (170 minutes)
- Question navigation panel
- Flag questions for review
- Single-answer and multiple-answer question support
- Score calculation with domain breakdown
- Detailed explanations after submission
- Progress persistence (localStorage)
- Randomization options
- Responsive design

## Quick Start

```bash
cd src/aws-dea-c01-prep/mock-exam-app
pip install flask
python app.py
```

Then open http://localhost:5000 in your browser.

## Tech Stack
- Backend: Python Flask
- Frontend: Vanilla HTML/CSS/JS
- Data: JSON question bank
- Storage: Browser localStorage for progress

## Project Structure
```
mock-exam-app/
├── app.py                 # Flask server
├── questions/
│   ├── exam1.json         # Mock Exam 1 questions
│   └── exam2.json         # Mock Exam 2 questions
├── static/
│   ├── style.css          # Exam UI styles
│   └── exam.js            # Exam logic (timer, navigation, scoring)
└── templates/
    ├── index.html          # Exam selection page
    ├── exam.html           # Exam taking page
    └── results.html        # Results and review page
```
