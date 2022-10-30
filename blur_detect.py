import cv2
import os
from PIL import Image
directory='E:/v2_data\crop (335-340-371-385)200337'
subdirectory=list(os.path.join(directory,f) for f in os.listdir(directory) if f.endswith('.jpg'))
threshold=100
def variance_of_laplacian(image):
	# compute the Laplacian of the image and then return the focus
	# measure, which is simply the variance of the Laplacian
	return cv2.Laplacian(image, cv2.CV_64F).var()
for i in range(len(subdirectory)):
    image = cv2.imread(subdirectory[i])
    convert_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    fm = variance_of_laplacian(convert_image)
    text = "Not Blurry"
	# if the focus measure is less than the supplied threshold,
	# then the image should be considered "blurry"
    if fm < threshold:
        text = "Blurry"
	# show the image
    cv2.putText(image, "{}: {:.2f}".format(text, fm), (10, 30),
	    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)
    cv2.imshow("Image", image)
    key = cv2.waitKey(0)
    


