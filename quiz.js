// Quiz questions
const quizQuestions = [
    { question: "What is the capital of France?", options: ["Paris", "London", "Berlin", "Madrid"], answer: "Paris" },
    { question: "What is 2 + 2?", options: ["3", "4", "5", "6"], answer: "4" },
    { question: "Who wrote 'Hamlet'?", options: ["Shakespeare", "Homer", "Dante", "Chaucer"], answer: "Shakespeare" }
];

// Render quiz questions
function renderQuiz() {
    const quizContainer = document.getElementById("quiz-container");
    quizQuestions.forEach((q, index) => {
        const questionDiv = document.createElement("div");
        questionDiv.innerHTML = `<p>${q.question}</p>`;
        q.options.forEach(option => {
            questionDiv.innerHTML += `
                <input type="radio" name="q${index}" value="${option}" required> ${option}<br>
            `;
        });
        quizContainer.appendChild(questionDiv);
    });
}

// Handle quiz submission
function submitQuiz() {
    let score = 0;
    quizQuestions.forEach((q, index) => {
        const selectedOption = document.querySelector(`input[name="q${index}"]:checked`);
        if (selectedOption && selectedOption.value === q.answer) {
            score++;
        }
    });

    const username = sessionStorage.getItem("loggedInUser");
    if (username) {
        const results = JSON.parse(localStorage.getItem("quizResults")) || {};
        results[username] = score;
        localStorage.setItem("quizResults", JSON.stringify(results));
    }

    alert(`Your Score: ${score}/${quizQuestions.length}`);
    window.location.href = "index.html";
}
