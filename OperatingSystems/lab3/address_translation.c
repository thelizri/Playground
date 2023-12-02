#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define PATH_ADDRESS "lab3_data/addresses.txt"
#define PAGE_SIZE 256
#define DISK_ADDRESS "lab3_data/BACKING_STORE.bin"
#define TLB_SIZE 16
#define PAGE_TABLE_SIZE 256
#define MEMORY_SIZE 256

typedef struct {
    int page_number;
    int frame_number;
    int valid_bit;
} MMU_Unit;

MMU_Unit TLB[TLB_SIZE];
MMU_Unit page_table[PAGE_TABLE_SIZE];
char memory[MEMORY_SIZE][PAGE_SIZE];
int next_free_frame;
int page_faults;
int tlb_hits;

void initializeTLB() {
    for (int i = 0; i < TLB_SIZE; i++) {
        TLB[i] = (MMU_Unit){-1, -1, 0};
    }
}

void initializePageTable() {
    for (int i = 0; i < PAGE_TABLE_SIZE; i++) {
        page_table[i] = (MMU_Unit){-1, -1, 0};
    }
}

void initializeMemory() {
    memset(memory, 0, sizeof(memory));
}

void updateTLB(int page_number, int frame_number) {
    static int position = 0;
    TLB[position] = (MMU_Unit){page_number, frame_number, 1};
    position = (position + 1) % TLB_SIZE;
}

int loadPage(int page, FILE *disk) {
    fseek(disk, (long)page * PAGE_SIZE, SEEK_SET);
    if (fread(memory[next_free_frame], 1, PAGE_SIZE, disk) != PAGE_SIZE) {
        return -1;
    }

    page_table[next_free_frame] = (MMU_Unit){page, next_free_frame, 1};
    next_free_frame++;
    return 0;
}

int findFrameNumber(int page_number) {
    for (int i = 0; i < TLB_SIZE; i++) {
        if (TLB[i].page_number == page_number && TLB[i].valid_bit) {
            tlb_hits++;
            return TLB[i].frame_number;
        }
    }

    for (int i = 0; i < PAGE_TABLE_SIZE; i++) {
        if (page_table[i].page_number == page_number && page_table[i].valid_bit) {
            return page_table[i].frame_number;
        }
    }

    return -1;
}

int main() {
    tlb_hits = 0;
    page_faults = 0;
    int total_accesses = 0;

    initializeTLB();
    initializePageTable();
    initializeMemory();
    next_free_frame = 0;

    FILE *address_file = fopen(PATH_ADDRESS, "r");
    FILE *disk_file = fopen(DISK_ADDRESS, "rb");
    if (!address_file || !disk_file) {
        perror("Error opening file");
        exit(EXIT_FAILURE);
    }

    char line[PAGE_SIZE];
    while (fgets(line, sizeof(line), address_file)) {
        int logical_address = atoi(line);
        int offset = logical_address & 0xFF;
        int page_number = logical_address >> 8;

        int frame_number = findFrameNumber(page_number);
        if (frame_number == -1) {
            if (loadPage(page_number, disk_file) == -1) {
                perror("Error reading from disk");
                continue;
            }
            frame_number = next_free_frame - 1;
            page_faults++;
        }
        updateTLB(page_number, frame_number);

        int physical_address = (frame_number << 8) | offset;
        int value = memory[frame_number][offset];

        printf("Virtual address: %d Physical address: %d Value: %d\n", logical_address, physical_address, value);
        total_accesses++;
    }

    printf("Page Fault Rate: %.1f%%\n", (float)page_faults / total_accesses * 100);
    printf("TLB Hit Rate: %.1f%%\n", (float)tlb_hits / total_accesses * 100);

    fclose(address_file);
    fclose(disk_file);
    return 0;
}
