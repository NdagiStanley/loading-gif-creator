import cairosvg
from PIL import Image
import os

# Define SVG file names (update these based on your actual file names)
svg_files = [
    # "hexagon_blue.svg",
    # "hexagon-2-sixths_blue.svg",
    "hexagon-4-sixths_blue.svg",
    "hexagon-6-sixths_blue.svg"
]

# Convert SVGs to PNG and store temporary images
png_files = []
for svg in svg_files:
    png_name = svg.replace(".svg", ".png")
    cairosvg.svg2png(url=svg, write_to=png_name, dpi=600)
    png_files.append(png_name)

# Load PNG images
images = [Image.open(png) for png in png_files]

# Save as GIF
output_path = "hexagon_animation_600dpi_300ms_4+6.gif"
images[0].save(
    output_path,
    save_all=True,
    append_images=images[1:],
    duration=300,  # 500ms per frame
    loop=0,  # Infinite loop
    optimize=True  # Compress GIF
)

# Cleanup: Delete temporary PNG files
for png in png_files:
    os.remove(png)

print(f"GIF saved as {output_path}")
