import os
import shutil

crop_path = r"F:/yolo_test/crop"
clean_path = r"F:/yolo_test/clean"

clean_from_cropped_path = r'F:/yolo_test/yolo_file_from_crop_to_clean'

count = 0

path_dirs = list(os.walk(crop_path))[1:]
for dirs in path_dirs:

    dir = dirs[0]
    files = dirs[2]

    savedir=os.path.join(clean_from_cropped_path, os.path.basename(dir))
    if not os.path.isdir(savedir):
        os.makedirs(savedir)
    for name in files:
        source=os.path.join(clean_path, os.path.basename(dir), name)
        destination= os.path.join(savedir, name)
        try:
            shutil.copy(source,destination)
        except:
            print(name)
print('Value of count: ', count)

        
       






   
           