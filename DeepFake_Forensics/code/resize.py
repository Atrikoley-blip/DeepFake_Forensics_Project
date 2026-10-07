from PIL import Image
image = Image.open("All_Images/original/img1.jpg")
width, height = image.size
new_size = (width // 2, height // 2)
resized = image.resize(new_size)
resized.save("All_Images/resized/image1_resized.jpg")
print("Resizing completed.")