#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <sys/wait.h>
#include <ctype.h>
#include <stdbool.h>

// Count words
int countWords(char *str)
{
    int wordCount = 0;
    bool inWord = false;

    while (*str)
    {
        if (isspace((unsigned char)*str))
        {
            inWord = false;
        }
        else if (!inWord)
        {
            inWord = true;
            ++wordCount;
        }
        ++str;
    }

    return wordCount;
}

// Define the message structure
struct msg_buffer
{
    long msg_type;
    char msg_text[300];
} message;

int main()
{
    key_t key;
    int msgid;
    FILE *file;

    // Generate a unique key
    key = ftok("/mnt/c/Users/karlw/Documents/Code/Playground/OperatingSystems/File.txt", 123);
    if (key == -1)
    {
        perror("ftok");
        exit(EXIT_FAILURE);
    }

    // Create a message queue
    msgid = msgget(key, 0666 | IPC_CREAT);
    if (msgid == -1)
    {
        perror("msgget");
        exit(EXIT_FAILURE);
    }

    // Create a new process
    pid_t pid = fork(); // Create a new process

    if (pid == -1)
    {
        // An error occurred during fork()
        perror("fork");
        exit(EXIT_FAILURE);
    }

    if (pid == 0)
    {
        // Child process
        message.msg_type = 1;

        // Read content of File.txt into message
        file = fopen("/mnt/c/Users/karlw/Documents/Code/Playground/OperatingSystems/File.txt", "r");
        if (file == NULL)
        {
            perror("fopen");
            exit(EXIT_FAILURE);
        }

        // Read the entire content of the file at once
        fread(message.msg_text, sizeof(message.msg_text), 1, file);

        // Send the message
        if (msgsnd(msgid, &message, sizeof(message), 0) == -1)
        {
            perror("msgsnd");
            exit(EXIT_FAILURE);
        }

        // Close the file
        fclose(file);
        exit(EXIT_SUCCESS);
    }
    else
    {
        // Parent process
        // Wait for child process to complete
        wait(NULL);

        // Receive the message
        if (msgrcv(msgid, &message, sizeof(message), message.msg_type, 0) == -1)
        {
            perror("msgrcv");
            exit(EXIT_FAILURE);
        }
        printf("Data Received is :\n %s\n", message.msg_text);

        // Count the number of words
        int words = countWords(message.msg_text);
        printf("Number of words is: %d\n", words);

        // Destroy the message queue
        if (msgctl(msgid, IPC_RMID, NULL) == -1)
        {
            perror("msgctl");
            exit(EXIT_FAILURE);
        }
    }

    return EXIT_SUCCESS;
}
