import os

directory_path = r'C:\Users\Nikhil\Desktop\Learning\Python'
entries = os.listdir(directory_path)

print("Full paths of entries in the directory:")
for entry in entries:
    full_path = os.path.join(directory_path, entry)
    print(full_path)
