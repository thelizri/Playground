#include <stdio.h>   // Standard input-output header for printf and file operations
#include <stdlib.h>  // Standard library for exit function

#define PATH_ADDRESSES "lab3_data/addresses.txt"

// Main function
int main() {
    FILE *file;  // File pointer
    char line[256];  // Buffer to hold each line of text

    // Open the file for reading
    file = fopen(PATH_ADDRESSES, "r");

    // Check if file opening succeeded
    if (file == NULL) {
        perror("Error opening file");  // Print error message
        exit(EXIT_FAILURE);  // Exit program with failure status
    }

    // Read and print each line of the file
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    // Close the file
    fclose(file);

    return 0;
}