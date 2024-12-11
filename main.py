from PIL import Image

ASCII_CHARS = "@%#*+=-:. "

def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(new_width * aspect_ratio * 0.55)
    resized_image = image.resize((new_width, new_height))
    return resized_image

def grayify(image):
    return image.convert("L")

def pixels_to_ascii(image):
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[min(pixel // 25, len(ASCII_CHARS) - 1)] for pixel in pixels)
    return ascii_str

def image_to_ascii(image_path, output_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image file: {image_path}\n{e}")
        return

    image = resize_image(image, output_width)
    image = grayify(image)
    ascii_str = pixels_to_ascii(image)

    ascii_lines = [ascii_str[i:i + output_width] for i in range(0, len(ascii_str), output_width)]
    ascii_art = "\n".join(ascii_lines)

    return ascii_art

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python script.py <image_path> [output_width]")
        sys.exit(1)

    image_path = sys.argv[1]
    output_width = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    ascii_art = image_to_ascii(image_path, output_width)

    if ascii_art:
        print(ascii_art)

        with open("ascii_art.txt", "w") as f:
            f.write(ascii_art)
            print("ASCII art saved to ascii_art.txt")
