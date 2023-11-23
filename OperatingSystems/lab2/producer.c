#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/shm.h>
#include <string.h>
#include <sys/types.h>
#include <semaphore.h>
#include <stdbool.h>
#include <sys/mman.h>
#include <fcntl.h>
#include <sys/wait.h>

const int MAX = 2;

sem_t *rw_mutex;
sem_t *mutex;

int *VAR;

void reader_function()
{
    int read_count = 0;
    pid_t pid = getpid(); // Gets the current process's PID
    do
    {
        sem_wait(mutex);
        read_count++;
        if (read_count == 1)
            sem_wait(rw_mutex);
        sem_post(mutex);

        /* reading is performed */
        printf("The reader (%d) reads the value %d\n", pid, *VAR);

        sem_wait(mutex);
        read_count--;
        if (read_count == 0)
            sem_post(rw_mutex);
        sem_post(mutex);

    } while (*VAR < MAX);
}

void writer_function()
{
    pid_t pid = getpid(); // Gets the current process's PID
    do
    {
        sem_wait(rw_mutex);
        printf("The writer aquires the lock\n");

        /* writing is performed */
        (*VAR)++;
        printf("The writer (%d) writes the value %d\n", pid, *VAR);

        printf("The writer releases the lock\n");
        sem_post(rw_mutex);

    } while (*VAR < MAX);
}

int main()
{
    int shmid;

    // Create shared memory segment with key 2345
    shmid = shmget((key_t)2345, sizeof(int), 0666 | IPC_CREAT);
    if (shmid == -1)
    {
        perror("shmget failed");
        exit(EXIT_FAILURE);
    }

    // Attach process to shared memory segment
    VAR = (int *)shmat(shmid, NULL, 0);
    if (VAR == (void *)-1)
    {
        perror("shmat failed");
        exit(EXIT_FAILURE);
    }

    // Initialize shared integer
    *VAR = 0;

    // Initialize semaphores
    rw_mutex = sem_open("/rw_mutex", O_CREAT, 0644, 1);
    mutex = sem_open("/mutex", O_CREAT, 0644, 1);

    pid_t pid = fork(); // Create a new process

    if (pid == -1)
    {
        // An error occurred during fork()
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0)
    {
        // This branch is executed by the child process
        // The child process will execute the writing function
        writer_function();
    }
    else
    {
        // This branch is executed by the parent process
        // This branch will create two threads and execute the reading function
        pid_t readers = fork();

        if (readers == 0)
        {
            // Child process
            reader_function();
        }
        else
        {
            reader_function();
            waitpid(readers, NULL, 0);
            waitpid(pid, NULL, 0);

            // Close named semaphores
            sem_close(rw_mutex);
            sem_close(mutex);

            // Unlink named semaphores
            sem_unlink("/rw_mutex");
            sem_unlink("/mutex");
        }
    }

    // Detach from shared memory (it's a good practice to detach after use)
    if (shmdt(VAR) == -1)
    {
        perror("shmdt failed");
        exit(EXIT_FAILURE);
    }

    return 0;
}
