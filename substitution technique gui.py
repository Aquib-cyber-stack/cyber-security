import tkinter as tk
from tkinter import messagebox

def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def process_text(is_encrypt):
    try:
        text = text_entry.get("1.0", tk.END).strip()
        shift = int(shift_entry.get())
        if not is_encrypt:
            shift = -shift
        result = encrypt_caesar(text, shift)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Shift key must be an integer")

root = tk.Tk()
root.title("Substitution Cipher GUI")
root.geometry("400x400")

tk.Label(root, text="Enter Message:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

tk.Label(root, text="Enter Shift Key:").pack(pady=5)
shift_entry = tk.Entry(root)
shift_entry.pack()

tk.Button(root, text="Encrypt", command=lambda: process_text(True)).pack(pady=5)
tk.Button(root, text="Decrypt", command=lambda: process_text(False)).pack(pady=5)

tk.Label(root, text="Result:").pack(pady=5)
result_entry = tk.Text(root, height=5, width=40)
result_entry.pack()

root.mainloop()