"""

new_data_loader.py is used to make a TripletFaceDataset, where each data point is a triplet
of an anchor image, a positive image, and a negative image. get_dataloader function return 
dataloaders and size of datasets.


TripletDataset:
---------------
---------------

Attributes:
-----------
root_dir: directory path
    Directory path of the dataset
df: pandas dataframe instance
    Pandas dataframe object initiated from a csv file that contains all information 
    about the directory tree of the dataset
num_triplets: int 
    Number of triplets to be created
training_triplets: list
    This list has all the randomly selected triplets. Each element of this list has a 
    structure of [anc_id, pos_id, neg_id, pos_class, neg_class, pos_name, neg_name]
    Here,
    anc_id      --> file name of the anchor image
    neg_id      --> file name of the positive image
    pos_id      --> file name of the negative image
    pos_class   --> assigned class value (during making csv file) for the sub-folder that contains
                    images of the "anchor/positive image" sample
    neg_class   --> assigned class value (during making csv file) for the sub-folder that contains
                    images of the "negative image" sample
    pos_name    --> name of the sub-folder in directory that contains images of the "positive image" sample
    neg_name    --> name of the sub-folder in directory that contains images of the "negative image" sample
transform: a dictionary object
    Transform as 2 keys: 'train' and 'valid'. Each key has a torchvision.transforms.transforms.Compose
    object as its value. This individual transformation will be applied consecutively on training and 
    validation dataset.

    
Parameters:
----------
root_dir: directory path
    Root directory path of the dataset
csv_name: directory path
    Directory of the csv file that has all information from dataset
num_triplets: int
    Number of triplets to be created
transform: dictionary
    Transformation to be applied on training and validation set

-------------


get_dataloader:
---------------
---------------

parameters:
-----------
train_root_dir: directory path (string)
    Root directory path of the training dataset
valid_root_dir: directory path (string)
    Root directory path of the validation dataset
train_csv_name: directory path (string)
    Directory path of the csv file of training data
valid_csv_name: directory path (string)
    Directory path of the csv file of validation data
num_train_triplets: int
    Number of triplets to be created from training dataset
num_valid_triplets: int
    Number of triplets to be created from validation dataset
batch_size: int
    Number of samples per batch
num_workers: int
    How many workers (core) will be used

Returns:
--------
dataloaders: dictionary object
    A dictionary, consists of 2 keys - 'train', 'valid'
    'train' --> dataloader object, iterable over training dataset
    'valid' --> dataloader object, iterable over validation dataset
data_size: dictionary object
    A dictionary, consists of 2 keys - 'train', 'valid'
    'train' --> length of train dataset
    'valid' --> length of validation dataset


"""


import torch
import pandas as pd
from torch.utils.data import Dataset
import numpy as np
import os
from PIL import Image
from torchvision import transforms
from collections import deque


class TripletFaceDataset(Dataset):
    def __init__(self, root_dir, csv_name, num_triplets, transform=None):
        self.root_dir = root_dir
        self.df = pd.read_csv(csv_name)
        self.num_triplets = num_triplets
        self.training_triplets = self.generate_triplets(self.df, self.num_triplets)
        self.transform = transform

    @staticmethod
    def generate_triplets(df, num_triplets):
        face_classes = {}
        triplets = []
        classes = df['class'].unique()

        
        for single_class in list(df.groupby('class')):
            class_name = single_class[0]
            class_data = list(single_class[1]['id'].values)
            face_classes[class_name] = class_data
        

        """
        '''
        This codeblock will also create the dictionary to store 
        individual class name and corresponding image names

        '''
        data_list = []
        deque(map(lambda x: data_list.append(list(x[1]['id'].values)), list(df.groupby('class'))))
        face_classes = dict(zip(classes, data_list))
        """
        
        for _ in range(num_triplets):
            pos_class = np.random.choice(classes)
            while len(face_classes[pos_class]) < 2:
                pos_class = np.random.choice(classes)
            neg_class = np.random.choice(list(set(classes)-set([pos_class])))

            pos_name = df.loc[df['class'] == pos_class, 'name'].values[0]
            neg_name = df.loc[df['class'] == neg_class, 'name'].values[0]

            ianc, ipos = np.random.choice(len(face_classes[pos_class]), size=2, replace=False)
            ineg = np.random.choice(len(face_classes[neg_class]))
            
           

            anc_id = face_classes[pos_class][ianc]
            pos_id = face_classes[pos_class][ipos]
            neg_id = face_classes[neg_class][ineg]

            triplets.append([anc_id, pos_id, neg_id, pos_class, neg_class, pos_name, neg_name])
        
        return triplets
    
    def __getitem__(self, idx):

        anc_id, pos_id, neg_id, pos_class, neg_class, pos_name, neg_name = \
            self.training_triplets[idx]
        
        anc_img = os.path.join(self.root_dir, str(pos_name).zfill(3), str(anc_id))
        pos_img = os.path.join(self.root_dir, str(pos_name).zfill(3), str(pos_id))
        neg_img = os.path.join(self.root_dir, str(neg_name).zfill(3), str(neg_id))

        anc_img = np.array(Image.open(anc_img).convert('RGB'))
        pos_img = np.array(Image.open(pos_img).convert('RGB'))
        neg_img = np.array(Image.open(neg_img).convert('RGB'))
        # print('image shape: ', anc_img.shape)
        # print('dtype: ', type(anc_img.dtype))
        # raise Exception('stop')
        

        pos_class = torch.from_numpy(np.array([pos_class]).astype('long'))
        neg_class = torch.from_numpy(np.array([neg_class]).astype('long'))

        sample = {'anc_img': anc_img, 'pos_img': pos_img, 'neg_img': neg_img,
                        'pos_class': pos_class, 'neg_class': neg_class}
        
        if self.transform:
            sample['anc_img'] = self.transform(sample['anc_img'])
            sample['pos_img'] = self.transform(sample['pos_img'])
            sample['neg_img'] = self.transform(sample['neg_img'])

        return sample
    
    def __len__(self):
        return len(self.training_triplets)
    

def get_dataloader(train_root_dir, valid_root_dir,
                    train_csv_name, valid_csv_name,
                    num_train_triplets, num_valid_triplets,
                    batch_size, num_workers):

    data_transforms = {
        'train': transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(224),
            transforms.RandomRotation(15, interpolation=transforms.InterpolationMode.BILINEAR), 
            transforms.RandomResizedCrop(224, scale=(0.25, 1.0), ratio=(0.95, 1.05)),
            transforms.RandomHorizontalFlip(p=0.4),
            transforms.RandomVerticalFlip(p=0.4),
            transforms.ToTensor(),
            # transforms.Normalize(mean=[0.485, 0.456, 0.406],
            #                     std=[0.229, 0.224, 0.225])
        ]),

        'valid': transforms.Compose([
            transforms.ToPILImage(),
            transforms.Resize(224),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            # transforms.Normalize(mean=[0.485, 0.456, 0.406],
            #                     std=[0.229, 0.224, 0.225])
        ])
    }

    face_dataset = {
        'train': TripletFaceDataset(root_dir=train_root_dir,
                                    csv_name=train_csv_name,
                                    num_triplets=num_train_triplets,
                                    transform=data_transforms['train']),
        'valid': TripletFaceDataset(root_dir=valid_root_dir,
                                    csv_name=valid_csv_name,
                                    num_triplets=num_valid_triplets,
                                    transform=data_transforms['valid'])
    }

    dataloaders = {
        x: torch.utils.data.DataLoader(face_dataset[x], batch_size=batch_size, shuffle=False, num_workers=num_workers)
        for x in ['train', 'valid']
    }

    data_size = {x: len(face_dataset[x]) for x in ['train', 'valid']}
    
    

    return dataloaders, data_size 





