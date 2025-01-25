import sys
from zipfile import ZipFile
from pathlib import Path
import shutil
import re
from datetime import datetime
import os



def repackage_sb3(assets_folder, output_file):
    with ZipFile(output_file, 'w') as sb3:
        for file in assets_folder.glob('**/*'):
            print(f"Wrote {file}")
            sb3.write(file, file.relative_to(assets_folder.parent))

def create_backup(output_file):
    backups_folder = Path("Backups")
    backups_folder.mkdir(exist_ok=True)  # Create the "Backups" folder if it doesn't exist
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    backup_file = backups_folder / f"CarDrivingSimulator2{timestamp}.sb3"
    if Path(output_file).exists():
        shutil.copy(output_file, backup_file)
        print(f"Backup created: {backup_file}")


assets_folder = Path("Assets/")
output_file = "CarDrivingSimulator2.sb3"

if not assets_folder.is_dir():
    print('Error, Assets folder missing!')
    sys.exit('Abort.')

if os.path.exists('CarDrivingSimulator2.sb3'):
    user_conformation = input("CarDrivingSimulator2.sb3 will be overwritten, are you sure you would like to proceed? (Y/n)")
    if re.match('[Yy]', user_conformation):
        create_backup(f"{output_file}")  # Create a backup before repackaging
        print('Packaging file...')
        repackage_sb3(assets_folder, output_file)
        print('Success!')
    else:
        print('Operation canceled, no files overwritten.')
else:
    print('Packaging file...')
    repackage_sb3(assets_folder, output_file)
    print('Success!')

print('Ensure to open the .sb3 to allow TurboWarp to handle file compression!')
