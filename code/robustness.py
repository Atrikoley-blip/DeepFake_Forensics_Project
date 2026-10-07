from PIL import Image, ImageFilter
from pathlib import Path

# Project folder
project_folder = Path(__file__).resolve().parent.parent

# Original image
original_path = project_folder / "All_Images" / "original" / "img6.png"

# Output folders
compressed_folder = project_folder / "All_Images" / "compressed"
resized_folder = project_folder / "All_Images" / "resized"
blurred_folder = project_folder / "All_Images" / "blurred"

# Create folders automatically
compressed_folder.mkdir(exist_ok=True)
resized_folder.mkdir(exist_ok=True)
blurred_folder.mkdir(exist_ok=True)

# Open original image
image = Image.open(original_path).convert("RGB")

print("Original image loaded successfully!")
print("Size:", image.size)

# --------------------------------
# 1. JPEG COMPRESSION
# --------------------------------

compressed_path = compressed_folder / "image1_compressed.jpg"

image.save(
    compressed_path,
    "JPEG",
    quality=30
)

print("Compressed image created.")

# --------------------------------
# 2. RESIZING
# --------------------------------

width, height = image.size

new_width = width // 2
new_height = height // 2

resized = image.resize(
    (new_width, new_height)
)

resized_path = resized_folder / "image1_resized.jpg"

resized.save(
    resized_path,
    "JPEG",
    quality=95
)

print("Resized image created.")

# --------------------------------
# 3. BLURRING
# --------------------------------

blurred = image.filter(
    ImageFilter.GaussianBlur(radius=5)
)

blurred_path = blurred_folder / "image1_blurred.jpg"

blurred.save(
    blurred_path,
    "JPEG",
    quality=95
)

print("Blurred image created.")

print("\nAll robustness tests completed!")