#include <stdio.h>  // Standard input-output header for printf and file operations
#include <stdlib.h> // Standard library for exit function
#include <string.h>

#define PATH_ADDRESS "lab3_data/addresses.txt"
#define PAGE_SIZE 256
#define DISK_ADDRESS "lab3_data/BACKING_STORE.bin"

typedef struct
{
    int page_number;
    int frame_number;
    int valid_bit;
} MMU_Unit;

MMU_Unit TLB[16];
MMU_Unit page_table[256];
char physical_memory[256][256];
int next_frame;

int page_faults;
int tlb_hits;

void initialize_TLB()
{
    for (int i = 0; i < 16; i++)
    {
        TLB[i].page_number = -1;  // Indicates an invalid entry
        TLB[i].frame_number = -1; // Indicates an invalid entry
        TLB[i].valid_bit = 0;     // 0 indicates the entry is not valid
    }
}

void initialize_page_table()
{
    for (int i = 0; i < 256; i++)
    {
        page_table[i].page_number = -1;  // Indicates an invalid entry
        page_table[i].frame_number = -1; // Indicates an invalid entry
        page_table[i].valid_bit = 0;     // 0 indicates the entry is not valid
    }
}

void initialize_physical_memory()
{
    for (int i = 0; i < 256; i++)
    {
        for (int j = 0; j < 256; j++)
        {
            physical_memory[i][j] = 0; // Initialize each byte to 0
        }
    }
}

// TLB First in First Out
void enqueue(int page_number, int frame_number)
{
    static int pos = 0;
    TLB[pos].page_number = page_number;
    TLB[pos].frame_number = frame_number;
    TLB[pos].valid_bit = 1;
    pos = (pos + 1) % 16;
}

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

    // Load the page into the frame
    memcpy(physical_memory[next_frame], buffer, PAGE_SIZE);

    // Update the page table
    page_table[next_frame].page_number = page;
    page_table[next_frame].frame_number = next_frame;
    page_table[next_frame].valid_bit = 1;
    next_frame += 1;

    return 0; // Return success
}

int check_tlb(int page_number)
{
    // Check the TLB for the page number
    for (int i = 0; i < 16; i++)
    {
        if (TLB[i].page_number == page_number && TLB[i].valid_bit)
        {
            // Page found in TLB
            int frame_number = TLB[i].frame_number;
            return frame_number;
        }
    }
    return -1;
}

int get_frame_number(int page_number)
{
    // Check the page table for the page number
    for (int i = 0; i < PAGE_SIZE; i++)
    {
        if (page_table[i].page_number == page_number && page_table[i].valid_bit)
        {
            // Page found in page table
            int frame_number = page_table[i].frame_number;
            return frame_number;
        }
    }
    return -1;
}

// Main function
int main()
{
    tlb_hits = 0;
    page_faults = 0;
    int readings = 0;

    initialize_TLB();
    initialize_page_table();
    initialize_physical_memory();
    next_frame = 0;

    FILE *file;
    FILE *binary;           // File pointer
    char buffer[PAGE_SIZE]; // Buffer to hold each buffer of text
    char line[PAGE_SIZE];

    // Open the file for reading
    file = fopen(PATH_ADDRESS, "r");
    binary = fopen(DISK_ADDRESS, "rb");

    // Check if file opening succeeded
    if (file == NULL || binary == NULL)
    {
        perror("Error opening file"); // Print error message
        exit(EXIT_FAILURE);           // Exit program with failure status
    }
    // Read and print each buffer of the file
    while (fgets(line, sizeof(line), file))
    {
        int logical_address = atoi(line); // Convert buffer to integer
        int offset = logical_address & 0xFF;
        int page_number = logical_address >> 8;

        // Get virtual address
        int frame_number = check_tlb(page_number);
        if (frame_number == -1)
        {
            frame_number = get_frame_number(page_number);
            if (frame_number == -1)
            {
                // Page Fault
                frame_number = next_frame;
                read_disk(page_number, buffer, binary);
                page_faults++;
            }
            enqueue(page_number, frame_number);
        }
        else
        {
            tlb_hits++;
        }

        int physical_address = (frame_number << 8) + offset;
        int value = (int)physical_memory[frame_number][offset];

        printf("Virtual address: %d, Physical address: %d, Value: %d\n", logical_address, physical_address, value);

        readings++;
        // Get physical address
        // 1. Check TLB
        // 2. Check page_table
        // 3. Update TLB
        // Get value in RAM
        // Keep track of page faults
        // Keep track of TLB hit rate
    }
    float tlb_hit_rate = (float)tlb_hits / readings * 100;
    float page_fault_rate = (float)page_faults / readings * 100;
    printf("Page faults %.1f %% \n", page_fault_rate);
    printf("TLB Hit rate %.1f %% \n", tlb_hit_rate);

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