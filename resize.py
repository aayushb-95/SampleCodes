import cv2
import numpy as np
import os
from pathlib import Path
import configuration as config

image_counter = 0

def save(image_counter, image):
    image_file_path = config.RESIZED_IMAGES + "img_" + str(image_counter) + "_" +".jpg"
    print("Saving image: ", image_counter)
    cv2.imwrite(image_file_path, image, [cv2.IMWRITE_JPEG_QUALITY, 100])

file_type = "**/*." + "png"
path_list = sorted(Path(config.IMAGES + "/").glob(file_type))
print(len(path_list))

for i in range(image_counter, len(path_list), 1):
    path_str = str(path_list[i])
    frame_input = cv2.imread(path_str)
    img = cv2.resize(frame_input, (config.HEIGHT, config.WIDTH), interpolation=cv2.INTER_AREA)
    save(i,img)