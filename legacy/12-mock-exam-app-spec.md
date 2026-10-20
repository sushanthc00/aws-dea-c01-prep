# H. Local Mock Exam Website — Product & Technical Spec

## Overview
A local web application that simulates the AWS certification exam environment for practice.

## Tech Stack
- **Backend**: Python Flask (lightweight, you already have Python)
- **Frontend**: Vanilla HTML/CSS/JS (no build step, instant startup)
- **Data**: JSON files for question bank
- **Storage**: Browser localStorage for progress persistence
- **Hosting**: Local only (localhost:5000)

## Architecture
```
Browser (HTML/CSS/JS)
    ↕ HTTP
Flask Server (Python)
    ↕ File I/O
JSON Question Bank (questions/*.json)
```

## Data Model — Question Bank JSON Schema

```json
{
  "title": "string — exam title",
  "time_minutes": "number — exam duration in minutes",
  "questions": [
    {
      "id": "string — unique question ID (e.g., 'e1q1')",
      "domain": "number — exam domain (1-4)",
      "topic": "string — specific topic",
      "difficulty": "string — Easy | Medium | Hard",
      "type": "string — 'single' or 'multi-2' or 'multi-3'",
      "text": "string — question text",
      "options": ["string array — answer options (A through E)"],
      "correct": ["string array — correct answer letters"],
      "explanation": "string — detailed explanation"
    }
  ]
}
```

## Features

### Core (Built — Phase 1)
- [x] Exam selection page
- [x] Timed exam simulation (countdown timer)
- [x] Question display with single/multi-answer support
- [x] Question navigation grid (sidebar)
- [x] Flag questions for review
- [x] Previous/Next navigation
- [x] Keyboard shortcuts (arrow keys, a-e for options, f for flag)
- [x] Submit exam with confirmation
- [x] Score calculation with pass/fail
- [x] Domain-wise score breakdown with visual bars
- [x] Full answer review with explanations
- [x] Correct/incorrect highlighting in review
- [x] Progress persistence (localStorage)
- [x] Question randomization option
- [x] Responsive design
- [x] Timer warning (last 5 minutes)

### Phase 2 (Stretch — Add Later)
- [ ] Add remaining 55 questions to each exam JSON
- [ ] Analytics dashboard (historical scores, improvement tracking)
- [ ] Weak domain identification and targeted practice mode
- [ ] Custom exam builder (select domains, difficulty, question count)
- [ ] Spaced repetition for missed questions
- [ ] Export results as PDF
- [ ] Dark mode
- [ ] Import custom question banks

## Timer Behavior
- Starts at exam duration (170 min) and counts down
- Displays MM:SS format
- Turns red and pulses when < 5 minutes remain
- Auto-submits when timer reaches 0
- Persisted in localStorage (survives page refresh)

## Question Navigation
- Grid of numbered buttons in sidebar
- Color-coded: blue (answered), orange (flagged), gray (unanswered)
- Current question highlighted with border
- Click any number to jump to that question
- Summary shows answered/flagged/remaining counts

## Submit and Review Flow
1. Click "Submit Exam" → confirmation dialog (shows unanswered count)
2. Timer stops
3. Answers fetched from server (explanations included)
4. Score calculated and displayed
5. Domain breakdown shown with color-coded bars
6. "Review All Answers" button shows every question with:
   - Your answer highlighted
   - Correct answer highlighted
   - Detailed explanation

## Score Calculation
- Each question worth 1 point (no partial credit for multi-answer)
- Multi-answer: ALL correct options must be selected (no partial)
- Percentage = correct / total × 100
- Pass threshold: 72% (approximating AWS's 720/1000)

## How to Run

```bash
cd src/aws-dea-c01-prep/mock-exam-app
pip install flask
python app.py
# Open http://localhost:5000
```

## How to Add More Questions

1. Edit `questions/exam1.json` or `questions/exam2.json`
2. Follow the JSON schema above
3. Each question needs a unique `id`
4. Restart the Flask server (or it auto-reloads in debug mode)

## Estimated Complexity

| Phase | Effort | What's Included |
|---|---|---|
| Phase 1 (Core) | ~2-3 hours | ✅ Already built — all core features |
| Add full 65 questions per exam | ~1-2 hours | Copy from markdown mock exams to JSON |
| Phase 2 analytics | ~3-4 hours | Score history, charts, weak area detection |
| Phase 2 custom exams | ~2-3 hours | Domain/difficulty filters, custom question count |
| Phase 2 spaced repetition | ~3-4 hours | Track missed questions, resurface them |

## Accessibility Considerations
- Keyboard navigation supported (arrow keys, letter keys)
- Semantic HTML structure
- Color is not the only indicator (text labels accompany colors)
- Sufficient color contrast ratios
- Screen reader compatible (semantic elements, ARIA where needed)
- Responsive layout for different screen sizes
