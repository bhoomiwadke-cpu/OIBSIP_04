import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for length")
        return

    characters = ""
    if letters_var.get():
        characters += string.ascii_letters
    if numbers_var.get():
        characters += string.digits
    if symbols_var.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "No character set selected!")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Advanced Password Generator")

tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=5, pady=5)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=5, pady=5)

letters_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Letters", variable=letters_var).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Include Symbols", variable=symbols_var).grid(row=3, column=0, sticky="w")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=4, column=0, columnspan=2, pady=10)
result_entry = tk.Entry(root, width=30)
result_entry.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).grid(row=6, column=0, columnspan=2, pady=10)

root.mainloop()
