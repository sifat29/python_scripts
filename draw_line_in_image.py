# import cv2
# import os

# image = cv2.imread("F:/resized_images/200081_008.jpg")
# cv2.line(image, (110,51), (105,174), (0,0,255), 2)
# cv2.line(image, (167,116), (55,114), (255,0,0), 2)
# cv2.imshow("image", image)  
# cv2.imwrite('F:/test_image/200081_008.jpg', image)
# cv2.waitKey(0)
# import necessary libraries
import pandas as pd
import os
import glob
from pathlib import Path 
import cv2

# use glob to get all the csv files
# in the folder
Path = "E:/v2_data/Resized_landmark_annotation"
save_path="F:/test_redraw_images"
csv_files = glob.glob(os.path.join(Path, "*.csv"))
for i in csv_files:
	# name=i.split("\\")[1].split(".")[0] 
	name=i.split(".")[0] 
	# print(name)
	df = pd.read_csv(i) 
	New_df=df[['BX', 'BY']]
	X1Y1=New_df.iloc[0]
	X2Y2=New_df.iloc[1]
	X3Y3=New_df.iloc[2]
	X4Y4=New_df.iloc[3]
	# cv2.namedWindow("output", cv2.WINDOW_NORMAL)
	# cv2.resizeWindow('output', 400,400)
	image = cv2.imread(os.path.join(name + "." +'jpg'))
	cv2.line(image, (X1Y1), (X2Y2), (0,0,255), 2)
	cv2.line(image, (X3Y3), (X4Y4), (255,0,0), 2)
	# cv2.imshow("output", image)
	os.chdir(save_path)  
	name = name.split("\\")[1]
	cv2.imwrite((name +".jpg"),image)
	cv2.waitKey(0)

		


	

    # print the location and filename
  
    # print('File Name:', f.split("\\")[-1])
