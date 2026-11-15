
#include <stdio.h>

#define SIZE 5

int deque[SIZE];
int front = -1;
int rear = -1;

// Check whether deque is full
int isFull() {
    return (rear + 1) % SIZE == front;
}

// Check whether deque is empty
int isEmpty() {
    return front == -1;
}

// Insert element at front
void insertFront(int value) {
    if (isFull()) {
        printf("Deque is full\n");
        return;
    }

    if (isEmpty()) {
        front = rear = 0;
    } else {
        front = (front - 1 + SIZE) % SIZE;
    }

    deque[front] = value;
    printf("%d inserted at front\n", value);
}

// Insert element at rear
void insertRear(int value) {
    if (isFull()) {
        printf("Deque is full\n");
        return;
    }

    if (isEmpty()) {
        front = rear = 0;
    } else {
        rear = (rear + 1) % SIZE;
    }

    deque[rear] = value;
    printf("%d inserted at rear\n", value);
}

// Delete element from front
void deleteFront() {
    if (isEmpty()) {
        printf("Deque is empty\n");
        return;
    }

    printf("Deleted from front: %d\n", deque[front]);

    if (front == rear) {
        front = rear = -1;
    } else {
        front = (front + 1) % SIZE;
    }
}

// Delete element from rear
void deleteRear() {
    if (isEmpty()) {
        printf("Deque is empty\n");
        return;
    }

    printf("Deleted from rear: %d\n", deque[rear]);

    if (front == rear) {
        front = rear = -1;
    } else {
        rear = (rear - 1 + SIZE) % SIZE;
    }
}

// Display deque elements
void display() {
    if (isEmpty()) {
        printf("Deque is empty\n");
        return;
    }

    int i = front;

    printf("Deque elements: ");

    while (1) {
        printf("%d ", deque[i]);

        if (i == rear) {
            break;
        }

        i = (i + 1) % SIZE;
    }

    printf("\n");
}

int main() {
    insertRear(10);
    insertRear(20);
    insertFront(5);

    display();

    deleteFront();
    deleteRear();

    display();

    return 0;
}
