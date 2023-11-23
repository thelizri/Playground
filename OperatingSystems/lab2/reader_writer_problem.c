#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <sys/types.h>
#include <semaphore.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <sys/wait.h>

const int MAX = 2;

sem_t *rw_mutex;
sem_t *mutex;

typedef struct {
    int VAR;
    int read_count;
} SharedData;

SharedData *shared_data;

void reader_function() {

    pid_t pid = getpid();

    do {
        sem_wait(mutex);
        shared_data->read_count++;
        if (shared_data->read_count == 1) {
            sem_wait(rw_mutex);
            printf("First reader aquired lock\n");
        }
        sem_post(mutex);

        // Perform reading
        printf("The reader (%d) reads the value: %d\n", pid, shared_data->VAR);

        sem_wait(mutex);
        shared_data->read_count--;
        if (shared_data->read_count == 0) {
            sem_post(rw_mutex);
            printf("Last reader released lock\n");
        }
        sem_post(mutex);
    } while (shared_data->VAR < MAX);
}

void writer_function() {

    pid_t pid = getpid();

    do {
        sem_wait(rw_mutex);
        printf("The writer aquired the lock\n");

        // Perform writing
        shared_data->VAR++;
        printf("The writer (%d) writes the value: %d\n", pid, shared_data->VAR);

        sem_post(rw_mutex);
        printf("The writer released the lock\n");
    } while (shared_data->VAR < MAX);
}

int main() {
    int shmid = shmget((key_t)2345, sizeof(SharedData), 0666 | IPC_CREAT);
    shared_data = (SharedData *)shmat(shmid, NULL, 0);
    shared_data->VAR = 0;
    shared_data->read_count = 0;

    rw_mutex = sem_open("/rw_mutex", O_CREAT, 0666, 1);
    mutex = sem_open("/mutex", O_CREAT, 0666, 1);

    pid_t pid = fork();
    if (pid == 0) {
        writer_function();
    } else {
        pid_t pid2 = fork();
        if (pid2 == 0) {
            printf("First reader(%d)\n", getpid());
            reader_function();
        } else {
            printf("Second reader(%d)\n", getpid());
            reader_function();
            waitpid(pid, NULL, 0);
            waitpid(pid2, NULL, 0);
        }
    }

    shmdt(shared_data);
    sem_close(rw_mutex);
    sem_close(mutex);
    sem_unlink("/rw_mutex");
    sem_unlink("/mutex");

    return 0;
}
