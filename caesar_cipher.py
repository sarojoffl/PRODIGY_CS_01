def caesar_cipher_encrypt(plaintext, shift):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += char  # Non-alphabetic characters are not changed
    return ciphertext

def caesar_cipher_decrypt(ciphertext, shift):
    return caesar_cipher_encrypt(ciphertext, -shift)

def main():
    while True:
        print("Caesar Cipher")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ")
        
        if choice == '1':
            plaintext = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_message = caesar_cipher_encrypt(plaintext, shift)
            print(f"Encrypted message: {encrypted_message}\n")
        elif choice == '2':
            ciphertext = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_message = caesar_cipher_decrypt(ciphertext, shift)
            print(f"Decrypted message: {decrypted_message}\n")
        elif choice == '3':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose a valid option.\n")

if __name__ == "__main__":
    main()

