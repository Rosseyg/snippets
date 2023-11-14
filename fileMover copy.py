import os
import shutil

class FileMover:
    def __init__(self):
        pass

    def move_files_by_extension(self, folder_to_search, folder_to_move, file_extension):
        # Check if the source folder exists
        if not os.path.exists(folder_to_search):
            print(f"Source folder '{folder_to_search}' does not exist.")
            return

        # Check if the destination folder exists, and create it if it doesn't
        if not os.path.exists(folder_to_move):
            os.makedirs(folder_to_move)

        # Walk through the source folder and its subfolders
        for root, _, files in os.walk(folder_to_search):
            for file in files:
                if file.endswith(file_extension):
                    source_file_path = os.path.join(root, file)
                    destination_file_path = os.path.join(folder_to_move, file)

                    # Move the file to the destination folder
                    try:
                        shutil.move(source_file_path, destination_file_path)
                        print(f"Moved '{file}' to '{folder_to_move}'.")
                    except Exception as e:
                        print(f"Error moving '{file}': {str(e)}")

if __name__ == "__main__":
    # Create an instance of the FileMover class
    file_mover = FileMover()

    # Define the source folder, destination folder, and file extension
    folder_to_search = "/path/to/source/folder"
    folder_to_move = "/path/to/destination/folder"
    file_extension = ".txt"  # Change this to the desired file extension

    # Call the method to move files
    file_mover.move_files_by_extension(folder_to_search, folder_to_move, file_extension)
