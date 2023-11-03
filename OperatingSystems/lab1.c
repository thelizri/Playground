#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main()
{
    int pipe_fd[2];
    pid_t pid;

    // Create a pipe
    if (pipe(pipe_fd) == -1)
    {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    pid = fork(); // Create a new process

    if (pid == -1)
    {
        // An error occurred during fork()
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0)
    {
        // This branch is executed by the child process

        // Close the read end of the pipe in the child
        close(pipe_fd[0]);

        // Redirect stdout to the write end of the pipe
        if (dup2(pipe_fd[1], STDOUT_FILENO) == -1)
        {
            perror("dup2");
            exit(EXIT_FAILURE);
        }

        // Execute ls /
        char *args[] = {"ls", "/", NULL};
        execvp("ls", args); // Using execvp instead of execv

        // If execvp returns, it must have failed
        perror("execvp");
        exit(EXIT_FAILURE);
    }
    else
    {
        // This branch is executed by the parent process

        // Close the write end of the pipe in the parent
        close(pipe_fd[1]);

        // Wait for the child to finish
        wait(NULL);

        // Redirect the read end of the pipe to stdin
        if (dup2(pipe_fd[0], STDIN_FILENO) == -1)
        {
            perror("dup2");
            exit(EXIT_FAILURE);
        }

        // Execute wc -l to count number of lines
        char *args[] = {"wc", "-l", NULL};
        execvp("wc", args); // Using execvp instead of execv

        // If execvp returns, it must have failed
        perror("execvp");
        exit(EXIT_FAILURE);
    }

    return EXIT_SUCCESS;
}
