import tkinter as tk
from tkinter import ttk
import csv
import os

FILE_NAME = "students.csv"

root = tk.Tk()
root.title("Record of Students")

name_label = tk.Label(root, text="Name")
name_label.grid(row=0, column=0, padx=10, pady=5)

age_label = tk.Label(root, text="Age")
age_label.grid(row=1, column=0, padx=10, pady=5)

name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=5)

age_entry = tk.Entry(root)
age_entry.grid(row=1, column=1, padx=10, pady=5)

tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings", height=10)
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.column("Name", width=150)
tree.column("Age", width=80)
tree.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def load_from_file():
    if not os.path.exists(FILE_NAME):
        return
    with open(FILE_NAME, newline="", encoding="utf-8") as f:
        for row in csv.reader(f):
            if row:
                tree.insert("", tk.END, values=row)

def save_to_file():
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        for item in tree.get_children():
            writer.writerow(tree.item(item)["values"])

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    tree.insert("", tk.END, values=(name, age))
    save_to_file()
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add", command=add_student)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=0, padx=10, pady=10)

save_button = tk.Button(root, text="Save", command=save_to_file)
save_button.grid(row=4, column=1, padx=10, pady=10)

load_from_file()
root.mainloop()