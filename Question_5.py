from collections import deque

queue = deque()

def enqueue():
    try:
        value = int(input("Enter the value to insert: "))
        queue.append(value)
        print(value, "inserted into queue")
    except ValueError:
        print("Invalid input. Please enter an integer.")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        value = queue.popleft()
        print("Deleted element:", value)

def display():
    if not queue:
        print("Queue is empty")
    else:
        print("Queue elements:", list(queue))

while True:
    print("\nQUEUE OPERATIONS")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 4.")
        continue

    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Program ended")
        break
    else:
        print("Invalid choice")