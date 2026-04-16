import tkinter as tk

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

student_listbox = tk.Listbox(root, width=40, height=10)
student_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

def add_student():
    name = name_entry.get()
    age = age_entry.get()
    student_listbox.insert(tk.END, f"{name} - {age}")
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

def clear_entries():
    name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)

add_button = tk.Button(root, text="Add", command=add_student)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

clear_button = tk.Button(root, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=0, padx=10, pady=10)

save_button = tk.Button(root, text="Save")
save_button.grid(row=4, column=1, padx=10, pady=10)

root.mainloop() 