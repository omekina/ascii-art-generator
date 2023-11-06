from PIL import Image
import numpy as np


ASCII_BRIGHTNESS = "@&%QWXKA\"bY5Zoen[ultr!_:'-.` "
IMAGE_SIZE = (80, 30)


def fetch_image(filepath: str) -> np.array:
    img = Image.open(filepath)
    img = img.resize(IMAGE_SIZE)
    load = img.load()
    pixels = []
    for y in range(img.height):
        temp = []
        for x in range(img.width):
            current = load[x, y]
            temp.append((current[0] + current[1] + current[2]) / 3)
        pixels.append(temp)
    return np.array(pixels)


def to_linspace(data: np.array) -> np.array:
    data = data - np.min(data)
    return np.round(1 - (data / np.max(data)), 1)


def to_ascii(data: np.array) -> np.array:
    result = ""
    for row in range(len(data)):
        current_row = "echo \""
        for column in range(len(data[0])):
            current_item = data[row][column]
            current_char = ASCII_BRIGHTNESS[int(current_item * (len(ASCII_BRIGHTNESS) - 1))] * 1
            current_row += "\\" if current_char == "\"" else ""
            current_row += current_char
        result += current_row + "\"\n"
    return result


def main() -> None:
    data = fetch_image(input("Path to image: "))
    data = to_linspace(data)
    data = to_ascii(data)
    print(data)


if __name__ == '__main__':
    main()
