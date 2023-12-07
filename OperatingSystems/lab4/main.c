#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CYLINDER_COUNT 5000
#define REQUEST_COUNT 1000

void fcfs(int requests[], int head);
void sstf(int requests[], int head);
void scan(int requests[], int head);
void cscan(int requests[], int head);
void look(int requests[], int head);
void clook(int requests[], int head);

int main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Usage: %s <initial head position>\n", argv[0]);
        return 1;
    }

    int head = atoi(argv[1]);
    if (head < 0 || head >= CYLINDER_COUNT) {
        printf("Invalid initial head position.\n");
        return 1;
    }

    int requests[REQUEST_COUNT];
    int hard_disk[CYLINDER_COUNT];

    // Generate random requests
    for (int i = 0; i < REQUEST_COUNT; i++) {
        requests[i] = rand() % CYLINDER_COUNT;
    }

    //Initialize hard disk
    for (int i = 0; i < CYLINDER_COUNT; i++){
        hard_disk[i] = i;
    }

    for(int loop = 0; loop < head; loop++)
      printf("%d ", hard_disk[loop]);

    // Call each scheduling function
    /*
    fcfs(requests, head);
    sstf(requests, head);
    scan(requests, head);
    cscan(requests, head);
    look(requests, head);
    clook(requests, head);
    */

    return 0;
}

void fcfs(int requests[], int head) {
    // Implement FCFS algorithm
}

void sstf(int requests[], int head) {
    // Implement SSTF algorithm
}

void scan(int requests[], int head) {
    // Implement SCAN algorithm
}

void cscan(int requests[], int head) {
    // Implement C-SCAN algorithm
}

void look(int requests[], int head) {
    // Implement LOOK algorithm
}

void clook(int requests[], int head) {
    // Implement C-LOOK algorithm
}
