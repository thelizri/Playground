#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int main()
{
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
        char *args[] = {"/bin/windlass", NULL};
        if (execv("/bin/windlass", args) == -1)
        {
            perror("execv");
            exit(1);
        }
    }
    else
    {
        // This branch is executed by the parent process
        printf("I am the parent of pid = %d!\n", pid);
    }

    return EXIT_SUCCESS;
}
