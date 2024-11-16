#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 50

// Function to calculate quiz score
int calculate_score(char *q1, char *q2) {
    int score = 0;

    if (strcmp(q1, "Paris") == 0) score++;
    if (strcmp(q2, "8") == 0) score++;

    return score;
}

// Save the result for the user
void save_result(char *username, int score) {
    char filename[MAX_LEN + 10];
    sprintf(filename, "%s_results.txt", username);

    FILE *file = fopen(filename, "a");
    if (file == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("Error saving results.\n");
        return;
    }

    fprintf(file, "Score: %d\n", score);
    fclose(file);
}

// Handle the quiz
void handle_quiz(char *username, char *q1, char *q2) {
    int score = calculate_score(q1, q2);

    // Save the result for the user
    save_result(username, score);

    printf("Content-Type: text/html\n\n");
    printf("<!DOCTYPE html>");
    printf("<html>");
    printf("<head><title>Quiz Result</title></head>");
    printf("<body>");
    printf("<h2>Thank you for taking the quiz, %s!</h2>", username);
    printf("<p>Your score: %d/2</p>", score);
    printf("</body>");
    printf("</html>");
}

int main() {
    // Read input (Environment Variables)
    char *query = getenv("QUERY_STRING");
    if (query == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("No input provided.\n");
        return 1;
    }

    // Parse input (e.g., username=John&q1=Paris&q2=8)
    char username[MAX_LEN], q1[MAX_LEN], q2[MAX_LEN];
    sscanf(query, "username=%[^&]&q1=%[^&]&q2=%s", username, q1, q2);

    handle_quiz(username, q1, q2);

    return 0;
}
