# pixel-csv-exporter

A simple utility to export pixel data from an image to a CSV file. The script resizes the input image based on a scaling factor and outputs the resulting pixel coordinates along with their RGB values.

## Prerequisites

Ensure you have Python installed on your system. If you don't have Python installed, you can install it using Homebrew:

```bash
brew install python
```

## Setup

1. **Create a virtual environment:**

```bash
python3 -m venv venv
```

2. **Activate the virtual environment:**

```bash
source venv/bin/activate
```

3. **Install the required packages:**

```bash
pip install pillow
```

## Usage

By default, the script uses a scaling factor of `0.1` to resize the image before exporting pixel data. To run the script without any arguments:

```bash
python create_pixel_csv.py
```

To use a different scaling factor, pass the `--scale` argument:

```bash
python create_pixel_csv.py --scale 0.2
```

## Note
The script uses a hardcoded input image path and output CSV path. Make sure these paths are correct for your setup before running the script.

## Exiting the Virtual Environment

When you are finished, you can exit the virtual environment by running:

```bash
deactivate
```

## License

This project is open-source. Feel free to modify and distribute it as per your needs.

## 🔗 Related Project

- [swift-charts-canvas](https://github.com/akkie76/swift-charts-canvas)  

A creative exploration of graph-based art using Swift Charts. This script helps generate pixel CSVs used in the **One More Pixel** artwork.

