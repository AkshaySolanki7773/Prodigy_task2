from PIL import Image  # Make sure Pillow is installed

def encrypt_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # swapping red and blue channels
                encrypted_pixel = (b, g, r)

                pixels[i, j] = encrypted_pixel

        img.save(output_path)
        print("Image encrypted successfully!")

    except Exception as e:
        print(f"Error during encryption: {e}")

def decrypt_image(input_path, output_path):
    try:
        img = Image.open(input_path)
        pixels = img.load()

        width, height = img.size

        for i in range(width):
            for j in range(height):
                r, g, b = pixels[i, j]

                # swapping red and blue channels back
                decrypted_pixel = (b, g, r)

                pixels[i, j] = decrypted_pixel

        img.save(output_path)
        print("Image decrypted successfully!")

    except Exception as e:
        print(f"Error during decryption: {e}")

# Paths to the images
input_image = r"C:\Users\Akshay Solanki\Documents\PRODIGY_CS-02-main\image.jpg"
encrypted_image = r"C:\Users\Akshay Solanki\Documents\PRODIGY_CS-02-main\encrypted_image.jpg"
decrypted_image = r"C:\Users\Akshay Solanki\Documents\PRODIGY_CS-02-main\decrypted_image.jpg"

# Encrypt the image
encrypt_image(input_image, encrypted_image)

# Decrypt the image
decrypt_image(encrypted_image, decrypted_image)
