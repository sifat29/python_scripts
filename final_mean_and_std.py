import os
from pathlib import Path 
from PIL import Image
import numpy as np
import cv2
class Calculclate_Mean_Std:
    def __init__(self, file):
        self.file=file
        self.mean = np.array([0.,0.,0.])
        self.std = np.array([0.,0.,0.])
   

    def mean_std(self):
        file= self.file
        mean =self.mean
        std = self.std
        file=list(os.path.join(file,f) for f in os.listdir(file) if f.endswith('.jpg'))
        #file = list(file.rglob('*.jpg'))
        print(file)
        for i in range(len(file)):
            # image = cv2.imread(str(file[i]))
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.open(file[i]).convert("RGB")
            image = np.array(image)
            image = image.astype(float) / 255.
            mean += np.mean(image, axis=(0, 1))
            std += np.std(image)
            print("Mean", mean)
        mean = (mean/len(file))
        print("final Mean =", mean)
        std = std/len(file)   
        print("final std =", std)

if __name__ == '__main__':
    files = Path(r'F:/test_images/027')
    x= Calculclate_Mean_Std(files)
    x.mean_std()