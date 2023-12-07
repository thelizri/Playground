#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define CYLINDER_COUNT 100
#define REQUEST_COUNT 5

int fcfs(int requests[], int head);
int sstf(int requests[], int head);
int scan(int requests[], int head);
int cscan(int requests[], int head);
int look(int requests[], int head);
int clook(int requests[], int head);
int compareInts(const void *a, const void *b);
void printArray(int array[], int arraySize);
void copyArray(int original[], int copy[], int arraySize);

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: %s <initial head position>\n", argv[0]);
        return 1;
    }

    int head = atoi(argv[1]);
    if (head < 0 || head >= CYLINDER_COUNT)
    {
        printf("Invalid initial head position.\n");
        return 1;
    }

    int requests[REQUEST_COUNT];

    // Generate random requests
    for (int i = 0; i < REQUEST_COUNT; i++)
    {
        requests[i] = rand() % CYLINDER_COUNT;
    }

    printArray(requests, REQUEST_COUNT);

    int sorted_copy[REQUEST_COUNT];
    copyArray(requests, sorted_copy, REQUEST_COUNT);
    qsort(sorted_copy, REQUEST_COUNT, sizeof(int), compareInts);
    printArray(sorted_copy, REQUEST_COUNT);

    // Call each scheduling function
    printf("\nFCFS %d\n", fcfs(requests, head));
    printf("SSTF %d\n", sstf(requests, head));
    printf("SCAN %d\n", scan(requests, head));
    printf("C-SCAN %d\n", cscan(requests, head));
    printf("LOOK %d\n", look(requests, head));
    printf("C-LOOK %d\n", clook(requests, head));
    return 0;
}

// Helper function
int compareInts(const void *a, const void *b)
{
    return (*(int *)a - *(int *)b);
}

void copyArray(int original[], int copy[], int arraySize)
{
    for (int i = 0; i < arraySize; i++)
    {
        copy[i] = original[i];
    }
}

void printArray(int array[], int arraySize)
{
    printf("\n");
    for (int i = 0; i < arraySize; i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
}

// FCFS (First Come First Served): This is the simplest type of disk scheduling algorithm. In FCFS, the disk requests are addressed in the order they are received.
int fcfs(int requests[], int head)
{
    // Implement FCFS algorithm
    int distance = abs(requests[0] - head);
    for (int i = 1; i < REQUEST_COUNT; i++)
    {
        distance += abs(requests[i - 1] - requests[i]);
    }
    return distance;
}

// SSTF (Shortest Seek Time First): SSTF is a more optimized approach than FCFS. Here, the disk head moves to the request that is closest to its current position.
int sstf(int original[], int head)
{
    // Implement SSTF algorithm
    int requests[REQUEST_COUNT];
    copyArray(original, requests, REQUEST_COUNT);

    int travelled_distance = 0;
    int current_position = head;
    for (int j = 0; j < REQUEST_COUNT; j++)
    {
        int closest_distance = 10000;       // Greater than maximum distance
        int index_of_closest_position = -1; // Fake index
        for (int i = 0; i < REQUEST_COUNT; i++)
        {
            int distance = abs(requests[i] - current_position);
            if (requests[i] == -1)
                continue;
            else if (distance < closest_distance)
            {
                closest_distance = distance;
                index_of_closest_position = i;
            }
        }
        travelled_distance += closest_distance;
        current_position = requests[index_of_closest_position];
        requests[index_of_closest_position] = -1;
    }
    return travelled_distance;
}

// SCAN (Elevator Algorithm): This algorithm works like an elevator, moving the disk arm back and forth across the disk, servicing requests in one direction until it reaches the end,
// and then reversing direction.
int scan(int original[], int head)
{
    int requests[REQUEST_COUNT];
    copyArray(original, requests, REQUEST_COUNT);
    qsort(requests, REQUEST_COUNT, sizeof(int), compareInts);

    if (requests[0] >= head)
    {
        // All the requests are on the right side of the head
        return requests[REQUEST_COUNT - 1] - head;
    }
    else
    {
        return (CYLINDER_COUNT - requests[0]) + (CYLINDER_COUNT - head);
    }

    return 0;
}

// C-SCAN (Circular SCAN): Similar to SCAN, but instead of reversing direction at the ends, it jumps back to the beginning (or the other extreme) and starts scanning in the same direction again.
int cscan(int original[], int head)
{
    int requests[REQUEST_COUNT];
    copyArray(original, requests, REQUEST_COUNT);
    qsort(requests, REQUEST_COUNT, sizeof(int), compareInts);

    if (requests[0] >= head)
    {
        // All the requests are on the right side of the head
        return requests[REQUEST_COUNT - 1] - head;
    }
    else if (requests[REQUEST_COUNT - 1] <= head)
    {
        // All the requests are on the left side of the head
        return requests[REQUEST_COUNT - 1] + CYLINDER_COUNT + (CYLINDER_COUNT - head);
    }
    else
    {
        for (int i = 0; i < REQUEST_COUNT; i++)
        {
            if (requests[i] >= head)
                return requests[i - 1] + CYLINDER_COUNT + (CYLINDER_COUNT - head);
        }
    }

    return 0;
}

// LOOK: A variant of SCAN, the LOOK algorithm moves the disk arm only as far as the last request in each direction,
// then reverses direction. This can be more efficient than SCAN, as it avoids unnecessary movement of the disk arm.
int look(int original[], int head)
{
    // Implement LOOK algorithm
    int requests[REQUEST_COUNT];
    copyArray(original, requests, REQUEST_COUNT);
    qsort(requests, REQUEST_COUNT, sizeof(int), compareInts);

    if (requests[0] >= head)
    {
        // All the requests are on the right side of the head
        return requests[REQUEST_COUNT - 1] - head;
    }
    else if(requests[REQUEST_COUNT-1] <= head){
        // All the requests are on the left side of the head
        return head - requests[0];
    }
    else
    {
        return (requests[REQUEST_COUNT - 1] - requests[0]) + (requests[REQUEST_COUNT - 1] - head);
    }

    return 0;
}
// C-LOOK (Circular LOOK)**: This is similar to C-SCAN. In C-LOOK, the disk arm goes only as far as the final request in one direction,
// then jumps back to the earliest request in the other direction. Like C-SCAN, it also tends to provide a more uniform wait time.
int clook(int original[], int head)
{
    // Implement C-LOOK algorithm
    int requests[REQUEST_COUNT];
    copyArray(original, requests, REQUEST_COUNT);
    qsort(requests, REQUEST_COUNT, sizeof(int), compareInts);

    if (requests[0] >= head)
    {
        // All the requests are on the right side of the head
        return requests[REQUEST_COUNT - 1] - head;
    }
    else if (requests[REQUEST_COUNT - 1] <= head)
    {
        // All the requests are on the left side of the head
        return (head - requests[0]) + (requests[REQUEST_COUNT - 1] - requests[0]);
    }
    else
    {
        for (int i = 0; i < REQUEST_COUNT; i++)
        {
            if (requests[i] >= head)
            {
                if (i > 1)
                {
                    return (requests[REQUEST_COUNT - 1] - head) + (requests[REQUEST_COUNT - 1] - requests[0] + requests[i - 1]);
                }
                else
                {
                    return (requests[REQUEST_COUNT - 1] - head) + (requests[REQUEST_COUNT - 1] - requests[0]);
                }
            }
        }
    }

    return 0;
}