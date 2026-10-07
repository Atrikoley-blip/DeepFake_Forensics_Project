from PIL import Image
image = Image.open("All_Images/original/img1.jpg").convert("RGB")
image.save(
    "All_Images/compressed/image1_compressed.jpg",
    "JPEG",
    quality=30
)
print("JPEG compression completed.")