#include <stdio.h>  // Standard input-output header for printf and file operations
#include <stdlib.h> // Standard library for exit function

#define PATH_ADDRESS "lab3_data/addresses.txt"
#define PAGE_SIZE 256
#define DISK_ADDRESS "lab3_data/BACKING_STORE.bin"

typedef struct
{
    int page_number;
    int frame_number;
    int valid_bit;
} MMU_Unit;

MMU_Unit Page_Table[256];
MMU_Unit TLB[16];
char Page_Frame[256][256];

// Reads from fake disk
int read_disk(int page, char *buffer, FILE *file)
{
    // Seek to the correct page in the file
    if (fseek(file, (long)page * PAGE_SIZE, SEEK_SET) != 0)
    {
        return -1; // Return an error code if seek fails
    }

    // Read PAGE_SIZE bytes from the file into the buffer
    size_t bytesRead = fread(buffer, 1, PAGE_SIZE, file);

    // Check if the read operation was successful
    if (bytesRead != PAGE_SIZE)
    {
        return -1; // Return an error code if read fails
    }

    return 0; // Return success
}

int load_page(int page, FILE *file){
    //Check the page table for page number
    //If found read page frame from Page_Frame
    //Else read page and put it in next available frame
    //Update the Page_table
    //Return page
}

// Main function
int main()
{
    FILE *file;
    FILE *binary;             // File pointer
    char buffer[PAGE_SIZE]; // Buffer to hold each buffer of text
    char line[PAGE_SIZE];

    // Open the file for reading
    file = fopen(PATH_ADDRESS, "r");
    binary = fopen(DISK_ADDRESS, "rb");

    // Check if file opening succeeded
    if (file == NULL)
    {
        perror("Error opening file"); // Print error message
        exit(EXIT_FAILURE);           // Exit program with failure status
    }
    // Read and print each buffer of the file
    while (fgets(line, sizeof(line), file))
    {
        int number = atoi(line); // Convert buffer to integer
        int offset = number & 0xFF;
        int page_number = number >> 8;
        
    }

    // Close the file
    fclose(file);
    fclose(binary);

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