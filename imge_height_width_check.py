import os
import cv2
data_path="E:/v2_data/crop"
folders = list(os.path.join(data_path,f) for f in os.listdir(data_path))     # List of sub folders
for root, folder_name in enumerate(folders):
    sub_directory_files = list(os.path.join(folder_name,f) for f in os.listdir(folder_name) if f.endswith('.jpg')) 
    for file_name in sub_directory_files:
        image = cv2.imread(file_name)
        image_name=file_name[:-4] + ".jpg"
        h, w = image.shape[0], image.shape[1]
        if (w<=400):
            print('Width of the iamge is less than 400 and image name is: ', image_name)
        elif (h<=420):
            print('Hieght of the iamge is less than 420 and image name is: ', image_name)
        elif (h/w<=1.05):
             print('Aspect Ratio of the iamge is less than 1.05 and image name is: ', image_name)
        elif (h/w>=1.8):
             print('Aspect Ratio of the iamge is higher than 1.80 and image name is: ', image_name)
        # else:
        #     print("OK",image_name)

       
        
