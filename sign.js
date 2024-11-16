// Save user data to localStorage
function signup() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username && password) {
        // Store user data in localStorage
        const users = JSON.parse(localStorage.getItem("users")) || {};
        if (users[username]) {
            alert("Username already exists! Please choose another.");
        } else {
            users[username] = password;
            localStorage.setItem("users", JSON.stringify(users));
            alert("Sign-up successful! Redirecting to login...");
            window.location.href = "login.html";
        }
    } else {
        alert("Please provide both username and password.");
    }
}

