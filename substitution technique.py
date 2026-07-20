def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

if __name__ == "__main__":
    print("--- Substitution Cipher (CLI) ---")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    message = input("Enter your message: ")
    shift = int(input("Enter shift key (integer): "))

    if choice == 'E':
        print(f"Encrypted Message: {encrypt_caesar(message, shift)}")
    elif choice == 'D':
        print(f"Decrypted Message: {decrypt_caesar(message, shift)}")
    else:
        print("Invalid choice.")