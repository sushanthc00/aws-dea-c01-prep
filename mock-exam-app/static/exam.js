/**
 * AWS DEA-C01 Mock Exam Simulator — Frontend Logic
 */

let questions = [];
let answers = {};       // user answers: { questionId: [selectedOptions] }
let flagged = new Set();
let currentIndex = 0;
let timerInterval = null;
let timeRemaining = 0;  // seconds
let examSubmitted = false;
let correctAnswers = {}; // loaded after submission

// ─── Initialization ───

async function init() {
    try {
        const res = await fetch(`/api/exam/${EXAM_ID}`);
        const data = await res.json();
        questions = data.questions;
        timeRemaining = data.time_minutes * 60;

        if (SHUFFLE) shuffleArray(questions);

        // Restore progress from localStorage
        restoreProgress();

        document.getElementById('total-count').textContent = questions.length;
        buildNavGrid();
        renderQuestion();
        startTimer();
        updateProgress();
    } catch (err) {
        console.error('Failed to load exam:', err);
        alert('Failed to load exam data. Please refresh.');
    }
}

function shuffleArray(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [arr[i], arr[j]] = [arr[j], arr[i]];
    }
}

// ─── Timer ───

function startTimer() {
    updateTimerDisplay();
    timerInterval = setInterval(() => {
        timeRemaining--;
        updateTimerDisplay();
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            alert('Time is up! Your exam will be submitted.');
            submitExam();
        }
    }, 1000);
}

function updateTimerDisplay() {
    const mins = Math.floor(timeRemaining / 60);
    const secs = timeRemaining % 60;
    const el = document.getElementById('timer');
    el.textContent = `${mins}:${secs.toString().padStart(2, '0')}`;
    if (timeRemaining <= 300) el.classList.add('timer-warning');
}

// ─── Question Rendering ───

function renderQuestion() {
    const q = questions[currentIndex];
    const qId = q.id;

    document.getElementById('question-number').textContent =
        `Question ${currentIndex + 1} of ${questions.length}`;
    document.getElementById('question-meta').textContent =
        `Domain ${q.domain} | ${q.topic} | ${q.difficulty}`;
    document.getElementById('question-type').textContent =
        q.type === 'single' ? 'Single Answer' : `Multiple Answer — Select ${q.type.replace('multi-', '')}`;
    document.getElementById('question-text').textContent = q.text;

    // Flag button
    const flagBtn = document.getElementById('flag-btn');
    flagBtn.classList.toggle('active', flagged.has(qId));

    // Options
    const optionsList = document.getElementById('options-list');
    optionsList.innerHTML = '';
    const userAnswer = answers[qId] || [];

    q.options.forEach((opt, i) => {
        const letter = String.fromCharCode(65 + i);
        const div = document.createElement('div');
        div.className = 'option-item';
        if (userAnswer.includes(letter)) div.classList.add('selected');

        // In review mode, show correct/incorrect
        if (examSubmitted && correctAnswers[qId]) {
            const correct = correctAnswers[qId].correct;
            if (correct.includes(letter)) {
                div.classList.add('correct');
            } else if (userAnswer.includes(letter)) {
                div.classList.add('incorrect');
            }
        }

        div.innerHTML = `
            <span class="option-letter">${letter}</span>
            <span class="option-text">${opt}</span>
        `;

        if (!examSubmitted) {
            div.onclick = () => selectOption(qId, letter, q.type);
        }
        optionsList.appendChild(div);
    });

    // Show explanation in review mode
    if (examSubmitted && correctAnswers[qId]) {
        const existing = optionsList.parentElement.querySelector('.explanation');
        if (existing) existing.remove();
        const expDiv = document.createElement('div');
        expDiv.className = 'explanation';
        expDiv.textContent = correctAnswers[qId].explanation;
        optionsList.after(expDiv);
    }

    // Nav buttons
    document.getElementById('prev-btn').disabled = currentIndex === 0;
    document.getElementById('next-btn').textContent =
        currentIndex === questions.length - 1 ? 'Finish' : 'Next →';

    // Update nav grid
    updateNavGrid();
}

function selectOption(qId, letter, type) {
    if (!answers[qId]) answers[qId] = [];

    if (type === 'single') {
        answers[qId] = [letter];
    } else {
        const maxSelect = parseInt(type.replace('multi-', ''));
        const idx = answers[qId].indexOf(letter);
        if (idx >= 0) {
            answers[qId].splice(idx, 1);
        } else {
            if (answers[qId].length < maxSelect) {
                answers[qId].push(letter);
            } else {
                // Replace oldest selection
                answers[qId].shift();
                answers[qId].push(letter);
            }
        }
    }

    saveProgress();
    renderQuestion();
    updateProgress();
}

// ─── Navigation ───

function nextQuestion() {
    if (currentIndex < questions.length - 1) {
        currentIndex++;
        renderQuestion();
    }
}

function prevQuestion() {
    if (currentIndex > 0) {
        currentIndex--;
        renderQuestion();
    }
}

function goToQuestion(index) {
    currentIndex = index;
    renderQuestion();
}

function toggleFlag() {
    const qId = questions[currentIndex].id;
    if (flagged.has(qId)) {
        flagged.delete(qId);
    } else {
        flagged.add(qId);
    }
    saveProgress();
    renderQuestion();
    updateProgress();
}

// ─── Navigation Grid ───

function buildNavGrid() {
    const grid = document.getElementById('nav-grid');
    grid.innerHTML = '';
    questions.forEach((q, i) => {
        const btn = document.createElement('button');
        btn.className = 'nav-btn';
        btn.textContent = i + 1;
        btn.onclick = () => goToQuestion(i);
        btn.id = `nav-${i}`;
        grid.appendChild(btn);
    });
}

function updateNavGrid() {
    questions.forEach((q, i) => {
        const btn = document.getElementById(`nav-${i}`);
        if (!btn) return;
        btn.className = 'nav-btn';
        if (i === currentIndex) btn.classList.add('current');
        if (answers[q.id] && answers[q.id].length > 0) btn.classList.add('answered');
        if (flagged.has(q.id)) btn.classList.add('flagged');
    });
}

function updateProgress() {
    const answeredCount = questions.filter(q => answers[q.id] && answers[q.id].length > 0).length;
    document.getElementById('answered-count').textContent = answeredCount;

    const flaggedCount = flagged.size;
    const summary = document.getElementById('nav-summary');
    summary.textContent = `${answeredCount} answered | ${flaggedCount} flagged | ${questions.length - answeredCount} remaining`;
}

// ─── Submission ───

async function submitExam() {
    const answeredCount = questions.filter(q => answers[q.id] && answers[q.id].length > 0).length;
    const unanswered = questions.length - answeredCount;

    if (unanswered > 0 && !examSubmitted) {
        const proceed = confirm(
            `You have ${unanswered} unanswered question(s). Are you sure you want to submit?`
        );
        if (!proceed) return;
    }

    clearInterval(timerInterval);
    examSubmitted = true;

    // Fetch correct answers
    try {
        const res = await fetch(`/api/exam/${EXAM_ID}/answers`);
        correctAnswers = await res.json();
    } catch (err) {
        console.error('Failed to load answers:', err);
        alert('Failed to load answers. Please try again.');
        return;
    }

    // Calculate score
    let totalCorrect = 0;
    const domainScores = {};

    questions.forEach(q => {
        const qId = q.id;
        const userAns = (answers[qId] || []).sort().join(',');
        const correctAns = (correctAnswers[qId]?.correct || []).sort().join(',');
        const isCorrect = userAns === correctAns;

        if (isCorrect) totalCorrect++;

        const domain = `Domain ${q.domain}`;
        if (!domainScores[domain]) domainScores[domain] = { correct: 0, total: 0 };
        domainScores[domain].total++;
        if (isCorrect) domainScores[domain].correct++;
    });

    const percentage = Math.round((totalCorrect / questions.length) * 100);
    const passed = percentage >= 72;

    // Show results
    document.querySelector('.exam-body').style.display = 'none';
    const resultsPanel = document.getElementById('results-panel');
    resultsPanel.style.display = 'block';

    // Score display
    const scoreDisplay = document.getElementById('score-display');
    scoreDisplay.innerHTML = `
        <div class="score-number ${passed ? 'score-pass' : 'score-fail'}">${percentage}%</div>
        <div>${totalCorrect} / ${questions.length} correct</div>
        <div style="font-size:1.3rem;margin-top:0.5rem;font-weight:600;color:${passed ? 'var(--correct)' : 'var(--incorrect)'}">
            ${passed ? '✓ PASS' : '✗ FAIL'}
        </div>
        <div style="color:#666;margin-top:0.5rem">Passing threshold: 72% (~720/1000)</div>
    `;

    // Domain breakdown
    const domainNames = {
        'Domain 1': 'Ingestion & Transformation (34%)',
        'Domain 2': 'Data Store Management (26%)',
        'Domain 3': 'Operations & Support (22%)',
        'Domain 4': 'Security & Governance (18%)',
    };

    const breakdown = document.getElementById('domain-breakdown');
    breakdown.innerHTML = '<h3 style="margin-bottom:1rem">Domain Breakdown</h3>';
    Object.entries(domainScores).sort().forEach(([domain, scores]) => {
        const pct = Math.round((scores.correct / scores.total) * 100);
        const color = pct >= 72 ? 'var(--correct)' : pct >= 60 ? 'var(--flagged)' : 'var(--incorrect)';
        breakdown.innerHTML += `
            <div class="domain-row">
                <span class="domain-name">${domainNames[domain] || domain}</span>
                <div class="domain-bar">
                    <div class="domain-fill" style="width:${pct}%;background:${color}"></div>
                </div>
                <span class="domain-score" style="color:${color}">${scores.correct}/${scores.total} (${pct}%)</span>
            </div>
        `;
    });

    clearProgress();
}

function reviewAnswers() {
    const section = document.getElementById('review-section');
    section.style.display = 'block';
    section.innerHTML = '<h3>Answer Review</h3>';

    questions.forEach((q, i) => {
        const qId = q.id;
        const userAns = (answers[qId] || []).sort().join(',');
        const correct = correctAnswers[qId]?.correct || [];
        const correctAns = correct.sort().join(',');
        const isCorrect = userAns === correctAns;

        const div = document.createElement('div');
        div.className = `review-question ${isCorrect ? 'review-correct' : 'review-incorrect'}`;

        let optionsHtml = q.options.map((opt, oi) => {
            const letter = String.fromCharCode(65 + oi);
            const isUserSelected = (answers[qId] || []).includes(letter);
            const isCorrectOpt = correct.includes(letter);
            let cls = '';
            if (isCorrectOpt) cls = 'correct';
            else if (isUserSelected) cls = 'incorrect';
            return `<div class="option-item ${cls}" style="cursor:default;padding:0.5rem 0.75rem">
                <span class="option-letter">${letter}</span>
                <span class="option-text">${opt}</span>
            </div>`;
        }).join('');

        div.innerHTML = `
            <div class="review-header">
                <span>Q${i + 1} | Domain ${q.domain} | ${q.topic} | ${q.difficulty}</span>
                <span class="review-result ${isCorrect ? 'correct' : 'incorrect'}">
                    ${isCorrect ? '✓ Correct' : '✗ Incorrect'}
                </span>
            </div>
            <div class="question-text" style="margin-bottom:0.75rem">${q.text}</div>
            <div style="display:flex;flex-direction:column;gap:0.4rem">${optionsHtml}</div>
            <div class="explanation">${correctAnswers[qId]?.explanation || 'No explanation available.'}</div>
        `;
        section.appendChild(div);
    });

    section.scrollIntoView({ behavior: 'smooth' });
}

// ─── Progress Persistence ───

function saveProgress() {
    const state = {
        answers,
        flagged: Array.from(flagged),
        currentIndex,
        timeRemaining,
    };
    localStorage.setItem(`exam-${EXAM_ID}`, JSON.stringify(state));
}

function restoreProgress() {
    const saved = localStorage.getItem(`exam-${EXAM_ID}`);
    if (saved) {
        try {
            const state = JSON.parse(saved);
            answers = state.answers || {};
            flagged = new Set(state.flagged || []);
            currentIndex = state.currentIndex || 0;
            if (state.timeRemaining) timeRemaining = state.timeRemaining;
        } catch (e) {
            console.warn('Failed to restore progress:', e);
        }
    }
}

function clearProgress() {
    localStorage.removeItem(`exam-${EXAM_ID}`);
}

// ─── Keyboard Navigation ───

document.addEventListener('keydown', (e) => {
    if (examSubmitted) return;
    if (e.key === 'ArrowRight' || e.key === 'n') nextQuestion();
    if (e.key === 'ArrowLeft' || e.key === 'p') prevQuestion();
    if (e.key === 'f') toggleFlag();
    if (e.key >= 'a' && e.key <= 'e') {
        const q = questions[currentIndex];
        const letter = e.key.toUpperCase();
        if (letter.charCodeAt(0) - 65 < q.options.length) {
            selectOption(q.id, letter, q.type);
        }
    }
});

// ─── Start ───
init();
