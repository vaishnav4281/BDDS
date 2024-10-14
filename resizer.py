import os
from PIL import Image

# Define the path to the main dataset directory
dataset_dir = 'dataset'  # Adjust to your dataset path

# Set the desired image size (for example, 224x224)
target_size = (224, 224)

# Create a function to resize images and convert to PNG
def resize_images(input_dir, target_size):
    # Walk through all subdirectories and files
    for root, dirs, files in os.walk(input_dir):
        for file in files:
            if file.endswith(('.png', '.jpg', '.jpeg')):  # Check for valid image formats
                file_path = os.path.join(root, file)
                
                try:
                    # Open the image file
                    with Image.open(file_path) as img:
                        # Resize the image
                        img_resized = img.resize(target_size, Image.Resampling.LANCZOS)
                        
                        # Convert image file extension to '.png'
                        new_file_name = os.path.splitext(file)[0] + '.png'
                        new_file_path = os.path.join(root, new_file_name)
                        
                        # Save the resized image as PNG
                        img_resized.save(new_file_path, 'PNG')
                        
                        print(f"Resized and saved as PNG: {new_file_path}")
                except Exception as e:
                    print(f"Failed to process {file_path}: {e}")

# Call the function to resize all images in the dataset directory
resize_images(dataset_dir, target_size)
