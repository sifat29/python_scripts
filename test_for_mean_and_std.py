from pathlib import Path
import numpy as np
import cv2


Files_dir = Path(r'F:/test_images/027')
files = list(Files_dir.rglob('*.jpg'))
mean = np.array([0.,0.,0.])
#temp_mean = np.array([0.,0.,0.])
#Temp_std = np.array([0.,0.,0.])
std = np.array([0.,0.,0.])

number_of_samples = len(files)

for i in range(number_of_samples):
    image = cv2.imread(str(files[i]))
    print("this is image shape",image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("this is after conversion image shape",image.shape)
    image = image.astype(float) / 255.
    #for j in range (3):
    mean += np.mean(image, axis=(0, 1))
    print("this mean is indivitual", mean)
    std += np.std(image)
    print("this std is indivitual", std)
#print("Mean", mean)
mean = (mean/number_of_samples)
print("final Mean =", mean)
print("final std =", (std/number_of_samples))