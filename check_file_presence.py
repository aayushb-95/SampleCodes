# Python Internal Modules
import os
from typing import List

SRC_DIR: str = "/src_files/"
TRG_DIR: str = "/trg_files/"
EXTENSION: str = "png"


class CheckFilePresence:
    """
    CheckFilePresence class provides methods to compare and synchronize files between two directories.
    """

    @staticmethod
    def __get_filenames(directory: str) -> List[str]:
        return [os.path.splitext(filename)[0] for filename in os.listdir(directory) if
                os.path.isfile(os.path.join(directory, filename))]

    def __check_file_presence(self, src_dir: str, trg_dir: str) -> (List[str], List[str]):
        src_dir_filenames = set(self.__get_filenames(src_dir))
        trg_dir_filenames = set(self.__get_filenames(trg_dir))

        files_not_present_in_src_dir = trg_dir_filenames - src_dir_filenames
        files_not_present_in_trg_dir = src_dir_filenames - trg_dir_filenames

        return list(files_not_present_in_src_dir), list(files_not_present_in_trg_dir)

    @staticmethod
    def __display_missing_files(message: str, missing_files: List[str]):
        if missing_files:
            print(message)
            for filename in missing_files:
                print(filename)
            print(f"Total count: {len(missing_files)}")
        else:
            print(f"All files from {message.split()[3]} are present in {message.split()[5]}")
        print()  # Adding a new line for clarity

    @staticmethod
    def remove_files(trg_dir: str, files_to_remove: List[str]):
        if files_to_remove:
            print(f"Removing files from {trg_dir}")
            for filename in files_to_remove:
                file_path = os.path.join(trg_dir, filename + EXTENSION)
                os.remove(file_path)
                print(f"Removed file from: {file_path}")
            print("All files removed successfully")
        else:
            print(f"No files to remove from {trg_dir}")

    def remove_mismatched_files(self, src_dir: str, trg_dir: str):
        missing_files_src, missing_files_trg = self.__check_file_presence(src_dir, trg_dir)

        self.__display_missing_files(f"Files present in {trg_dir} but not in {src_dir}:", missing_files_src)
        self.__display_missing_files(f"Files present in {src_dir} but not in {trg_dir}:", missing_files_trg)

        # Remove files from dir2 that are not present in dir1
        self.remove_files(trg_dir, missing_files_src)


def main():
    file_presence = CheckFilePresence()
    file_presence.remove_mismatched_files(SRC_DIR, TRG_DIR)


# ========= Main Entry Point =========
if __name__ == "__main__":
    main()
