import os

folder_path = r"E:\P_Photos"

files = os.listdir(folder_path)

count = 1

for file in files:
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        new_name = f"kedar_photo_{count}.jpg"
        new_path = os.path.join(folder_path, new_name)

        os.rename(file_path, new_path)

        print(f"Renamed {file} → {new_name}")

        count += 1