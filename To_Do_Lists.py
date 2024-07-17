

import sys

tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(task_number):
    try:
        task = tasks.pop(task_number - 1)
        print(f"Task '{task}' removed.")
    except IndexError:
        print("Invalid task number.")

def update_task(task_number, new_task):
    try:
        tasks[task_number - 1] = new_task
        print(f"Task {task_number} updated to '{new_task}'.")
    except IndexError:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Update task")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            show_tasks()
        elif choice == '2':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '3':
            show_tasks()
            try:
                task_number = int(input("Enter task number to remove: "))
                remove_task(task_number)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '4':
            show_tasks()
            try:
                task_number = int(input("Enter task number to update: "))
                new_task = input("Enter new task: ")
                update_task(task_number, new_task)
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting...")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
