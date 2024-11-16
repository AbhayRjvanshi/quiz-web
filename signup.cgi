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

// Function to save new user to file
void save_user(User user) {
    FILE *file = fopen("users.txt", "a");
    if (file == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("Error saving user.\n");
        return;
    }
    fprintf(file, "%s %s\n", user.username, user.password);
    fclose(file);
}

// Handle sign-up
void signup(char *username, char *password) {
    // Check if user already exists
    for (int i = 0; i < user_count; i++) {
        if (strcmp(users[i].username, username) == 0) {
            printf("Content-Type: text/plain\n\n");
            printf("User already exists.\n");
            return;
        }
    }

    // Add new user
    User new_user;
    strcpy(new_user.username, username);
    strcpy(new_user.password, password);
    users[user_count++] = new_user;

    // Save to file
    save_user(new_user);

    printf("Content-Type: text/plain\n\n");
    printf("Sign-up successful.\n");
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

    signup(username, password);

    return 0;
}
