# ============================================
# Caesar Cipher Encryption and Decryption
# TASK-1
# ============================================

def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)


# Main Program
print("=" * 50)
print("       CAESAR CIPHER")
print("   Encryption & Decryption Tool")
print("=" * 50)

while True:
    print("\nChoose an option:")
    print("1. Encrypt Message")
    print("2. Decrypt Message")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        message = input("Enter message: ")

        try:
            shift = int(input("Enter shift value: "))
            encrypted = caesar_encrypt(message, shift)

            print("\nOriginal Message :", message)
            print("Shift Value      :", shift)
            print("Encrypted Message:", encrypted)

        except ValueError:
            print("Please enter a valid integer for shift.")

    elif choice == "2":
        message = input("Enter encrypted message: ")

        try:
            shift = int(input("Enter shift value: "))
            decrypted = caesar_decrypt(message, shift)

            print("\nEncrypted Message:", message)
            print("Shift Value      :", shift)
            print("Decrypted Message:", decrypted)

        except ValueError:
            print("Please enter a valid integer for shift.")

    elif choice == "3":
        print("\nThank you for using Caesar Cipher!")
        break

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")