function showResults() {
    const username = sessionStorage.getItem("loggedInUser");
    if (!username) {
        window.location.href = "login.html"; // Redirect if not logged in
        return;
    }

    const quizResults = JSON.parse(localStorage.getItem("quizResults")) || {};
    const userScore = quizResults[username];

    if (userScore !== undefined) {
        document.getElementById("score").innerText = `Your Score: ${userScore}`;
    } else {
        document.getElementById("score").innerText = "You haven't completed the quiz yet.";
    }
}

window.onload = showResults;
