# Gigazit-Take-Home-Challenge-Image-to-Pixel-Conversion
A working Python script that converts images into a representation of their constituent pixels.

# Image to Pixel Conversion

## Approach
This script uses the direct pixel extraction approach to convert an image into its pixel representation. The image is loaded using the Pillow library and converted to a grayscale image. The pixel values are extracted and stored in a list. It also outputs a .txt file with pixel information.

## Libraries Used
- Pillow: For loading and processing the image.
- NumPy: For handling the pixel data.

## Output Format
The output is a list containing the pixel values of the image. This list is also saved to a text file.

## Usage
### Convert Image to Pixel List
1. Place your input image in the specified path.
2. Run the script to convert the image to a pixel list and save the output to a text file.

   ![Test Image](https://raw.githubusercontent.com/arzmn/Gigazit-Take-Home-Challenge-Image-to-Pixel-Conversion/main/testImage.png)
   ⏬
   ⏬
   ⏬
   ⏬
   ![Pixel List](https://raw.githubusercontent.com/arzmn/Gigazit-Take-Home-Challenge-Image-to-Pixel-Conversion/main/Pixel%20List%20Screenshot.png)



## Example
### Convert Image to Pixel List
```bash
python pixelExraction.py
```

# Additional Functionality - Visualizing the extracted pixel information

### Convert Pixel List to Image
1. Place your input pixel list file in the specified path.
2. Run the script to convert the pixel list back to an image and save the output image.

```bash
python pixelToImage.py
```
This will save the pixel data to pixel_output.txt and the reconstructed image to reconstructed_image.jpg.


