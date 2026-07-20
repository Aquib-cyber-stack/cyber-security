def encrypt_rail_fence(text, key):
    if key == 1: return text
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down, row, col = False, 0, 0
    
    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row += 1 if dir_down else -1
        
    return "".join([rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n'])

def decrypt_rail_fence(cipher, key):
    if key == 1: return cipher
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down, row, col = None, 0, 0
    
    # Mark the places with '*'
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        rail[row][col] = '*'
        col += 1
        row += 1 if dir_down else -1
        
    # Fill the marked places with cipher characters
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == '*' and index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1
                
    # Read the zigzag to decrypt
    result, row, col = [], 0, 0
    for i in range(len(cipher)):
        if row == 0: dir_down = True
        if row == key - 1: dir_down = False
        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1
        row += 1 if dir_down else -1
    return "".join(result)

if __name__ == "__main__":
    print("--- Transposition Cipher (CLI) ---")
    choice = input("Type 'E' to Encrypt or 'D' to Decrypt: ").upper()
    message = input("Enter your message: ")
    key = int(input("Enter number of rails (integer): "))

    if choice == 'E':
        print(f"Encrypted Message: {encrypt_rail_fence(message, key)}")
    elif choice == 'D':
        print(f"Decrypted Message: {decrypt_rail_fence(message, key)}")
    else:
        print("Invalid choice.")