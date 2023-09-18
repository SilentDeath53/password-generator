import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import pyperclip

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for i in range(length))
    return password

def show_password():
    password_length = str(length_entry.get())
    if password_length.isdigit():
        password_length = int(password_length)
        password = generate_password(password_length)
        password_label.config(text="\n".join([password[i:i+90] for i in range(0, len(password), 90)]))
        pyperclip.copy(password)
    else:
        password_label.config(text="Invalid input")

def copy_to_clipboard():
    password = password_label.cget("text")
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Info", "Password copied to clipboard")
    else:
        messagebox.showerror("Error", "No password generated yet")        

# Tkinter GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("900x600")

# Length Entry
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack(pady=10)

# Generate Password Button
generate_button = tk.Button(root, text="Generate Password", command=show_password)
generate_button.pack(pady=10)

# Copy to Clipboard Button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Password Label
password_label = tk.Label(root, text="")
password_label.pack(pady=10)

root.mainloop()
