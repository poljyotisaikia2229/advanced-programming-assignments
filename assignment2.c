#include <stdio.h>
#include <string.h>

#define MAX 100

struct Product {
    char name[30];
    int stock;
};

struct Product products[MAX];
int count = 0;

void insertProduct(char name[], int stock) {
    strcpy(products[count].name, name);
    products[count].stock = stock;
    count++;
}

void searchProduct(char name[]) {
    int found = 0;

    for (int i = 0; i < count; i++) {
        if (strcmp(products[i].name, name) == 0) {
            printf("Product Found: %s | Stock: %d\n",
                   products[i].name,
                   products[i].stock);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("Product not found\n");
    }
}

void displayLowStock() {

    printf("\nProducts with stock less than 10:\n");

    for (int i = 0; i < count; i++) {
        if (products[i].stock < 10) {
            printf("%s - Stock: %d\n",
                   products[i].name,
                   products[i].stock);
        }
    }
}

int main() {

    insertProduct("Laptop", 15);
    insertProduct("Mouse", 8);
    insertProduct("Keyboard", 5);
    insertProduct("Monitor", 12);
    insertProduct("Printer", 3);

    searchProduct("Mouse");

    displayLowStock();

    return 0;
}