// Display quiz results for the logged-in user
function showResults() {
    const username = sessionStorage.getItem("loggedInUser");
    if (!username) {
        alert("You are not logged in!");
        window.location.href = "login.html";
        return;
    }

    const results = JSON.parse(localStorage.getItem("quizResults")) || {};
    const userScore = results[username] !== undefined ? results[username] : "No score yet";

    // Display results
    const resultsContainer = document.getElementById("results-container");
    resultsContainer.innerHTML = `
        <h1>Quiz Results</h1>
        <p>Welcome, <strong>${username}</strong>!</p>
        <p>Your Score: <strong>${userScore}</strong></p>
        <a href="index.html"><button>Return to Home</button></a>
    `;
}
