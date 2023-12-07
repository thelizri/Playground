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
        printf("%d ", requests[i]);
    }

    // Call each scheduling function
    /*
    fcfs(requests, head);
    sstf(requests, head);
    scan(requests, head);
    cscan(requests, head);
    look(requests, head);
    clook(requests, head);
    */

    printf("\nFCFS %d\n", fcfs(requests, head));
    printf("SSTF %d\n", sstf(requests, head));

    return 0;
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
int sstf(int requests[], int head)
{
    // Implement SSTF algorithm
    int travelled_distance = 0;
    int current_position = head;
    for (int j = 0; j < REQUEST_COUNT; j++)
    {
        int closest_distance = 10000; // Greater than maximum distance
        int closest_position = -1;    // Fake index
        for (int i = 0; i < REQUEST_COUNT; i++)
        {
            int distance = abs(requests[i] - current_position);
            if (requests[i] == -1)
                continue;
            else if (distance < closest_distance)
            {
                closest_distance = distance;
                closest_position = i;
            }
        }
        travelled_distance += closest_distance;
        current_position = requests[closest_position];
        requests[closest_position] = -1;
    }
    return travelled_distance;
}

// SCAN (Elevator Algorithm): This algorithm works like an elevator, moving the disk arm back and forth across the disk, servicing requests in one direction until it reaches the end,
// and then reversing direction.
int scan(int requests[], int head)
{
    // Implement SCAN algorithm
    return 0;
}

// C-SCAN (Circular SCAN): Similar to SCAN, but instead of reversing direction at the ends, it jumps back to the beginning (or the other extreme) and starts scanning in the same direction again.
int cscan(int requests[], int head)
{
    // Implement C-SCAN algorithm
    return 0;
}

// LOOK: A variant of SCAN, the LOOK algorithm moves the disk arm only as far as the last request in each direction,
// then reverses direction. This can be more efficient than SCAN, as it avoids unnecessary movement of the disk arm.
int look(int requests[], int head)
{
    // Implement LOOK algorithm
    return 0;
}
// C-LOOK (Circular LOOK)**: This is similar to C-SCAN. In C-LOOK, the disk arm goes only as far as the final request in one direction,
// then jumps back to the earliest request in the other direction. Like C-SCAN, it also tends to provide a more uniform wait time.
int clook(int requests[], int head)
{
    // Implement C-LOOK algorithm
    return 0;
}