import tkinter as tk

window = tk.Tk()
window.title("This is my first GUI")
window.geometry('900x500')

root_label = tk.Label(window, text="Calculator For SI",
                      font=("Arial", 14, "bold"), background="red",
                      fg="black", padx=10, pady=5)
root_label.pack()

principal_label = tk.Label(window, text="Principal (in rs):")
principal_label.pack(pady=5)
principal_entry = tk.Entry(window)
principal_entry.pack(pady=5)

time_label = tk.Label(window, text="Time (in yrs):")
time_label.pack(pady=5)
time_entry = tk.Entry(window)
time_entry.pack(pady=10)  

rate_label = tk.Label(window, text="Rate (in percent):")
rate_label.pack(pady=5)
rate_entry = tk.Entry(window)
rate_entry.pack(pady=10)

result_label = tk.Label(window, text="", font=("Arial", 13), fg="blue")
result_label.pack(pady=20)  # FIX 1: pack() called once outside the function

def calculate():
    P = float(principal_entry.get())
    T = float(time_entry.get())
    R = float(rate_entry.get())
    si = P * T * R / 100
    result_label.config(text=f"Simple Interest: {si:.2f}")  # FIX 2: use text= and f-string

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack(pady=20)

window.mainloop()