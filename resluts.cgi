#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_LEN 50

// Display results for the user
void display_results(char *username) {
    char filename[MAX_LEN + 10];
    sprintf(filename, "%s_results.txt", username);

    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("No results found for user: %s\n", username);
        return;
    }

    printf("Content-Type: text/html\n\n");
    printf("<!DOCTYPE html>");
    printf("<html>");
    printf("<head><title>Your Results</title></head>");
    printf("<body>");
    printf("<h2>Quiz Results for %s</h2>", username);

    char line[100];
    while (fgets(line, sizeof(line), file)) {
        printf("<p>%s</p>", line);
    }

    printf("</body>");
    printf("</html>");

    fclose(file);
}

int main() {
    // Read input (Environment Variables)
    char *query = getenv("QUERY_STRING");
    if (query == NULL) {
        printf("Content-Type: text/plain\n\n");
        printf("No input provided.\n");
        return 1;
    }

    // Parse input (e.g., username=John)
    char username[MAX_LEN];
    sscanf(query, "username=%s", username);

    display_results(username);

    return 0;
}
