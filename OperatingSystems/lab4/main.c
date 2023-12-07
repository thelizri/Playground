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

//FCFS (First Come First Served): This is the simplest type of disk scheduling algorithm. In FCFS, the disk requests are addressed in the order they are received. 
void fcfs(int requests[], int head) {
    // Implement FCFS algorithm
}

//SSTF (Shortest Seek Time First): SSTF is a more optimized approach than FCFS. Here, the disk head moves to the request that is closest to its current position.
void sstf(int requests[], int head) {
    // Implement SSTF algorithm
}

// SCAN (Elevator Algorithm): This algorithm works like an elevator, moving the disk arm back and forth across the disk, servicing requests in one direction until it reaches the end, 
// and then reversing direction.
void scan(int requests[], int head) {
    // Implement SCAN algorithm
}

// C-SCAN (Circular SCAN): Similar to SCAN, but instead of reversing direction at the ends, it jumps back to the beginning (or the other extreme) and starts scanning in the same direction again.
void cscan(int requests[], int head) {
    // Implement C-SCAN algorithm
}

// LOOK: A variant of SCAN, the LOOK algorithm moves the disk arm only as far as the last request in each direction,
// then reverses direction. This can be more efficient than SCAN, as it avoids unnecessary movement of the disk arm.
void look(int requests[], int head) {
    // Implement LOOK algorithm
}
// C-LOOK (Circular LOOK)**: This is similar to C-SCAN. In C-LOOK, the disk arm goes only as far as the final request in one direction,
// then jumps back to the earliest request in the other direction. Like C-SCAN, it also tends to provide a more uniform wait time.
void clook(int requests[], int head) {
    // Implement C-LOOK algorithm
}