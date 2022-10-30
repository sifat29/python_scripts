import os
from pathlib import Path 
from PIL import Image
import numpy as np
import argparse
"""
These are the library function that we need for this mean and standard devaition code
"os" module gives us all the functionalities to access the file directories.
"PIL" helps us to load the images
"Pathlib" gives us the path of the certain directory
"numpy" gives us the different kinds of mathmetical operational functions

"""
class Calculclate_Mean_Std:
    """
     A class which represents the calculation of mean and standard deviation
    """
    def __init__(self, file):
        self.file=file
        self.mean = np.array([0.,0.,0.])
        self.std = np.array([0.,0.,0.])
   
    """
     This is the mean and standard devaition calculation function. 
     This function can access the subdirectories of the folders and
     can calculate the mean and standard deviation of every folder of the subdirectory 
     Parameters
        ----------
        directory: str
            which holds the path of the root directory
    """
    def mean_std(self,directory):
        mean =self.mean
        std = self.std
        subdirectory=list(os.path.join(directory,f) for f in os.listdir(directory) if f.endswith('.jpg'))
        #file = list(file.rglob('*.jpg'))
        #print(subdirectory)
        for i in range(len(subdirectory)):
            # image = cv2.imread(str(file[i]))
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.open(subdirectory[i]).convert("RGB")
            image = np.array(image)
            image = image.astype(float) / 255.
            mean += np.mean(image, axis=(0, 1))
            std += np.std(image)
            print("Mean", mean)
        mean = (mean/len(subdirectory))
        print("final Mean =", mean)
        std = (std/len(subdirectory))   
        print("final std =", std)
    """
    This function is for Acessing the root directory.
    In this function we first access the root directory with os.path.join and list the directories
    then call the mean_std function for accessing the subdirectory and calculate
    """
    def root_directory(self):
        file = self.file
        file=list(os.path.join(file,f) for f in os.listdir(file))
        for i in range(len(file)):
            print(f"This is for {i} th folder.")
            self.mean_std(file[i])
            
            #mean_std()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This is for calculate the mean and standard deviation for each image in every folder')
    parser.add_argument('--root-dir', type=str, help='Path of images of root dir')
    args = parser.parse_args()
    root_dir = args.root_dir
    image_set = Calculclate_Mean_Std(root_dir)
    image_set.root_directory()
    #files = Path(r'F:/test_images')
    #x= Calculclate_Mean_Std(files)
    #x.root_directory()