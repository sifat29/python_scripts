from PIL import Image
import numpy as np
import os
dst_img = "F:/test_images/027"
arr_mean = np.array([0.,0.,0.])
#listing files in images folder
list_img = os.listdir(dst_img)
#iterating over dst_image to get the images as arrays
for image in sorted(list_img):
    [file_name, ext] = os.path.splitext(image) #splitting file name from its extension
    arr = np.array(Image.open(os.path.join(dst_img, image))) #creating arrays for all the images
    [h, w] = np.shape(arr)[0:2]#calculating height and width for each image
    arr_dim = arr.ndim #calculating the dimension for each array
    arr_shape = arr.shape #calculating the shape for each array
    if arr_dim == 3:
        arr_mean += np.mean(arr)
        print("overall Mean", arr_mean)
final_mean = arr_mean/list_img
print(final_mean) 