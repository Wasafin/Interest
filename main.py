import tkinter as tk
from tkinter import messagebox

# Function to calculate simple interest
def calculate_simple_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        si = (principal * rate * time) / 100
        messagebox.showinfo("Simple Interest", f"The Simple Interest is: {si:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Function to calculate compound interest
def calculate_compound_interest():
    try:
        principal = float(principal_entry.get())
        rate = float(rate_entry.get())
        time = float(time_entry.get())
        n = float(compound_entry.get())  # times interest is compounded per year
        ci = principal * (1 + (rate / (n * 100)))**(n * time) - principal
        messagebox.showinfo("Compound Interest", f"The Compound Interest is: {ci:.2f}")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter valid numbers.")

# Create the main application window
root = tk.Tk()
root.title("Interest Calculator")

# Create labels and entry widgets for Principal, Rate, Time
tk.Label(root, text="Principal (P):").pack(pady=5)
principal_entry = tk.Entry(root)
principal_entry.pack(pady=5)

tk.Label(root, text="Rate of Interest (R %):").pack(pady=5)
rate_entry = tk.Entry(root)
rate_entry.pack(pady=5)

tk.Label(root, text="Time (T in years):").pack(pady=5)
time_entry = tk.Entry(root)
time_entry.pack(pady=5)

tk.Label(root, text="Compound Frequency (n, CI only):").pack(pady=5)
compound_entry = tk.Entry(root)
compound_entry.pack(pady=5)

# Create buttons to calculate Simple Interest and Compound Interest
simple_button = tk.Button(root, text="Calculate Simple Interest", command=calculate_simple_interest)
simple_button.pack(pady=10)

compound_button = tk.Button(root, text="Calculate Compound Interest", command=calculate_compound_interest)
compound_button.pack(pady=10)

# Run the application
root.mainloop()
