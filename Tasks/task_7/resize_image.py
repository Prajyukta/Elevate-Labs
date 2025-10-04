import os
from PIL import Image

# Folders
input_folder = "input img"
output_folder = "output img"

# Make sure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Desired size (width, height)
new_size = (300, 300)  # change this as needed

# Loop through all files in input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(input_folder, filename)
        img = Image.open(img_path)

        # Resize image
        resized_img = img.resize(new_size)

        # Convert all images to JPEG (optional)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + ".jpg")

        # Save resized image
        resized_img.save(output_path, "JPEG")

        print(f"✅ Resized and saved: {output_path}")

print("\n🎉 All images resized successfully!")
