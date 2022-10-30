from genericpath import isdir
from PIL import Image
import os, sys

path = "E:/v2_data/lanmark_annotation2"
save_path = "E:/v2_data/Resized_landmark_annotation2"
images = os.listdir(path)

if not os.path.isdir(save_path):
    os.makedirs(save_path)


for image in images:
    image_path = os.path.join(path, image)
    iamge_save_path = os.path.join(save_path, image)
    if image.split(".")[1] not in ["jpg", "png"]:
        continue
    if os.path.exists(image_path):
        im = Image.open(image_path)
        image_resized = im.resize((224,224))
        image_resized.save(iamge_save_path, quality=90)

print("saved")