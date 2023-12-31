// C Program for Message Queue (Reader Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdlib.h>
#include <stdbool.h>
#include <ctype.h>

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

// structure for message queue
struct mesg_buffer
{
    long type;
    char text[100];
} message;

int main()
{
    key_t key;
    int msgid;

    // ftok to generate unique key
    key = ftok("File.txt", 123);

    // msgget creates a message queue
    // and returns identifier
    msgid = msgget(key, 0666 | IPC_CREAT);
    if (msgid == -1)
    {
        perror("msgget");
        exit(EXIT_FAILURE);
    }
    message.type = 1;

    // Receive the message
    if (msgrcv(msgid, &message, sizeof(message), message.type, 0) == -1)
    {
        perror("msgrcv");
        exit(EXIT_FAILURE);
    }

    // Count the number of words
    int words = countWords(message.text);
    printf("Number of words is: %d\n", words);

    // Destroy the message queue
    if (msgctl(msgid, IPC_RMID, NULL) == -1)
    {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }

    return EXIT_SUCCESS;
}
