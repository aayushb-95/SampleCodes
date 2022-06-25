import cv2
from pathlib import Path
import os
import configuration as config

image_counter = 0


def save(filename, image):
    image_file_path = config.OVERLAY + str(filename) + ".jpg"
    print("Saving image: ", filename)
    cv2.imwrite(image_file_path, image, [cv2.IMWRITE_JPEG_QUALITY, 100])


img_file_type = "**/*." + "jpg"
path_list = sorted(Path(config.IMAGES + "/").glob(img_file_type))

masks_file_type = "**/*." + "png"
masks_path_list = sorted(Path(config.MASKS + "/").glob(masks_file_type))

for i in range(image_counter, len(path_list), 1):
    path_str = str(path_list[i])
    masks_path_str = str(masks_path_list[i])
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)

    frame_input = cv2.imread(path_str)
    masks_input = cv2.imread(masks_path_str)

    dst = cv2.addWeighted(frame_input, 0.5, masks_input, 0.4, 0)
    save(filename_root[0], dst)
