#include <stdio.h>
#include <stdlib.h>

int main()
{
    int test[5];
    for (int i = 0; i < 999; i++)
    {
        printf("Row: %d Number: %d\n", i, test[i]);
    }
    return 0;
}