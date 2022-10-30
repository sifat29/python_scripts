import os
data_path="E:/v2_data/clean"
folders = list(os.path.join(data_path,f) for f in os.listdir(data_path))     # List of sub folders
for root, folder_name in enumerate(folders):
    sub_directory_files = list(os.path.join(folder_name,f) for f in os.listdir(folder_name) if f.endswith('.jpg')) 
    for file_name in sub_directory_files:
        print(file_name)
        os.remove(file_name)

# for folder in folders:
#     for file in os.listdir(folder):
#         if file.endswith('.jpg'):
#             os.remove(file) 



