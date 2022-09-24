import extcolors
from PIL import Image


def rgb_to_hex(r, g, b):
    return ("#{:X}{:X}{:X}").format(r, g, b)


def color_group_test(path: str) -> dict:
    MAX_WIDTH = 250
    MAX_HEIGHT = 250

    img = Image.open(path)
    img = img.resize((MAX_WIDTH, MAX_HEIGHT))

    colors, _ = extcolors.extract_from_image(img, tolerance=20, limit=3000)

    groups = []
    for rgb in colors:
        r, g, b = rgb[0]
        groups.append({"hex": rgb_to_hex(r, g, b), "count": rgb[1]})

    return groups, len(groups)
