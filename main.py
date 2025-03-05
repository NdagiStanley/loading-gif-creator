from PIL import Image
import os

# Define image file names (update these based on your actual file names)
image_files = [
    "hexagon_blue.svg",
    "hexagon-2-sixths_blue.svg",
    "hexagon-4-sixths_blue.svg",
    "hexagon-6-sixths_blue.svg"
]

# Load images
images = [Image.open(img) for img in image_files]

# Resize images (optional, for smaller file size)
resized_images = [img.resize((img.width // 2, img.height // 2)) for img in images]

# Save as GIF
output_path = "hexagon_animation.gif"
resized_images[0].save(
    output_path,
    save_all=True,
    append_images=resized_images[1:],
    duration=500,  # 500ms per frame
    loop=0,  # Infinite loop
    optimize=True  # Compress GIF
)

print(f"GIF saved as {output_path}")
