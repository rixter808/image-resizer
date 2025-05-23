# Image Resizer

A simple Python script for resizing images with a user-friendly interface.

## Features
- Interactive file explorer to select input image
- User-specified width and height for resizing
- Maintains aspect ratio during resizing
- Saves output with dimensions in filename (e.g., `image_500x500.png`)
- Supports common image formats (PNG, JPG, JPEG, BMP, GIF)
- High-quality image resizing using LANCZOS resampling
- Preserves transparency for images with alpha channels (saves as PNG)

## Requirements
- Python 3.6+
- Pillow (`pip install Pillow`)
- tkinter (usually included with Python installation)

## Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-resizer.git
cd image-resizer