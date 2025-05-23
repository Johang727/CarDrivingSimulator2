import sys
from zipfile import ZipFile
from pathlib import Path

if len(sys.argv) != 2:
    sb3File = "CarDrivingSimulator2.sb3"  # Just make it look for this specific file, rather than ask for an input
else:
    sb3File = sys.argv[1]

sb3Path = Path(sb3File)
if not sb3Path.is_file():
    sys.exit(f"File \"{sb3Path.name}\" does not exist")
sb3Dir = sb3Path.parent

with ZipFile(sb3Path, 'r') as zipFile:
    zipFile.extractall(sb3Dir / "Assets")
