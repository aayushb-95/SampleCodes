import cv2
import numpy as np
import os
from pathlib import Path
import configuration as config

image_counter = 0

def save(filename, image):
    image_file_path = config.IMAGES_ROTATE + str(filename) + ".jpg"
    print("Saving image: ", i, filename)
    cv2.imwrite(image_file_path, image)

file_type = "**/*." + "jpg"
path_list = sorted(Path(config.IMAGES + "/").glob(file_type))
print(len(path_list))

for i in range(image_counter, len(path_list), 1):
    path_str = str(path_list[i])
    frame_input = cv2.imread(path_str)
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)
    image = cv2.rotate(frame_input, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    save(filename_root[0], image)



def save(filename, image):
    image_file_path = config.MASKS_ROTATE + str(filename) + ".png"
    print("Saving image: ", i, filename)
    cv2.imwrite(image_file_path, image)

file_type = "**/*." + "png"
path_list = sorted(Path(config.MASKS + "/").glob(file_type))
print(len(path_list))

for i in range(image_counter, len(path_list), 1):
    path_str = str(path_list[i])
    frame_input = cv2.imread(path_str)
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)
    image = cv2.rotate(frame_input, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)
    save(filename_root[0], image)

