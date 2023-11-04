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
    long mesg_type;
    char mesg_text[100];
} message;

int main()
{
    key_t key;
    int msgid;

    // ftok to generate unique key
    key = ftok("/mnt/c/Users/karlw/Documents/Code/Playground/OperatingSystems/File.txt", 123);

    // msgget creates a message queue
    // and returns identifier
    msgid = msgget(key, 0666 | IPC_CREAT);

    // Receive the message
    if (msgrcv(msgid, &message, sizeof(message), message.mesg_type, 0) == -1)
    {
        perror("msgrcv");
        exit(EXIT_FAILURE);
    }

    // Count the number of words
    int words = countWords(message.mesg_text);
    printf("Number of words is: %d\n", words);

    // Destroy the message queue
    if (msgctl(msgid, IPC_RMID, NULL) == -1)
    {
        perror("msgctl");
        exit(EXIT_FAILURE);
    }

    return EXIT_SUCCESS;
}
