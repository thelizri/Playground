#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>

int main() {
    int shmid;
    int *shared_memory;

    // Get the ID of the existing shared memory segment with key 2345
    shmid = shmget((key_t)2345, sizeof(int), 0666);
    if (shmid == -1) {
        perror("shmget failed");
        exit(EXIT_FAILURE);
    }
    printf("Key of shared memory is %d\n", shmid);

    // Attach the shared memory segment to the process
    shared_memory = (int *)shmat(shmid, NULL, 0);
    if (shared_memory == (void *)-1) {
        perror("shmat failed");
        exit(EXIT_FAILURE);
    }
    printf("Process attached at %p\n", (void *)shared_memory);

    // Read the integer from the shared memory
    printf("Data read from shared memory is : %d\n", *shared_memory);

    // Detach from the shared memory segment
    if (shmdt(shared_memory) == -1) {
        perror("shmdt failed");
        exit(EXIT_FAILURE);
    }

    return 0;
}