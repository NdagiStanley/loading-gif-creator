# Loading GIF creator

## Features

- Converts SVG to PNG using CairoSVG
- Creates smooth GIF animation
- Optimized for smaller file size
- Automatically cleans up temporary PNG files

## Prerequisites

- Python virtual environment
- SVG files in the same directory as the script

## Steps to Use

1. Install dependencies

    ```sh
    pip install -r requirements.txt
    ```

2. Run the script

    ```sh
    python main.py
    ```

## Modifications

- For specific images, update the **svg_files** array

```diff
svg_files = [
--    "hexagon_blue.svg",
--    "hexagon-2-sixths_blue.svg",
++    # "hexagon_blue.svg",
++    # "hexagon-2-sixths_blue.svg",
    "hexagon-4-sixths_blue.svg",
    "hexagon-6-sixths_blue.svg"
]
```

- For higher resolution, remove or modify the resize function. (Example below removes the resize function)

```diff
images = [Image.open(png) for png in png_files]

-- # Resize images (optional, for smaller file size)
-- resized_images = [img.resize((img.width // 2, img.height // 2)) for img in images]

# Save as GIF
output_path = "hexagon_animation.gif"
-- resized_images[0].save(
++ images[0].save(
    output_path,
    save_all=True,
--    append_images=resized_images[1:],
++    append_images=images[1:],
    duration=500,  # 500ms per frame
    loop=0,  # Infinite loop
    optimize=True  # Compress GIF
)
```

- Increase the output resolution (Lower number -> lower resolution. Default value is 96 DPI)

```diff
-- cairosvg.svg2png(url=svg, write_to=png_name)
++ cairosvg.svg2png(url=svg, write_to=png_name, dpi=300)
```

- Adjust the animation speed (Lower number -> faster animation)

```diff
-- duration=500
++ duration=300
```
