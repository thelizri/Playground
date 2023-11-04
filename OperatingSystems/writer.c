// C Program for Message Queue (Writer Process)
#include <stdio.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <stdlib.h>
#define MAX 10

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
    FILE *file;

    // ftok to generate unique key
    key = ftok("/mnt/c/Users/karlw/Documents/Code/Playground/OperatingSystems/File.txt", 123);
    if (key == -1)
    {
        perror("ftok");
        exit(EXIT_FAILURE);
    }

    // msgget creates a message queue
    // and returns identifier
    msgid = msgget(key, 0666 | IPC_CREAT);
    if (msgid == -1)
    {
        perror("msgget");
        exit(EXIT_FAILURE);
    }
    message.type = 1;

    // Read content of File.txt into message
    file = fopen("/mnt/c/Users/karlw/Documents/Code/Playground/OperatingSystems/File.txt", "r");
    if (file == NULL)
    {
        perror("fopen");
        exit(EXIT_FAILURE);
    }

    // Read the entire content of the file at once
    fread(message.text, sizeof(message.text), 1, file);

    // Send the message
    if (msgsnd(msgid, &message, sizeof(message), 0) == -1)
    {
        perror("msgsnd");
        exit(EXIT_FAILURE);
    }

    // Close the file
    fclose(file);

    return EXIT_SUCCESS;
}