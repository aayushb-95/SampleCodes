import os
from pathlib import Path

IMAGES = ''  # Path to the images folder
MASKS = ''  # Path to the masks folder

img_file_type = "**/*." + "jpg"
img_path_list = sorted(Path(IMAGES + "/").glob(img_file_type))

masks_file_type = "**/*." + "png"
masks_path_list = sorted(Path(MASKS + "/").glob(masks_file_type))


for i in range(len(img_path_list)):
    img_filename = os.path.basename(img_path_list[i])
    img_filename_root = os.path.splitext(img_filename)

    masks_filename = os.path.basename(masks_path_list[i])
    masks_filename_root = os.path.splitext(masks_filename)
    print(img_filename_root, masks_filename_root)
