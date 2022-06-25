import cv2
import numpy as np
import os
from pathlib import Path
import configuration as config


def save_train_images(filename, image):
    image_file_path = config.IMAGES_TRAIN + str(filename) + ".jpg"
    print("Saving image: ", filename)
    cv2.imwrite(image_file_path, image)

def save_train_masks(filename, image):
    image_file_path = config.MASKS_TRAIN + str(filename) + ".png"
    print("Saving image: ", filename)
    cv2.imwrite(image_file_path, image)

def save_test_images(filename, image):
    image_file_path = config.IMAGES_TEST + str(filename) + ".jpg"
    print("Saving image: ", filename)
    cv2.imwrite(image_file_path, image)

def save_test_masks(filename, image):
    image_file_path = config.MASKS_TEST + str(filename) + ".png"
    print("Saving image: ", filename)
    cv2.imwrite(image_file_path, image)


def iterate_path_list(path_list, randomized=False):
    path_str = np.array([])

    print("Generate path list ...")

    for path in path_list:
        path_str = np.append(path_str, str(path))  # because path is object not string

    # Randomize the image lists
    if randomized:
        np.random.shuffle(path_str)

    return path_str

file_type_images = "**/*." + "jpg"
file_type_masks = "**/*." + "png"

path_list = iterate_path_list(sorted(Path(config.IMAGES).glob(file_type_images)), False)
path_list_ground_truth = iterate_path_list(sorted(Path(config.MASKS).glob(file_type_masks)), False)
print(len(path_list))
print(len(path_list_ground_truth))

print("Shuffling Entire dataset before Splitting")
indices = np.arange(path_list.shape[0])
np.random.shuffle(indices)
path_list_input = path_list[indices]
path_list_ground_truth = path_list_ground_truth[indices]
print(path_list_input)
print(path_list_ground_truth)

# Split up in 90% training and 10% test data
number_of_images = len(path_list_input)
number_of_training_images = int(0.98 * number_of_images)
number_of_test_images = number_of_images - number_of_training_images

path_list_input_training = path_list_input[:number_of_training_images]
for i in range(0, len(path_list_input_training), 1):
    path_str = str(path_list_input_training[i])
    frame_input = cv2.imread(path_str)
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)
    save_train_images(filename_root[0], frame_input)

path_list_ground_truth_training = path_list_ground_truth[:number_of_training_images]
for i in range(0, len(path_list_ground_truth_training), 1):
    path_str = str(path_list_ground_truth_training[i])
    frame_input = cv2.imread(path_str)
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)
    save_train_masks(filename_root[0], frame_input)


path_list_input_test = path_list_input[number_of_training_images:number_of_images]
for i in range(0, len(path_list_input_test), 1):
    path_str = str(path_list_input_test[i])
    frame_input = cv2.imread(path_str)
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)
    save_test_images(filename_root[0], frame_input)

path_list_ground_truth_test = path_list_ground_truth[number_of_training_images:number_of_images]
for i in range(0, len(path_list_ground_truth_test), 1):
    path_str = str(path_list_ground_truth_test[i])
    frame_input = cv2.imread(path_str)
    filename = os.path.basename(path_str)
    filename_root = os.path.splitext(filename)
    save_test_masks(filename_root[0], frame_input)


print(len(path_list_input_training))
print(len(path_list_input_test))