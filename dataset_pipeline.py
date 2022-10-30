import numpy as np
import pandas as pd
import os
import random

class Bolus_dataset:
    def __init__(self, root_dir, window_size=128, consecutive_threshold=2, window_missing_threshold=0.2, allowed_consecutive_missing_data_points=3, sampling_freq=2):
        self.root_dir = root_dir
        self.window_size = window_size
        self.consecutive_threshold = consecutive_threshold
        self.window_missing_threshold = window_missing_threshold
        self.allowed_consecutive_missing_data_points = allowed_consecutive_missing_data_points
        self.sampling_freq = sampling_freq
        
        def read_json_file(file_name):
            file = pd.read_json(f'{self.root_dir}/{file_name}', convert_dates=False)
            return file
        
        if self.root_dir.endswith('.json'):
            print(self.root_dir)
            # self.data = read_json_file(self.root_dir)
            self.data = pd.read_json(self.root_dir, convert_dates=False)
        else:
            json_files = list(filter(lambda x : x.endswith('.json'), sorted(os.listdir(root_dir))))
            print(json_files)
            self.data = pd.concat(list(map(lambda x : read_json_file(x), json_files)), axis=0)
        self.data.sort_values(by='timestamp', ignore_index=True, inplace=True)        
        self.data.dropna(inplace=True)

    def create_dataset(self, feature_cols=['x', 'y', 'z'], label_cols=['rumination'], normalized=True):
        starting_index = 0
        data_set = []
        # end_flag = False
        loop_count = 0
        highest_value = 127
        interval = 255
        self.data[feature_cols] = self.data[feature_cols].apply(lambda x : (x+highest_value)/interval)
        
        while(True):
            data_chunk = self.data.iloc[starting_index : starting_index+self.window_size].copy(deep=True)
            window_expected_data_points = (data_chunk['timestamp'].max()-data_chunk['timestamp'].min()) * self.sampling_freq + 1
            missing_ratio = (window_expected_data_points - self.window_size) / window_expected_data_points


            if (sum(data_chunk['timestamp'].diff() > self.consecutive_threshold) == 0 and missing_ratio > self.window_missing_threshold):
                starting_index += 1  # If there are so many missing data where each one less than consecutive threshold
                
            elif (sum(data_chunk['timestamp'].diff() > self.consecutive_threshold) > self.consecutive_threshold or missing_ratio > self.window_missing_threshold):
                starting_index = data_chunk[data_chunk['timestamp'].diff() > self.consecutive_threshold].index[-1] + 1
            else:
                data_set.append([data_chunk[feature_cols].values, int(data_chunk[label_cols].values.any())])
                starting_index += self.window_size
            # print(len(data_set))
            if (starting_index+self.window_size) > len(self.data)-1:
                break
            loop_count += 1
        return data_set

    def train_test_data(self, feature_cols=['x', 'y', 'z'], label_cols=['rumination'], normalized=True):
        data_set = self.create_dataset(feature_cols=feature_cols, label_cols=label_cols, normalized=normalized)
        data_zero = list(filter(lambda x : x[-1] == 0, data_set))
        data_ones = list(filter(lambda x : x[-1] == 1, data_set))
        print(f'0 in dataset: {len(data_zero)}  || 1 in dataset: {len(data_ones)}')

        val_data_zero_index = random.sample(range(len(data_zero)), 150)
        val_data_one_index = random.sample(range(len(data_ones)), 150)
        train_data_zero_index = [x for x in range(len(data_zero)) if x not in val_data_zero_index]
        train_data_one_index = [x for x in range(len(data_ones)) if x not in val_data_one_index]

        val_data_zero = list(map(data_zero.__getitem__, val_data_zero_index))
        val_data_one = list(map(data_ones.__getitem__, val_data_one_index))
        train_data_zero = list(map(data_zero.__getitem__, train_data_zero_index))
        train_data_one = list(map(data_ones.__getitem__, train_data_one_index))
        train_data = train_data_zero + train_data_one
        val_data = val_data_zero + val_data_one
        random.shuffle(train_data)
        random.shuffle(val_data)
        return train_data, val_data


