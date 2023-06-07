import os

# Example usage
dir1 = <path_to_dir1>
dir2 = <path_to_dir2>

def get_filenames(directory):
    filenames = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            filenames.append(os.path.splitext(filename)[0])
    return filenames


def check_files_presence(dir1, dir2):
    dir1_filenames = get_filenames(dir1)
    dir2_filenames = get_filenames(dir2)

    not_present_in_dir1 = []
    not_present_in_dir2 = []

    # Check filenames present in dir2 but not in dir1
    for filename in dir2_filenames:
        if filename not in dir1_filenames:
            not_present_in_dir1.append(filename)

    # Check filenames present in dir1 but not in dir2
    for filename in dir1_filenames:
        if filename not in dir2_filenames:
            not_present_in_dir2.append(filename)

    return not_present_in_dir1, not_present_in_dir2

not_present_in_dir1, not_present_in_dir2 = check_files_presence(dir1, dir2)

if not_present_in_dir1:
    print("Files present in dir2 but not in dir1:")
    for filename in not_present_in_dir1:
        print(filename)
    print(f"Total count: {len(not_present_in_dir1)}")
else:
    print("All files from dir2 are present in dir1.")

print()  # Adding a new line for clarity

if not_present_in_dir2:
    print("Files present in dir1 but not in dir2:")
    for filename in not_present_in_dir2:
        print(filename)
    print(f"Total count: {len(not_present_in_dir2)}")
else:
    print("All files from dir1 are present in dir2.")

print()  # Adding a new line for clarity

# Remove files from dir2 that are not present in dir1
if not_present_in_dir1:
    print("Removing files from dir2...")
    for filename in not_present_in_dir1:
        file_path = os.path.join(dir2, filename + ".png")
        os.remove(file_path)
        print(f"Removed: {file_path}")
    print("Files removed successfully.")
else:
    print("No files to remove from dir2.")
