from pathlib import Path
import numpy as np
import cv2


Files_dir = Path(r'F:/test_images/027')
files = list(Files_dir.rglob('*.jpg'))
mean = np.array([0.,0.,0.])
Temp_std = np.array([0.,0.,0.])
std = np.array([0.,0.,0.])

number_of_samples = len(files)

# for i in range(number_of_samples):
#     image = cv2.imread(str(files[i]))
#     print("this is image shape",image.shape)
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     print("this is after conversion image shape",image.shape)
#     image=(np.reshape(-1,3))
#     image = image.astype(float) / 255.
#     #for j in range (3):
#     print("image mean",np.mean(image,axis=2).shape)
#     mean = np.add(mean,np.mean(image))
#     #print("this mean is indivitual", mean)
#     std += np.std(image)
#     print("this std is indivitual", std)
    #Temp_std[j] +=((image[:,:,j]-mean[j]**2).sum()/(image.shape[0]*image.shape[1]))
# print("Mean", mean)
# mean = (mean/number_of_samples)
# std = (std/number_of_samples)
# for i in range(number_of_samples):
#     image = cv2.imread (str(files[i]))
#     image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     image = image.astype(float)/255.
#     for j in range(3):
#         Temp_std[j] +=((image[:,:,j]-mean[j]**2).sum()/(image.shape[0]*image.shape[1]))

# std = np.sqrt(Temp_std/number_of_samples)
# print("final Mean =", mean)
# print("final std =", std)

print("this is with the loop/n")
print("/////////////////")

for i in range(number_of_samples):
    image = cv2.imread(str(files[i]))
    print("this is for image shape",image.shape)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    print("this is after conversion image shape",image.shape)
    image = image.astype(float) / 255.
    for j in range (3):
        mean[j] += np.mean(image[:,:,j])
        print("this mean is indivitual", mean[j])
mean = (mean/number_of_samples)
for i in range(number_of_samples):
    image = cv2.imread (str(files[i]))
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image = image.astype(float)/255.
    for j in range(3):
        Temp_std[j] +=((image[:,:,j]-mean[j]**2).sum()/(image.shape[0]*image.shape[1]))
        print("this is for temp_std",Temp_std[j])
std = np.sqrt(Temp_std/number_of_samples)
print("final Mean =", mean)
print("final std =", std)




