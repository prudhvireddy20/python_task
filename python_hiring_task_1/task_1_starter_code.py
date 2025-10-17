import os
from PIL import Image
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PIL import ImageOps

INPUT_DIR = "input_images"
OUTPUT_PDF = "output.pdf"
PAGE_SIZE = A4  # width, height in points (1 pt = 1/72 inch) 

def preprocess_image(image_path: str):
    """This function preprocesses the images by removing transparent background
    and cropping to visible content

    Args:
        image_path (str): The Input path of the image

    Returns:
        PIL.Image: The preprocessed image
    """
    # Open image with alpha channel
    image = Image.open(image_path)
    
    # Convert to RGBA if not already
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    
    # Get bounding box of non-transparent pixels
    bbox = image.getbbox()
    if bbox:
        # Crop to visible content
        image = image.crop(bbox)
    
    # Convert to RGB (remove transparency)
    image = Image.new('RGB', image.size, (255, 255, 255))
    
    return image

def generate_pdf(input_dir: str, output_pdf_path: str, page_size):
    """This is the main function to generate the PDF

    Args:
        input_dir (str): The input directory containing the images
        output_pdf_path (str): The path to save the generated PDF
        page_size (_type_): The page size of the PDF (A4, Letter, etc.)
    """
    # Get list of image files
    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    # Create PDF canvas
    c = canvas.Canvas(output_pdf_path, pagesize=page_size)
    
    # Page dimensions
    page_width, page_height = page_size
    margin = 50  # 50 points margin
    
    for image_file in sorted(image_files):
        image_path = os.path.join(input_dir, image_file)
        
        # Preprocess image
        image = preprocess_image(image_path)
        
        # Compress image
        compressed_path = compress_images(image_path, "temp.jpg")
        
        # Calculate scaling to fit within margins
        img_width, img_height = image.size
        width_ratio = (page_width - 2 * margin) / img_width
        height_ratio = (page_height - 2 * margin) / img_height
        scale = min(width_ratio, height_ratio)
        
        # Calculate centered position
        final_width = img_width * scale
        final_height = img_height * scale
        x = (page_width - final_width) / 2
        y = (page_height - final_height) / 2
        
        # Draw image
        c.drawImage(compressed_path, x, y, width=final_width, height=final_height)
        
        # Add a new page for next image
        c.showPage()
        
        # Clean up temporary file
        if os.path.exists("temp.jpg"):
            os.remove("temp.jpg")
    
    c.save()

def compress_images(input_image_path: str, output_image_path: str, compression_level: int=5):
    """This function compresses the images to minimize the PDF size

    Args:
        input_image_path (str): The path of the input image
        output_image_path (str): The path to save the compressed image
        compression_level (int, optional): The compression level (0-9). Defaults to 5.

    Returns:
        str: The path of the compressed image
    """
    # Open and compress image
    with Image.open(input_image_path) as img:
        # Convert to RGB if necessary
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Quality ranges from 0 (worst) to 95 (best)
        # Map compression_level 0-9 to quality 95-5
        quality = 95 - (compression_level * 10)
        
        # Save with compression
        img.save(output_image_path, 'JPEG', quality=quality, optimize=True)
    
    return output_image_path

if __name__ == "__main__":
    # Create input directory if it doesn't exist
    os.makedirs(INPUT_DIR, exist_ok=True)
    
    generate_pdf(INPUT_DIR, OUTPUT_PDF, PAGE_SIZE)