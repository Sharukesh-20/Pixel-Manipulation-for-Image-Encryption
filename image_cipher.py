from PIL import Image
import os

def encrypt_decrypt_image(input_path, output_path, key):
    try:
        # Open the image
        img = Image.open(input_path)
        img = img.convert("RGB")
        pixels = img.load()

        # Get image dimensions
        width, height = img.size

        # Process each pixel
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Apply XOR with key
                r_new = r ^ key
                g_new = g ^ key
                b_new = b ^ key
                pixels[x, y] = (r_new, g_new, b_new)

        # Save the new image
        img.save(output_path)
        print(f"Image saved successfully at: {output_path}")

    except Exception as e:
        print("Error:", e)

def main():
    print("=== Image Encryption / Decryption Tool ===")
    choice = input("Type 'encrypt' or 'decrypt': ").strip().lower()

    input_path = input("Enter input image path (e.g., image.jpg): ")
    output_path = input("Enter output image path (e.g., encrypted.png): ")
    
    try:
        key = int(input("Enter a numeric key (0-255): "))
        if not (0 <= key <= 255):
            raise ValueError
    except ValueError:
        print("Invalid key. Must be an integer between 0 and 255.")
        return

    if choice in ['encrypt', 'decrypt']:
        encrypt_decrypt_image(input_path, output_path, key)
    else:
        print("Invalid option. Please type 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
