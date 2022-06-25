import cv2
import numpy as np
import os
from pathlib import Path
import configuration as config

def iterate_path_list(path_list, randomized=False):
    path_str = np.array([])

    print("Generate path list ...")

    for path in path_list:
        path_str = np.append(path_str, str(path))  # because path is object not string

    # Randomize the image lists
    if randomized:
        np.random.shuffle(path_str)

    return path_str

file_type_images = "**/*." + "png"
path_list = iterate_path_list(sorted(Path(config.MASKS_TEST).glob(file_type_images)), False)
print(len(path_list))


for i in range(0, len(path_list), 1):
    path_str = str(path_list[i])
    print(path_str, " ", i)