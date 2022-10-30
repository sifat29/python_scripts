import numpy as np
import os
import torch
from torchvision import transforms
from PIL import Image

folders = list(os.path.join(data_path,f) for f in os.listdir(data_path))     # List of sub folders
            for idx, folder_name in enumerate(folders):
                #print(f"This is for {idx} th folder.")
                sub_dir_files = list(os.path.join(folder_name,f) for f in os.listdir(folder_name) if f.endswith('.jpg')) 
                for file_name in sub_dir_files:  
