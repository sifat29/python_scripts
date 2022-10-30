import os
from random import choice
import shutil

#arrays to store file names
imgs =[]
xmls =[]

#setup dir names
crsPath = 'E:/v2_data/New_folder' #dir where images and annotations stored
trainimagePath = 'E:/v2_data/train_data2/images/train'
trainlabelPath = 'E:/v2_data/train_data2/labels/train'
valimagePath = 'E:/v2_data/train_data2/images/val'
vallabelPath = 'E:/v2_data/train_data2/labels/val'

#setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.7


#total count of imgs
totalImgCount = len(os.listdir(crsPath))/2

#soring files to corresponding arrays
for (dirname, dirs, files) in os.walk(crsPath):
    for filename in files:
        if filename.endswith('.txt'):
            xmls.append(filename)
        else:
            imgs.append(filename)


#counting range for cycles
countForTrain = int(len(imgs)*train_ratio)
countForVal = int(len(imgs)-countForTrain)
print("training images are : ",countForTrain)
print("Validation images are : ",countForVal)

#cycle for train dir
for x in range(countForTrain):

    fileJpg = choice(imgs) # get name of random image from origin dir
    fileXml = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir
    shutil.move(os.path.join(crsPath, fileJpg), os.path.join(trainimagePath, fileJpg))
    shutil.move(os.path.join(crsPath, fileXml), os.path.join(trainlabelPath, fileXml))

    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)


#cycle for test dir   
for x in range(countForVal):

    fileJpg = choice(imgs) # get name of random image from origin dir
    fileXml = fileJpg[:-4] +'.txt' # get name of corresponding annotation file

    #move both files into train dir
    shutil.move(os.path.join(crsPath, fileJpg), os.path.join(valimagePath, fileJpg))
    shutil.move(os.path.join(crsPath, fileXml), os.path.join(vallabelPath, fileXml))
    
    # remove files from arrays
    imgs.remove(fileJpg)
    xmls.remove(fileXml)
