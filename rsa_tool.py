import random
import argparse
import tkinter as tk
from tkinter import messagebox

# --- 1. RSA Mathematical Core ---

def gcd(a, b):
    """Calculates the Greatest Common Divisor."""
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    """Calculates the modular inverse using the Extended Euclidean Algorithm."""
    d_old, d_new = 0, 1
    r_old, r_new = phi, e
    while r_new != 0:
        quotient = r_old // r_new
        d_old, d_new = d_new, d_old - quotient * d_new
        r_old, r_new = r_new, r_old - quotient * r_new
    if d_old < 0:
        d_old += phi
    return d_old

def is_prime(num):
    """Simple primality check (for educational small primes)."""
    if num < 2: return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0: return False
    return True

def generate_keypair(p, q):
    """Generates the public and private key pairs."""
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    if p == q:
        raise ValueError("p and q cannot be equal.")
    
    # Calculate n and the totient (phi)
    n = p * q
    phi = (p - 1) * (q - 1)
    
    # Choose e (public exponent)
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)
    
    # Calculate d (private exponent)
    d = mod_inverse(e, phi)
    
    # Return (Public Key), (Private Key)
    return ((e, n), (d, n))

def encrypt(public_key, plaintext):
    """Encrypts a string into a list of integers."""
    e, n = public_key
    # Formula: c = m^e mod n
    return [pow(ord(char), e, n) for char in plaintext]

def decrypt(private_key, ciphertext):
    """Decrypts a list of integers back into a string."""
    d, n = private_key
    # Formula: m = c^d mod n
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# --- 2. CLI Implementation ---

def run_cli():
    print("--- RSA Encryption/Decryption CLI ---")
    try:
        p = int(input("Enter prime p (e.g., 61): "))
        q = int(input("Enter prime q (e.g., 53): "))
        
        print("\nGenerating keys...")
        public, private = generate_keypair(p, q)
        print(f"Public Key (e, n): {public}")
        print(f"Private Key (d, n): {private}")
        
        msg = input("\nEnter a message to encrypt: ")
        encrypted_msg = encrypt(public, msg)
        print(f"Ciphertext array: {encrypted_msg}")
        
        decrypted_msg = decrypt(private, encrypted_msg)
        print(f"Decrypted message: {decrypted_msg}")
    except ValueError as e:
        print(f"Error: {e}")

# --- 3. GUI Implementation ---

def run_gui():
    root = tk.Tk()
    root.title("RSA Encryption Tool")
    root.geometry("400x500")

    tk.Label(root, text="Enter Prime p (e.g., 61):").pack(pady=(10,0))
    entry_p = tk.Entry(root)
    entry_p.pack()

    tk.Label(root, text="Enter Prime q (e.g., 53):").pack(pady=(10,0))
    entry_q = tk.Entry(root)
    entry_q.pack()

    tk.Label(root, text="Message to Encrypt:").pack(pady=(10,0))
    entry_msg = tk.Entry(root)
    entry_msg.pack()

    result_text = tk.Text(root, height=15, width=45)

    def execute_rsa():
        try:
            p = int(entry_p.get())
            q = int(entry_q.get())
            msg = entry_msg.get()
            
            pub, priv = generate_keypair(p, q)
            enc = encrypt(pub, msg)
            dec = decrypt(priv, enc)
            
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"Public Key: {pub}\nPrivate Key: {priv}\n")
            result_text.insert(tk.END, f"-"*40 + "\n")
            result_text.insert(tk.END, f"Ciphertext:\n{enc}\n\n")
            result_text.insert(tk.END, f"Decrypted:\n{dec}")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(root, text="Run RSA", command=execute_rsa, bg="lightblue").pack(pady=15)
    result_text.pack()
    root.mainloop()

# --- Entry Point ---
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="RSA Algorithm Implementation")
    parser.add_argument('--gui', action='store_true', help="Launch the GUI version")
    args = parser.parse_args()
    
    if args.gui:
        run_gui()
    else:
        run_cli()