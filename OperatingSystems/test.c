#include <stdio.h>
#include <stdlib.h>

int main()
{
    int size;
    printf("Enter size: ");
    if (scanf("%d", &size) != 1)
    {
        // Handle error: input was not a number
        fprintf(stderr, "Error: Invalid input. Expected an integer.\n");
        return EXIT_FAILURE;
    }

    // Allocate memory for 'size' number of characters and initialize to 0
    char *arr = (char *)calloc(size, sizeof(char));
    if (arr == NULL)
    {
        // Handle error: memory allocation failed
        fprintf(stderr, "Error: Memory allocation failed.\n");
        return EXIT_FAILURE;
    }

    // Assuming you want to read a string from the user:
    printf("Enter a string: ");
    if (scanf("%s", arr) != 1)
    {
        // Handle error: input was not a string
        fprintf(stderr, "Error: Invalid input. Expected a string.\n");
        free(arr); // Release allocated memory
        return EXIT_FAILURE;
    }

    // Print the string entered by the user
    printf("You entered: %s\n", arr);

    // Release the allocated memory
    free(arr);

    return 0;
}
