import cv2
from pathlib import Path
import os
from PIL import Image
import configuration as config
image_counter = 0

masks_file_type = "**/*." + "png"
masks_path_list = sorted(Path(config.MASKS + "/").glob(masks_file_type))

for i in range(image_counter, len(masks_path_list), 1):
    masks_path_str = str(masks_path_list[i])
    filename = os.path.basename(masks_path_str)
    img = Image.open(masks_path_str)
    pixel_map = img.load()
    w, h = img.size
    for x in range(w):
        for y in range(h):
            r,g,b = img.getpixel((x, y))
            if (r,g,b) == (250, 250, 55):
                pixel_map[x,y] = (int(255), int(255), int(255))

    print("Manipulating image: ", i)
    img.save(config.MONOMASKS + filename)


