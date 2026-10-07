from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

project_folder = Path(__file__).resolve().parent.parent
image_path = project_folder / "All_Images" / "original" / "img1.jpg"
image = Image.open(image_path)

print("Image:", image_path)
print("Format:", image.format)
print("Size:", image.size)

exif_data = image.getexif()

if not exif_data:
    print("\nNo EXIF metadata found.")
else:
    print("\nEXIF Metadata:")
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")