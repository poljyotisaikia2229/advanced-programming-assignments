#include <stdio.h>
#include <time.h>

#define MAX 5000

void constantTime(int arr[]) {
    int x = arr[0];
}

void linearTime(int arr[], int n) {
    int sum = 0;

    for (int i = 0; i < n; i++) {
        sum += arr[i];
    }
}

void quadraticTime(int arr[], int n) {
    int count = 0;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            count++;
        }
    }
}

int main() {

    int arr[MAX];

    for (int i = 0; i < MAX; i++) {
        arr[i] = i;
    }

    clock_t start, end;

    printf("Input Size\tO(1)\t\tO(n)\t\tO(n^2)\n");

    for (int n = 500; n <= MAX; n += 500) {

        start = clock();
        constantTime(arr);
        end = clock();
        double constant_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        start = clock();
        linearTime(arr, n);
        end = clock();
        double linear_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        start = clock();
        quadraticTime(arr, n);
        end = clock();
        double quadratic_time =
            ((double)(end - start)) / CLOCKS_PER_SEC;

        printf("%d\t\t%f\t%f\t%f\n",
               n,
               constant_time,
               linear_time,
               quadratic_time);
    }

    return 0;
}