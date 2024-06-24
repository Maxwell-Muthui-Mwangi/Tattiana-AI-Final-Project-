import tkinter as tk
from tkinter import messagebox
import os
import json

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
        json.dump(tasks, file)

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

# Tkinter GUI class
class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("To-Do List")
        self.geometry("400x300")

        self.tasks = load_tasks()

        self.create_widgets()
        self.display_tasks()

    def create_widgets(self):
        self.task_listbox = tk.Listbox(self, width=50, height=15)
        self.task_listbox.pack()

        self.entry = tk.Entry(self, width=50)
        self.entry.pack()

        self.add_button = tk.Button(self, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.update_button = tk.Button(self, text="Update Task", command=self.update_task)
        self.update_button.pack()

        self.delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

        self.complete_button = tk.Button(self, text="Mark as Completed", command=self.complete_task)
        self.complete_button.pack()

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks):
            status = "Done" if task['completed'] else "Not Done"
            self.task_listbox.insert(tk.END, f"{i+1}. {task['task']} - {status}")

    def add_task(self):
        task = self.entry.get()
        if task:
            add_task(self.tasks, task)
            self.display_tasks()
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Task cannot be empty!")

    def update_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            new_task = self.entry.get()
            if new_task:
                update_task(self.tasks, task_index[0], new_task)
                self.display_tasks()
                self.entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")
        else:
            messagebox.showwarning("Warning", "Select a task to update!")

    def delete_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            delete_task(self.tasks, task_index[0])
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Select a task to delete!")

    def complete_task(self):
        task_index = self.task_listbox.curselection()
        if task_index:
            complete_task(self.tasks, task_index[0])
            self.display_tasks()
        else:
            messagebox.showwarning("Warning", "Select a task to mark as completed!")

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
