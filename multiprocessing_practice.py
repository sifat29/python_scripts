import csv
from operator import itemgetter
import os
def list_files(dir):
    print(f"Listing files in {dir}")
    r = []
    d = []
    for root, subdirectories, files in os.walk(dir):
        count=0
        for file in files:
            count=count+1
            subdir = os.path.join(root, file)
            print(subdir)
            subdir = subdir.split("\\")
            subdir.pop(0)
            folder_name = subdir[0]
            id = subdir[0].split("_")
            print(id)
            id = int(id[1])-1
            subdir_file = subdir[1].split(".")
            d = [subdir[1], f"{folder_name}", subdir_file[1], f"{id}"]
            # print(subdir[1], f'{folder_name}', subdir_file[1], f'{id}')
            r.append(d)
    print("total no", count)
    return sorted(r, key=itemgetter(3))
header = ["File Name", "Folder Name", "Extension", "Employee_ID"]
data = list_files(r"E:/problem_4_dir")
print(data)
print("data")


def write_csv(header, data):
    with open("info.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    # write multiple rows
    writer.writerows(data)


