# Image to ASCII Art Converter
A Python script that converts images into ASCII art. The script resizes the image, grayscales it, and maps pixel brightness values to ASCII characters.

## Features
* **Resize Images**: Automatically resizes images while maintaining aspect ratio for better ASCII representation.
* **Grayscale Conversion**: Converts images to grayscale for brightness-based ASCII mapping.
* **Customizable Output Width**: Specify the width of the ASCII art output.
* **Save Output**: Saves the generated ASCII art to a file (`ascii_art.txt`) for easy sharing or storage.

## Dependencies
This project requires the following Python libraries:
* `Pillow`

Install the library with:
```bash
pip install pillow
```

## Usage
Clone the repository and navigate to the script's directory:
```bash
git clone https://github.com/spencerboggs/image-to-ascii.git
cd image-to-ascii
```
Run the script with an image file:

```bash
python script.py <image_path> [output_width]
```

## Examples:
```bash
python script.py example.jpg 120
```
- `<image_path>`: Path to the image file.
- `[output_width]`: Optional. Sets the width of the ASCII art (default is 100).

View the ASCII art in the terminal or in the ascii_art.txt file saved in the same directory.

Convert `example.jpg` with default width:

```bash
python script.py example.jpg
```
Output is displayed in the terminal and saved to ascii_art.txt.

## Notes
Adjust the `output_width` to fine-tune the ASCII art detail. Larger widths yield more detailed results.
The script uses the following characters for mapping pixel brightness:
```
@%#*+=-:. 
```
