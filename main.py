import cairosvg
from PIL import Image
import os

# Define SVG file names (update these based on your actual file names)
svg_files = [
    "hexagon_blue.svg",
    "hexagon-2-sixths_blue.svg",
    "hexagon-4-sixths_blue.svg",
    "hexagon-6-sixths_blue.svg"
]

# Convert SVGs to PNG and store temporary images
png_files = []
for svg in svg_files:
    png_name = svg.replace(".svg", ".png")
    cairosvg.svg2png(url=svg, write_to=png_name)
    png_files.append(png_name)

# Load PNG images
images = [Image.open(png) for png in png_files]

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

# Cleanup: Delete temporary PNG files
for png in png_files:
    os.remove(png)

print(f"GIF saved as {output_path}")
