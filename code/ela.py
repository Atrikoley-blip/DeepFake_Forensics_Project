from PIL import Image, ImageChops, ImageEnhance
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent

input_image = project_folder / "All_Images" / "original" / "img1.jpg"

output_folder = project_folder / "forensic_results" / "ela"
output_folder.mkdir(parents=True, exist_ok=True)

output_image = output_folder / "img1_ela.jpg"

original = Image.open(input_image).convert("RGB")

temp_file = project_folder / "temp_ela.jpg"

original.save(temp_file, "JPEG", quality=90)

compressed = Image.open(temp_file).convert("RGB")

difference = ImageChops.difference(original, compressed)

enhancer = ImageEnhance.Brightness(difference)
ela_image = enhancer.enhance(10)
ela_image.save(output_image)

print("ELA test completed!")
print("ELA image saved at:")
print(output_image)