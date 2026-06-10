#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <semaphore.h>
#include <unistd.h>

#define BUFFER_SIZE 5
#define NUM_ITEMS 10

int buffer[BUFFER_SIZE];
int in = 0;
int out = 0;

sem_t empty;
sem_t full;

pthread_mutex_t mutex;

void* producer(void* arg)
{
    int item;
    int id = *((int*)arg);

    for (int i = 0; i < NUM_ITEMS; i++)
    {
        item = rand() % 100;

        sem_wait(&empty);

        pthread_mutex_lock(&mutex);

        buffer[in] = item;

        printf("Producer %d produced item %d at position %d\n",
               id, item, in);

        in = (in + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex);

        sem_post(&full);

        sleep(1);
    }

    pthread_exit(NULL);
}

void* consumer(void* arg)
{
    int item;
    int id = *((int*)arg);

    for (int i = 0; i < NUM_ITEMS; i++)
    {
        sem_wait(&full);

        pthread_mutex_lock(&mutex);

        item = buffer[out];

        printf("Consumer %d consumed item %d from position %d\n",
               id, item, out);

        out = (out + 1) % BUFFER_SIZE;

        pthread_mutex_unlock(&mutex);

        sem_post(&empty);

        sleep(2);
    }

    pthread_exit(NULL);
}

int main()
{
    pthread_t prod1, prod2, cons1, cons2;

    int p1 = 1, p2 = 2;
    int c1 = 1, c2 = 2;

    sem_init(&empty, 0, BUFFER_SIZE);
    sem_init(&full, 0, 0);

    pthread_mutex_init(&mutex, NULL);

    pthread_create(&prod1, NULL, producer, &p1);
    pthread_create(&prod2, NULL, producer, &p2);

    pthread_create(&cons1, NULL, consumer, &c1);
    pthread_create(&cons2, NULL, consumer, &c2);

    pthread_join(prod1, NULL);
    pthread_join(prod2, NULL);

    pthread_join(cons1, NULL);
    pthread_join(cons2, NULL);

    sem_destroy(&empty);
    sem_destroy(&full);

    pthread_mutex_destroy(&mutex);

    printf("\nAll threads finished execution.\n");

    return 0;
}