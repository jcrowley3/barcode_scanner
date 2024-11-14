from PIL import Image as PIL
from pdf417decoder import PDF417Decoder
from pdf417gen import encode, render_image


def decode_barcode(image_path, output_file):
    # Load the image
    image = PIL.open(image_path)

    # Decode the PDF417 barcode
    decoder = PDF417Decoder(image)

    if decoder.decode() > 0:
        decoded = decoder.barcode_data_index_to_string(0)
        # Save the data to a text file
        with open(output_file, 'w') as file:
            file.write(decoded)
            print(f"Decoded data saved to {output_file}")


def encode_barcode(input_file, output_image):
    # Read the modified data from the text file
    with open(input_file, 'r') as file:
        modified_data = file.read()

    # Encode the modified data into a PDF417 barcode
    codes = encode(modified_data)

    # Render the barcode as an image
    image = render_image(codes)
    image.save(output_image)
    print(f"Modified barcode saved as {output_image}")


# Paths
image_path = 'file_path.png'  # Update this to the path of your image file
output_text_file = 'barcode_data.txt'
output_image_file = 'modified_barcode.png'

# User choice
choice = input("Enter 'd' to decode or 'e' to encode: ").strip().lower()

if choice == 'd':
    decode_barcode(image_path, output_text_file)
elif choice == 'e':
    encode_barcode(output_text_file, output_image_file)
else:
    print("Invalid choice. Please enter 'd' to decode or 'e' to encode.")