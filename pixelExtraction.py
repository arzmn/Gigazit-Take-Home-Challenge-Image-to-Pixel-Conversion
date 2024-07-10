from PIL import Image
import numpy as np

def image_to_pixel_list(image_path):
    # Load the image
    image = Image.open(image_path).convert('L')  # Convert to grayscale
    # Convert image to NumPy array
    pixel_array = np.array(image)
    # Convert NumPy array to list
    pixel_list = pixel_array.tolist()
    return pixel_list

def save_pixel_list(pixel_list, output_path):
    # Save the pixel list to a file
    with open(output_path, 'w') as f:
        for row in pixel_list:
            f.write(' '.join(map(str, row)) + '\n')

if __name__ == "__main__":
    # Define input and output paths
    input_image_path = 'testImage.png'
    output_pixel_path = 'pixel_output.txt'
    
    # Convert image to pixel list
    pixel_list = image_to_pixel_list(input_image_path)
    
    # Save pixel list to a file
    save_pixel_list(pixel_list, output_pixel_path)
    
    print(f"Pixel data saved to {output_pixel_path}")
    # Print pixel list (for demonstration purposes)
    print("Pixel data as list:")
    print(pixel_list)
