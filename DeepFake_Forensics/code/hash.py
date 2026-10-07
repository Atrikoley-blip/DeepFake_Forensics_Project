import hashlib
image_path = "All_Images/compressed/img1.jpg"
sha256_hash = hashlib.sha256()
with open(image_path, "rb") as f:
    for block in iter(lambda: f.read(4096), b""):
        sha256_hash.update(block)

print("File:", image_path)
print("SHA-256:")
print(sha256_hash.hexdigest())