from dataset_pipeline import*

# root_dir = '/home/himel/Documents/Adorsho_pranisheba/Data_Analysis/pipeline_annoted/json_files/'
root_dir = open("C:/Users/IT BD/Desktop/all data jason/Annotaion_json_files")
# root_dir = '/home/himel/Documents/Adorsho_pranisheba/Data_Analysis/pipeline_annoted/json_all_data.json'
bolus_dataset = Bolus_dataset(root_dir=root_dir, consecutive_threshold=2, sampling_freq=2)
bolus_dataset.data.to_json('json_file.json')
# dataset = bolus_dataset.create_dataset(label_cols=['rumination'], normalized=True)
# np.save('all_data.npy', dataset)
