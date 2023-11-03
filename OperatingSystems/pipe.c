#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>

int main()
{
    int fd[2]; // 0  = read end, 1 = write end
    pid_t child_pid;
    char buf;
    char *message = "Hello, pipe!";

    if (pipe(fd) == -1)
    {
        perror("pipe");
        exit(EXIT_FAILURE);
    }

    child_pid = fork();
    if (child_pid == -1)
    {
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (child_pid == 0)
    {                 // Child process
        close(fd[0]); // Close unused read end
        write(fd[1], message, strlen(message));
        close(fd[1]); // Close write end
        exit(EXIT_SUCCESS);
    }
    else
    { // Parent process
        wait(NULL);
        close(fd[1]); // Close unused write end
        while (read(fd[0], &buf, 1) > 0)
        {
            write(STDOUT_FILENO, &buf, 1);
        }
        close(fd[0]); // Close read end
        exit(EXIT_SUCCESS);
    }
}
