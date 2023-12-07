#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <unistd.h>

int buffer = 0;
pthread_mutex_t lock;

void* thread_func(void *arg) {
    int *no_accesses = malloc(sizeof(int)); // Dynamically allocate memory for the counter
    *no_accesses = 0;
    while (1) {
        pthread_mutex_lock(&lock);
        if (buffer >= 15) {
            pthread_mutex_unlock(&lock);
            break;
        }
        printf("TID: %ld, PID: %d, buffer: %d\n", (long)pthread_self(), getpid(), buffer++);
        (*no_accesses)++;
        pthread_mutex_unlock(&lock);
    }

    return no_accesses; // Return the pointer
}

int main(void) {
    pthread_t t1, t2, t3;
    int *result1, *result2, *result3;

    pthread_mutex_init(&lock, NULL);

    pthread_create(&t1, NULL, &thread_func, NULL);
    pthread_create(&t2, NULL, &thread_func, NULL);
    pthread_create(&t3, NULL, &thread_func, NULL);

    pthread_join(t1, (void**)&result1);
    pthread_join(t2, (void**)&result2);
    pthread_join(t3, (void**)&result3);

    printf("TID %ld worked on the buffer %d times\n", (long)t1, *result1);
    printf("TID %ld worked on the buffer %d times\n", (long)t2, *result2);
    printf("TID %ld worked on the buffer %d times\n", (long)t3, *result3);

    int total = *result1 + *result2 + *result3;
    printf("Total buffer accesses %d\n", total);

    // Free the dynamically allocated memory
    free(result1);
    free(result2);
    free(result3);

    pthread_mutex_destroy(&lock);

    return 0;
}
