#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_USERS 100
#define MAX_LEN 50

// Structure to hold user data
typedef struct {
    char username[MAX_LEN];
    char password[MAX_LEN];
} User;

// Array to store registered users
User users[MAX_USERS];
int user_count = 0;

// Function to load existing users from file
void load_users() {
    FILE *file = fopen("users.txt", "r");
    if (file == NULL) return;

    while (fscanf(file, "%s %s", users[user_count].username, users[user_count].password) != EOF) {
        user_count++;
    }

    fclose(file);
}

// Handle login
int login(char *username, char *password) {
    for (int i = 0; i < user_count; i++) {
        if (strcmp(users[i].username, username) == 0 && strcmp(users[i].password, password) == 0) {
            return 1; // Successful login
        }
    }
    return 0; // Invalid credentials
}

int main() {
    // Load users from file
    load_users();

    // Read input (Environment Variables)
    char *query = getenv("QUERY_STRING");
    if (query == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("No input provided.\n");
        return 1;
    }

    // Parse input (e.g., username=user&password=pass)
    char username[MAX_LEN], password[MAX_LEN];
    sscanf(query, "username=%[^&]&password=%s", username, password);

    if (login(username, password)) {
        printf("Content-Type: text/plain\n\n");
        printf("Login successful.\n");
    } else {
        printf("Content-Type: text/plain\n\n");
        printf("Invalid username or password.\n");
    }

    return 0;
}
