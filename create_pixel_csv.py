from PIL import Image
import csv
import argparse

# Image data path
input_image_path = "image.png"

# Output CSV file path
output_csv_path = "pixels.csv"

def main(scaleRate: float):
    # Load the image
    img = Image.open(input_image_path).convert("RGB")
    
    # Get the original image size
    original_width, original_height = img.size
    print(f"Original image size: {original_width} x {original_height}")
    
    # Calculate the new dimensions using the scale rate
    new_width = int(original_width * scaleRate)
    new_height = int(original_height * scaleRate)
    print(f"Resized image size: {new_width} x {new_height}")
    
    # Resize the image (downscale to create a coarse mosaic effect)
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    
    # Pixel access object
    pixels = img.load()

    # Write to CSV
    with open(output_csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Header Row
        writer.writerow(["x", "y", "r", "g", "b"])

        # Iterate over each pixel in the image
        for y in range(new_height):
            for x in range(new_width):
                r, g, b = pixels[x, y]
                writer.writerow([x, y, r, g, b])

    print(f"Saved CSV to {output_csv_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Resize an image and export its pixel data to CSV.")
    parser.add_argument("--scale", type=float, default=0.1, help="Scaling factor for resizing the image (default: 0.1)")
    args = parser.parse_args()

    main(args.scale)