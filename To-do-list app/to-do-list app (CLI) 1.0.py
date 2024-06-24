import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task(tasks, task):
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)

# Update an existing task
def update_task(tasks, task_index, new_task):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['task'] = new_task
        save_tasks(tasks)

# Delete a task
def delete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)

# Mark a task as completed
def complete_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)

# Display tasks
def display_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{i+1}. {task['task']} - {status}")

# Command-line interface
def command_line_interface():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List:")
        display_tasks(tasks)
        print("\nOptions: ")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Mark task as completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter the new task: ")
            add_task(tasks, task)
        elif choice == '2':
            task_index = int(input("Enter the task number to update: ")) - 1
            new_task = input("Enter the updated task: ")
            update_task(tasks, task_index, new_task)
        elif choice == '3':
            task_index = int(input("Enter the task number to delete: ")) - 1
            delete_task(tasks, task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            complete_task(tasks, task_index)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    command_line_interface()
