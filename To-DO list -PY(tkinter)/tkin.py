import tkinter as tk
from tkinter import messagebox

def load_tasks(filename):
    try:
        with open(filename, 'r') as file:
            tasks = [line.strip().split('|') for line in file.readlines()]
        return tasks
    except FileNotFoundError:
        return []

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task[0]}|{task[1]}\n")

def display_tasks(tasks):
    task_list.delete(1.0, tk.END)  # Clear the current content
    if not tasks:
        task_list.insert(tk.END, "No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            task_list.insert(tk.END, f"{index}. {task[0]}: {task[1]}\n")

def add_task():
    title = entry_title.get()
    description = entry_description.get()
    if title and description:
        tasks.append((title, description))
        display_tasks(tasks)
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter both title and description.")

def mark_completed():
    try:
        index = int(entry_index.get()) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            display_tasks(tasks)
            entry_index.delete(0, tk.END)
        else:
            messagebox.showwarning("Index Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

def delete_task():
    try:
        index = int(entry_index.get()) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            display_tasks(tasks)
            entry_index.delete(0, tk.END)
        else:
            messagebox.showwarning("Index Error", "Invalid task number.")
    except ValueError:
        messagebox.showwarning("Input Error", "Please enter a valid task number.")

# Main program
filename = "tasks.txt"
tasks = load_tasks(filename)

root = tk.Tk()
root.title("Task Manager")

# GUI Components
label_title = tk.Label(root, text="Title:")
label_title.grid(row=0, column=0, padx=5, pady=5)
entry_title = tk.Entry(root)
entry_title.grid(row=0, column=1, padx=5, pady=5)

label_description = tk.Label(root, text="Description:")
label_description.grid(row=1, column=0, padx=5, pady=5)
entry_description = tk.Entry(root)
entry_description.grid(row=1, column=1, padx=5, pady=5)

btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.grid(row=2, column=0, columnspan=2, pady=10)

label_index = tk.Label(root, text="Task Number:")
label_index.grid(row=3, column=0, padx=5, pady=5)
entry_index = tk.Entry(root)
entry_index.grid(row=3, column=1, padx=5, pady=5)

btn_mark_completed = tk.Button(root, text="Mark Completed", command=mark_completed)
btn_mark_completed.grid(row=4, column=0, columnspan=2, pady=5)

btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.grid(row=5, column=0, columnspan=2, pady=5)

task_list = tk.Text(root, height=10, width=40)
task_list.grid(row=6, column=0, columnspan=2, pady=10)

# Load and display tasks
display_tasks(tasks)

# Save tasks when closing the window
root.protocol("WM_DELETE_WINDOW", lambda: [save_tasks(filename, tasks), root.destroy()])

root.mainloop()
