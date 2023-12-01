#include <stdio.h>   // Standard input-output header for printf and file operations
#include <stdlib.h>  // Standard library for exit function

#define PATH_ADDRESSES "lab3_data/addresses.txt"

typedef struct {
    int frame_number;
    int valid_bit;
} TLB_Unit;

TLB_Unit TLB[15];

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
        int number = atoi(line); // Convert line to integer
        int offset = number & 0xFF;
        int page_number = number >> 8;
        printf("Number: 0x%x\n", number); // Print the integer
        printf("Page Number: 0x%x\n", page_number);
        printf("Offset: 0x%x\n", offset);
    }

    // Close the file
    fclose(file);

    return 0;
}

/*
* 16 entries in the TLB
* 256 entries in the page table
* Page size of 256 bytes
* 256 frames in the physical memory
* Frame size of 256 bytes
* Physical memory of 65 536 bytes (256x256)
*/