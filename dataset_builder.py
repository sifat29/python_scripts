from pathlib import Path
import shutil
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
from random import choice

class Datadistributation:
    def __init__(self, main_src = None, trg_destination = None, main_source = None, img_train = None, img_val = None, label_train = None, label_val = None):
        self.main_src = main_src
        self.trg_destination = trg_destination
        # print('Debug-1: The type of destination folder: ', type(trg_destination))
        
        

    def data_transfer(self):
            # defining source and destination path
            main_src = self.main_src
            trg_destination = self.trg_destination

            # all the folders name in main_src
            files=os.listdir(main_src)
            # print(files)

            for i in files:
                each_source = (os.path.join(main_src,i))
                # print(each_source)
                files1=os.listdir(each_source)
                # print(files1)
                for fname in files1:
                    path_of_each_file = os.path.join(each_source,fname)
                    print(path_of_each_file)
                    # copying all the files in destination
                    shutil.copy2(path_of_each_file, trg_destination)
            print("********copy & paste done*********")

    def make_data_set(self, all_contents, image_train, label_train, image_val, label_val):
        
        #arrays to store file names
        imgs =[]
        txt =[]

        main_path = all_contents # dir where images and annotations stored

        #setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
        train_ratio = 0.7

        #soring files to corresponding arrays
        for (dirname, dirs, files) in os.walk(main_path):
            for filename in files:
                if filename.endswith('.txt'):
                    txt.append(filename)
                else:
                    imgs.append(filename)

        #counting range for cycles
        count_for_train = int(len(imgs)*train_ratio)
        count_for_val = int(len(imgs)-count_for_train)
        print("training images are : ",count_for_train)
        print("Validation images are : ",count_for_val)

        #cycle for train dir
        for x in range(count_for_train):

            file_jpg = choice(imgs) # get name of random image from origin dir
            file_text = file_jpg[:-4] +'.txt' # get name of corresponding annotation file

            #move both files into train dir
            shutil.move(os.path.join(main_path, file_jpg), os.path.join(image_train, file_jpg))
            shutil.move(os.path.join(main_path, file_text), os.path.join(label_train, file_text))

            # remove files from arrays
            imgs.remove(file_jpg)
            txt.remove(file_text)

        #cycle for test dir   
        for _ in range(count_for_val):

            file_jpg = choice(imgs) # get name of random image from origin dir
            file_text = file_jpg[:-4] +'.txt' # get name of corresponding annotation file

            #move both files into train dir
            shutil.move(os.path.join(main_path, file_jpg), os.path.join(image_val, file_jpg))
            shutil.move(os.path.join(main_path, file_text), os.path.join(label_val, file_text))
            
            # remove files from arrays
            imgs.remove(file_jpg)
            txt.remove(file_text)
        print("******Your Data Set is ready*******")




# shows dialog box and return the path
path1 = askdirectory(title='Select Main Folder where all subfolders are stored')
path2 = askdirectory(title='Select Destination Folder')

main_src, trg_destination = path1, path2    

files_transfer = Datadistributation(main_src, trg_destination)
files_transfer.data_transfer()

print("Do you want to split the data's for Train and Validation?  ")
opinion = input("yes or no: ")

if opinion == "yes":
    all = askdirectory(title='Select the folder where all images and text file stored')
    os.chdir(all)
    os.mkdir('image')
    os.mkdir('image/train')
    os.mkdir('image/val')
    os.mkdir('label')
    os.mkdir('label/train')
    os.mkdir('label/val')

    dir_path = Path(all)
    path3 = dir_path / "image" / "train"
    # print(path3)
    path4 = dir_path / "image" / "val"
    # print(path4)
    path5 = dir_path / "label" / "train"
    # print(path5)
    path6 = dir_path / "label" / "val"
    # print(path6)
elif opinion == "no":
    print("Image Copy&Paste Successful")
else:
    print("Wrong Input. Type yes or no in lower case")


all_contents, image_train, label_train, image_val, label_val = all, path3, path5, path4, path6

make_data_set = Datadistributation(main_src = None, trg_destination= None)
make_data_set.make_data_set(all_contents, image_train, label_train, image_val, label_val)