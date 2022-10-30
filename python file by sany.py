import csv
import os
import argparse
import time
​
​
​
class make_data_csv:
    def __init__(self, main_dir, save_dir, field_names = ['id', 'name', 'ext', 'class']):
        self.main_dir = main_dir    # Root directory of the dataset
        self.save_dir = save_dir    # Directory for saving a csv file where all the info of the dataset will be stored
        self.field_names = field_names  # This information from each data point will be kept in the csv file
    
    def create_csv(self):
        data_path = self.main_dir
        output_path = self.save_dir
        current_path_tree = list(os.walk(data_path))    # Sub folders, files from root directory
        folders = current_path_tree[0][1]   # List of sub folders
        
        
        with open(output_path, 'w', encoding='UTF8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.field_names)
            writer.writeheader()    # Writing header of the csv file as per given field names
            for idx, folder_name in enumerate(folders):
                sub_dir_files = list(current_path_tree[idx+1][2])   # List of images names for an individual cow
                label = idx # Assigned class, will be increased sequentially for each cow as per the sequential 
                            # arrangement of fub folders form the dataset
                for file_name in sub_dir_files:
                    dictionary_data = dict()
                    (name, extension) = file_name.split('.', 1)
                    data = [name, folder_name, extension, label]
​
                    if len(data) != len(self.field_names):
                        raise Exception('Length of a row does not match with number of fields')
​
                    data = zip(self.field_names, data)  # Each field name and corresponding data will be merged to create a tuple
                                                        # A list (of tuple) combined with (field name, data) tuples for all the fields will be created
                    dictionary_data = dict(data)    # Previously created list of tuples will be converted as a dictionary to be writen as a row in the csv file
                    writer.writerow(dictionary_data)
​
​
if __name__ == '__main__':
​
    # main_dir_path = 'D:/Himel_APS/FaceNet/datasets/muzzleDataset/muzzle_dataset/test_data'
    # save_dir_path = 'D:/Himel_APS/FaceNet/repo/facenet-master/facenet-master'
    # data_set_excel = make_data_csv(main_dir_path, save_dir_path)
    # data_set_excel.create_csv()
    init_time = time.time()
    parser = argparse.ArgumentParser(description='Dataset info creating for cow face detection project')
    parser.add_argument('--root-dir', type=str, help='Path to dataset root dir')
    parser.add_argument('--save-dir', type=str, help='Directory for saving the final csv final')
    args = parser.parse_args()
    
    root_dir = args.root_dir
    save_dir = args.save_dir
    dataset_excel = make_data_csv(root_dir, save_dir)        
    dataset_excel.create_csv()
    final_time = time.time()
    print('Elapsed time: {0:.4f} seconds'.format(final_time-init_time))