import tkinter as tk
from tkinter import ttk
import json
import os
import sys


# Determine the path to the JSON file
if hasattr(sys, "_MEIPASS"):
    JSON_PATH = os.path.join(sys._MEIPASS, "tasks.json")
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    JSON_PATH = os.path.join(BASE_DIR, "tasks.json")

# Load existing tasks from file or create an empty list
try:
    with open(JSON_PATH, "r") as f:
        tasks = json.load(f)
except FileNotFoundError:
    tasks = []

# Function to save tasks to file
def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)
        f.flush()

# Function to add a new task to the list
# Function to add a new task to the list
def add_task(event=None):
    task_text = entry.get().strip()
    tasks.append(task_text)
    listbox.insert(tk.END, task_text)
    entry.delete(0, tk.END)
    save_tasks()



# Function to remove the selected task from the list
def remove_task():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        listbox.delete(index)
        tasks.pop(index)
        save_tasks()

# Function to remove all tasks from the list
def remove_all_tasks():
    listbox.delete(0, tk.END)
    tasks.clear()
    save_tasks()

# Create the main window
root = tk.Tk()
root.title("Demo Reel Shots")
root.geometry("800x1000")
root.configure(bg="#333")

# Set the ttk style to a dark theme
style = ttk.Style()
style.theme_use("clam")
style.configure(".", background="#333", foreground="white")
style.configure("TLabel", padding=5, font=("Arial", 12), foreground="#fff")
style.configure("TButton", padding=10, font=("Arial", 12), foreground="#fff")
style.configure("TEntry", padding=5, font=("Arial", 12), foreground="#000", background="#eee")
style.configure("TListbox", padding=5, font=("Arial", 12), foreground="#fff", background="#222")
style.map("TButton", background=[("active", "#555")], foreground=[("active", "white")])

# Create the task entry widget and "add" button
entry = ttk.Entry(root, width=60)
entry.pack(padx=20, pady=(30,10))
add_button = ttk.Button(root, text="Add", command=add_task)
add_button.pack(padx=20, pady=(10,20))

# Bind the <Return> event to the entry widget to add a new task
entry.bind("<Return>", add_task)

# Create the task list widget, "remove" button, and "remove all" button
listbox_frame = ttk.Frame(root, padding=20, relief="raised")
listbox_frame.pack(padx=20, pady=(0,20), fill="both", expand=True)
listbox = tk.Listbox(listbox_frame, width=60, height=20, selectbackground="#444", selectforeground="white")
for task in tasks:
    listbox.insert(tk.END, task)
listbox.pack(side="left", fill="both", expand=True, padx=(0,10))
listbox_scrollbar = ttk.Scrollbar(listbox_frame, command=listbox.yview)
listbox_scrollbar.pack(side="left", fill="y")
listbox["yscrollcommand"] = listbox_scrollbar.set

remove_all_button = ttk.Button(root, text="Remove All", command=remove_all_tasks)
remove_all_button.pack(padx=20, pady=(0,20), anchor="e")

remove_button = ttk.Button(root, text="Remove", command=remove_task)
remove_button.pack(padx=20, pady=(0,20), anchor="e")

root.mainloop()
