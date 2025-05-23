import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog
from pathlib import Path

# Configuration Section
# Modify this path to change the default image folder
# Ex. DEFAULT_IMAGE_PATH = r"C:\Users\user\Documents\Pictures"
# Ex. DEFAULT_OUTPUT_PATH = r"C:\Users\user\Documents\Pictures"
DEFAULT_IMAGE_PATH = os.path.join(os.path.expanduser("~"), "Pictures")
DEFAULT_OUTPUT_PATH = os.path.join(os.path.expanduser("~"), "Pictures", "Resized_Images")

def select_image(default_path: str) -> str:
    """
    Opens a file explorer dialog for selecting an image file.
    
    Args:
        default_path (str): Default directory path for file explorer
    
    Returns:
        str: Path to selected image file or empty string if cancelled
    """
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    
    file_path = filedialog.askopenfilename(
        initialdir=default_path,
        title="Select Image",
        filetypes=[
            ("Image files", "*.png *.jpg *.jpeg *.bmp *.gif"),
            ("All files", "*.*")
        ]
    )
    return file_path

def get_dimensions() -> tuple[int, int]:
    """
    Prompts user for desired width and height dimensions.
    
    Returns:
        tuple: (width, height) of desired dimensions
    """
    while True:
        try:
            width = int(input("Enter desired width (pixels): "))
            height = int(input("Enter desired height (pixels): "))
            if width > 0 and height > 0:
                return (width, height)
            print("Dimensions must be positive numbers!")
        except ValueError:
            print("Please enter valid numbers!")

def resize_image(input_path: str, output_folder: str, dimensions: tuple[int, int]) -> None:
    """
    Resizes the selected image and saves it with new dimensions in the filename.
    Preserves transparency for images with an alpha channel.
    
    Args:
        input_path (str): Path to input image
        output_folder (str): Directory to save resized image
        dimensions (tuple): Desired (width, height) for resized image
    """
    try:
        # Open and process image
        with Image.open(input_path) as img:
            # Check if image has transparency (RGBA mode)
            has_transparency = img.mode == 'RGBA'
            
            # Resize image while maintaining aspect ratio
            img.thumbnail(dimensions, Image.Resampling.LANCZOS)
            
            # Get filename components
            file_name = os.path.splitext(os.path.basename(input_path))[0]
            file_ext = os.path.splitext(input_path)[1].lower()
            
            # Use PNG for output if the image has transparency, otherwise keep original extension
            if has_transparency:
                output_ext = '.png'  # PNG supports transparency
            else:
                output_ext = file_ext  # Keep original extension for non-transparent images
            
            # Create new filename with dimensions
            new_filename = f"{file_name}_{dimensions[0]}x{dimensions[1]}{output_ext}"
            output_path = os.path.join(output_folder, new_filename)
            
            # Create output directory if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            
            # Save resized image, preserving transparency if present
            if has_transparency:
                img.save(output_path, format='PNG')  # Save as PNG to preserve transparency
            else:
                img.save(output_path, quality=95)  # Use original format for non-transparent images
            
            print(f"Image saved successfully as: {new_filename}")
            
    except Exception as e:
        print(f"Error processing image: {str(e)}")

def main():
    """
    Main function to orchestrate the image resizing process.
    """
    print("Image Resizer Script")
    print("-------------------")
    
    # Select image using configured default path
    print(f"Default image folder: {DEFAULT_IMAGE_PATH}")
    image_path = select_image(DEFAULT_IMAGE_PATH)
    
    if not image_path:
        print("No image selected. Exiting...")
        return
    
    # Get desired dimensions
    dimensions = get_dimensions()
    
    # Resize and save image
    resize_image(image_path, DEFAULT_OUTPUT_PATH, dimensions)

if __name__ == "__main__":
    main()
