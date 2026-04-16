import tkinter as tk

window = tk.Tk()
window.title("This is my first GUI")
window.geometry('900x500')

# Title
root_label = tk.Label(window, text="Calculator For SI",
                      font=("Arial", 14, "bold"),
                      background="red", fg="black",
                      padx=10, pady=5)
root_label.grid(row=0, column=0, columnspan=2, pady=10)

# Principal
principal_label = tk.Label(window, text="Principal (in rs):")
principal_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

principal_entry = tk.Entry(window)
principal_entry.grid(row=1, column=1, padx=10, pady=5)

# Time
time_label = tk.Label(window, text="Time (in yrs):")
time_label.grid(row=2, column=0, padx=10, pady=5, sticky="e")

time_entry = tk.Entry(window)
time_entry.grid(row=2, column=1, padx=10, pady=5)

# Rate
rate_label = tk.Label(window, text="Rate (in percent):")
rate_label.grid(row=3, column=0, padx=10, pady=5, sticky="e")

rate_entry = tk.Entry(window)
rate_entry.grid(row=3, column=1, padx=10, pady=5)

# Result
result_label = tk.Label(window, text="", font=("Arial", 13), fg="blue")
result_label.grid(row=5, column=2, columnspan=2, pady=20)

# Function
def calculate():
    P = float(principal_entry.get())
    T = float(time_entry.get())
    R = float(rate_entry.get())
    si = P * T * R / 100
    result_label.config(text=f"Simple Interest: {si:.2f}")

# Button
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=3, columnspan=2, pady=10)

window.mainloop()