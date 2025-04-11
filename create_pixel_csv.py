from PIL import Image
import csv

# Image data path
input_image_path = ""

# Output CSV file path
output_csv_path = ""

# Resolution
width, height = 0, 0

def main():
    # Load the image
    img = Image.open(input_image_path).convert("RGB")
    # Resize the image (downscale to create a coarse mosaic effect)
    img = img.resize((width, height), Image.Resampling.LANCZOS)
    
    # Pixel access object
    pixels = img.load()

    # Write to CSV
    with open(output_csv_path, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Header Row
        writer.writerow(["x", "y", "r", "g", "b"])

        # Iterate over each pixel in the image
        for y in range(height):
            for x in range(width):
                r, g, b = pixels[x, y]
                writer.writerow([x, y, r, g, b])

    print(f"Saved CSV to {output_csv_path}")

if __name__ == "__main__":
    main()