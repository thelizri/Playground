#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

void *thread_func(void *number) {
    int num = *((int *)number); // Dereference the pointer to read the value
    printf("Hello this is thread: %d\n", num);
    free(number); // Don't forget to free the heap memory
    return NULL;
}

int main(void) {
    pthread_t thread;
    int rc;

    for (int i = 0; i < 20; i++) {
        int *pointer = malloc(sizeof(int)); // Allocate memory on the heap
        if (pointer == NULL) {
            perror("Failed to allocate memory\n");
            exit(EXIT_FAILURE);
        }
        *pointer = i; // Copy the value of 'i' into allocated memory

        rc = pthread_create(&thread, NULL, thread_func, (void *)pointer);
        if (rc != 0) {
            perror("Failed to create thread\n");
            free(pointer); // Clean up memory if thread creation fails
            exit(EXIT_FAILURE);
        }

        // Detach the newly created thread
        rc = pthread_detach(thread);
        if (rc != 0) {
            perror("Failed to detach thread\n");
            free(pointer); // Clean up memory if detaching fails
            // It may be unsafe to continue if we can't detach a thread, you might want to handle this differently
        }
    }

    // Allow some time for threads to complete before main exits
    sleep(1); // This is not the best way to handle this. Consider using pthread_join in a real application

    return 0;
}
