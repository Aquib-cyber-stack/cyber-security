import tkinter as tk
from tkinter import messagebox

def encrypt_rail(text, key):
    if key == 1: return text
    # Use None instead of '\n' to represent empty cells
    rail = [[None for _ in range(len(text))] for _ in range(key)]
    dir_down, row, col = False, 0, 0
    
    for char in text:
        if row == 0 or row == key - 1: 
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1
        
    # Only join characters that are not None
    return "".join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] is not None])

def decrypt_rail(cipher, key):
    if key == 1: return cipher
    rail = [[None for _ in range(len(cipher))] for _ in range(key)]
    dir_down, row, col = None, 0, 0
    
    # Trace the zigzag with '*'
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1
        
    # Replace '*' with actual cipher characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1
                
    # Read the zigzag path to reconstruct the message
    result, row, col = [], 0, 0
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        if rail[row][col] is not None:
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
        
    return "".join(result)

def process_text(is_encrypt):
    try:
        text = text_entry.get("1.0", tk.END).strip()
        key = int(key_entry.get())
        if key < 1:
            raise ValueError
        result = encrypt_rail(text, key) if is_encrypt else decrypt_rail(text, key)
        result_entry.delete("1.0", tk.END)
        result_entry.insert(tk.END, result)
    except ValueError:
        messagebox.showerror("Error", "Rails key must be an integer > 0")

root = tk.Tk()
root.title("Transposition Cipher GUI")
root.geometry("400x400")

tk.Label(root, text="Enter Message:").pack(pady=5)
text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

tk.Label(root, text="Enter Number of Rails:").pack(pady=5)
key_entry = tk.Entry(root)
key_entry.pack()

tk.Button(root, text="Encrypt", command=lambda: process_text(True)).pack(pady=5)
tk.Button(root, text="Decrypt", command=lambda: process_text(False)).pack(pady=5)

tk.Label(root, text="Result:").pack(pady=5)
result_entry = tk.Text(root, height=5, width=40)
result_entry.pack()

root.mainloop()