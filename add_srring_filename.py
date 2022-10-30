import os
from os import path

path_to_directory = "F:/test_images/027"

for file in os.listdir(path_to_directory):
    name , extension = path.splitext(file)
    first_name, last_name = name.split('_')
    last_name = last_name.zfill(3)
    new_name = first_name + "_" + last_name + extension
    os.rename(os.path.join(path_to_directory,file),os.path.join(path_to_directory,new_name))
    # print(new_name)
            
    

