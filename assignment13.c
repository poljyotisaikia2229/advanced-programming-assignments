#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Structure for Dynamic String Buffer */
typedef struct {
    char *data;
    size_t length;
    size_t capacity;
} StringBuffer;

/* Initialize StringBuffer */
StringBuffer *sb_init(size_t initial_capacity) {

    /* Allocate memory for struct */
    StringBuffer *sb = (StringBuffer *)malloc(sizeof(StringBuffer));

    if (sb == NULL) {
        printf("Memory allocation failed for StringBuffer\n");
        return NULL;
    }

    /* Allocate memory for character buffer */
    sb->data = (char *)malloc(initial_capacity);

    if (sb->data == NULL) {
        printf("Memory allocation failed for data buffer\n");
        free(sb);
        return NULL;
    }

    sb->length = 0;
    sb->capacity = initial_capacity;

    /* Initialize as empty string */
    sb->data[0] = '\0';

    return sb;
}

/* Append string to buffer */
void sb_append(StringBuffer *sb, const char *str) {

    if (sb == NULL || str == NULL) {
        return;
    }

    size_t str_len = strlen(str);

    /* Resize buffer if needed */
    while (sb->length + str_len + 1 > sb->capacity) {

        size_t new_capacity = sb->capacity * 2;

        /* Safe realloc using temporary pointer */
        char *temp = (char *)realloc(sb->data, new_capacity);

        if (temp == NULL) {
            printf("Reallocation failed\n");
            return;
        }

        sb->data = temp;
        sb->capacity = new_capacity;

        printf("Buffer resized to capacity: %zu\n", sb->capacity);
    }

    /* Append new string */
    strcpy(sb->data + sb->length, str);

    /* Update length */
    sb->length += str_len;
}

/* Destructor function */
void sb_free(StringBuffer *sb) {

    if (sb != NULL) {

        /* Free internal data buffer */
        free(sb->data);

        /* Free structure */
        free(sb);
    }
}

/* Main function */
int main() {

    char input[100];

    /* Initialize buffer */
    StringBuffer *sb = sb_init(8);

    if (sb == NULL) {
        return 1;
    }

    printf("Initial Capacity: %zu\n", sb->capacity);

    printf("Enter strings (type 'exit' to stop):\n");

    while (1) {

        printf("> ");

        fgets(input, sizeof(input), stdin);

        /* Remove newline character */
        input[strcspn(input, "\n")] = '\0';

        /* Exit condition */
        if (strcmp(input, "exit") == 0) {
            break;
        }

        /* Append user input */
        sb_append(sb, input);

        /* Append space after each word */
        sb_append(sb, " ");

        printf("Current Buffer: %s\n", sb->data);
    }

    printf("\nFinal String: %s\n", sb->data);
    printf("Final Length: %zu\n", sb->length);
    printf("Final Capacity: %zu\n", sb->capacity);

    /* Free all memory */
    sb_free(sb);

    printf("Memory freed successfully\n");

    return 0;
}