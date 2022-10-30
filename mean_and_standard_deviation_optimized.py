import os
#from pathlib import Path 
from PIL import Image
import numpy as np
import argparse
"""
These are the library function that we need for this mean and standard devaition code
"os" module gives us all the functionalities to access the file directories.
"PIL" helps us to load the images
"numpy" gives us the different kinds of mathmetical operational functions

"""
class Calculclate_Mean_Std:
    """
     A class which represents the calculation of mean and standard deviation
     Methods
    -------
     def__init__ : 
     Parameters
        root: str
        func_name:str
        func_name basically is the option that we will give in the command line(mean or std)
     self : the constructor object; its pramater is the file and self represents the instance of the class 
     
     mean_std()
      This function is for Acessing the root directory.
      In this function we first access the root directory with os.path.join and list the directories
      then call the mean_std function for accessing the subdirectory and calculate
      which holds the path of the root directory
      then the subdirectories of the folders are accessed and
      can calculate the mean and standard deviation of every folder of the subdirectory 
      if typing error in argument(mean or std), will show exception error

    """
    def __init__(self, root,func_name):
        self.root = root
        self.func_name = func_name
        self.mean = np.array([0.,0.,0.])
        self.std = np.array([0.,0.,0.])

    def mean_std(self):
        mean = self.mean
        std = self.std
        data_path = self.root
        func_name = self.func_name.lower()
        if (func_name == "mean" or func_name == "std"):
            folders = list(os.path.join(data_path,f) for f in os.listdir(data_path))     # List of sub folders
            for idx, folder_name in enumerate(folders):
                #print(f"This is for {idx} th folder.")
                sub_dir_files = list(os.path.join(folder_name,f) for f in os.listdir(folder_name) if f.endswith('.jpg')) 
                for file_name in sub_dir_files:   
                    image = Image.open(file_name).convert("RGB")
                    image = np.array(image)
                    image = image.astype(float) / 255.
                    mean += np.mean(image, axis=(0, 1))
                    std += np.std(image)
                    # if(func_name== "mean"):
                    #     print("Mean",mean)
                if(func_name == "mean"):
                    mean = (mean/len(sub_dir_files))
                    print("final Mean =", mean)
                if(func_name == "std"):
                    std = (std/len(sub_dir_files))   
                    print("final Std =", std)
        else:
            raise Exception('Allowed functions: mean or std')
    
            

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is for calculate the mean and standard deviation for each image in every folder')
    parser.add_argument('--root-dir', type = str, help ='Path of images of root dir')
    parser.add_argument('--func-name',type = str,help ='This is for mean or std')
    args = parser.parse_args()
    root_dir = args.root_dir
    func_name = args.func_name
    image_set = Calculclate_Mean_Std(root_dir,func_name)
    image_set.mean_std()
    #files = Path(r'F:/test_images')
   