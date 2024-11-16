function login() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const users = JSON.parse(localStorage.getItem("users")) || {};
    if (users[username] && users[username] === password) {
        sessionStorage.setItem("loggedInUser", username);
        alert("Login successful! Redirecting to quiz...");
        window.location.href = "quiz.html";
    } else {
        alert("Invalid username or password. Please try again.");
    }
}
