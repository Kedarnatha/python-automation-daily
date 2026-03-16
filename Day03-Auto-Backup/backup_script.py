import os
import shutil
from datetime import datetime

source_folder = r"D:\projects\Python_Automation_Projects"
backup_root = r"D:\Backup"

date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

backup_folder = os.path.join(backup_root, f"backup_{date}")

if not os.path.exists(backup_folder):
    shutil.copytree(source_folder, backup_folder)
    print("Backup completed successfully!")
else:
    print("Backup folder already exists.")
    