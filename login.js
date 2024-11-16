#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 100
#define MAX_LEN 50

// Validate user login
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

