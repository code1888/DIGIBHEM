from PIL import Image
import os


def encrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path).convert("RGB")
        pixels = image.load()

        for y in range(image.height):
            for x in range(image.width):
                r, g, b = pixels[x, y]

                # Mathematical pixel manipulation
                r = (r + key) % 256
                g = (g + key) % 256
                b = (b + key) % 256

                pixels[x, y] = (r, g, b)

        image.save(output_path)
        print(f"\nImage encrypted successfully!")
        print(f"Saved as: {output_path}")

    except FileNotFoundError:
        print("Error: Input image not found.")
    except Exception as e:
        print(f"Error: {e}")


def decrypt_image(input_path, output_path, key):
    try:
        image = Image.open(input_path).convert("RGB")
        pixels = image.load()

        for y in range(image.height):
            for x in range(image.width):
                r, g, b = pixels[x, y]

                # Reverse the encryption operation
                r = (r - key) % 256
                g = (g - key) % 256
                b = (b - key) % 256

                pixels[x, y] = (r, g, b)

        image.save(output_path)
        print(f"\nImage decrypted successfully!")
        print(f"Saved as: {output_path}")

    except FileNotFoundError:
        print("Error: Input image not found.")
    except Exception as e:
        print(f"Error: {e}")


def main():
    print("=" * 45)
    print("      PIXEL MANIPULATION IMAGE ENCRYPTION")
    print("=" * 45)

    print("\n1. Encrypt Image")
    print("2. Decrypt Image")

    choice = input("\nEnter your choice (1/2): ")

    input_path = input("Enter image path: ")

    try:
        key = int(input("Enter encryption key (1-255): "))

        if key < 1 or key > 255:
            print("Key must be between 1 and 255.")
            return

    except ValueError:
        print("Please enter a valid numeric key.")
        return

    if choice == "1":
        output_path = input("Enter output image path: ")
        encrypt_image(input_path, output_path, key)

    elif choice == "2":
        output_path = input("Enter output image path: ")
        decrypt_image(input_path, output_path, key)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()