#include <stdio.h>   // Standard input-output header for printf and file operations
#include <stdlib.h>  // Standard library for exit function

#define PATH_ADDRESS "lab3_data/addresses.txt"
#define PAGE_SIZE 256
#define DISK_ADDRESS "lab3_data/BACKING_STORE.bin"

typedef struct {
    int frame_number;
    int valid_bit;
} TLB_Unit;

TLB_Unit TLB[15];

//Reads from fake disk
int read_disk(int page, char* buffer, FILE* file) {
    // Seek to the correct page in the file
    if (fseek(file, (long) page * PAGE_SIZE, SEEK_SET) != 0) {
        return -1; // Return an error code if seek fails
    }

    // Read PAGE_SIZE bytes from the file into the buffer
    size_t bytesRead = fread(buffer, 1, PAGE_SIZE, file);

    // Check if the read operation was successful
    if (bytesRead != PAGE_SIZE) {
        return -1; // Return an error code if read fails
    }

    return 0; // Return success
}

// Main function
int main() {
    FILE *file;  // File pointer
    char buffer[PAGE_SIZE];  // Buffer to hold each buffer of text

    
    // Open the file for reading
    file = fopen(PATH_ADDRESS, "r");

    // Check if file opening succeeded
    if (file == NULL) {
        perror("Error opening file");  // Print error message
        exit(EXIT_FAILURE);  // Exit program with failure status
    }
    // Read and print each buffer of the file
    while (fgets(buffer, sizeof(buffer), file)) {
        int number = atoi(buffer); // Convert buffer to integer
        int offset = number & 0xFF;
        int page_number = number >> 8;
        printf("Number: 0x%x\n", number); // Print the integer
        printf("Page Number: 0x%x\n", page_number);
        printf("Offset: 0x%x\n", offset);
    }

    // Close the file
    fclose(file);
    

    //Test reading binary
    file = fopen(DISK_ADDRESS, "rb");
    int return_value = read_disk(1, buffer, file);
    printf("Return value: %d\n", return_value);
    for(int i = 0; i < PAGE_SIZE; i++){
        printf("0x%x\n", *(buffer+i));
    }
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

/*Bypass TLB and use a only a page table in the beginning*/