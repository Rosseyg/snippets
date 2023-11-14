import os
import datetime

class FileDeleter:
    def __init__(self):
        self.count = 0
        self.deleted_count = 0
        self.directory = 'CurrentWork'
        self.extension = 'opt'
        self.extension2 = 'bootinfo'
        self.extension3 = 'bootinfo_guids'
        self.extension4 = 'compileinfo'
        self.extension5 = 'precompilecache'
        
    def delete_files(self):
        filenames = self.get_files_to_delete()
        for filename in filenames:
            os.remove(filename)
            self.deleted_count += 1

  
    def get_files_to_delete(self):
        filenames = []
        for root, dirs, files in os.walk(self.directory):
            for filename in files:
                if filename.endswith(self.extension) or filename.endswith(self.extension2) or filename.endswith(self.extension3) or filename.endswith(self.extension4) or filename.endswith(self.extension5):
                    filenames.append(os.path.join(root, filename))
                    self.count += 1
        if self.count == 0:
            print(f"{datetime.datetime.now()}: No files with the extension '.{self.extension}' were found in the directory '{self.directory}'.")
        return filenames
    
# Create an instance of the FileDeleter class
file_deleter = FileDeleter()
filenamesToDelete = file_deleter.get_files_to_delete()
for filename in filenamesToDelete:
    print(filename)
# Call the get_num_files_to_del() method to get the number of files with the specified extension
num_files_to_del = file_deleter.count
print(f"Number of files to delete: {num_files_to_del}")

# Call the delete_files() method to delete all the files with the specified extension
#file_deleter.delete_files("/path/to/directory", ".extension")
answer = input("Delete files? (y/n)")
if answer.lower() == "y":
    file_deleter.delete_files()
    print(f"Deleted {file_deleter.deleted_count} files.")
else:
    print("Exiting without deleting files.")


