'''
A Python script that automates the organization of
folders and files in a user-specified directory
'''

#USE TEST FOLDER
from pathlib import Path
import shutil
from loader import Loader
import sys
import time


user = input('Specify a directory you want to organize: ')
path = Path(user)

if not path.exists():
    print("DIRECTORY DOES NOT EXIST")

else:
    print("Directory exists at:")
    print(f"{path}")
    loader = Loader("Cleaning...")
    loader.start()

    try:
        time.sleep(2)
        closet = path / 'closet'
        closet.mkdir(exist_ok=True, parents=True)
        print(f"Making closet: {closet}")
        time.sleep(2)
        print(f"Adding shelves...")
        text_files = closet / "text_files"
        text_files.mkdir(exist_ok=True, parents=True)
        time.sleep(1)
        print(f"text_files: {text_files}")
        time.sleep(1)
        csv_files = closet / "csv_files"
        csv_files.mkdir(exist_ok=True, parents=True)
        print(f"csv_files: {csv_files}")
        time.sleep(1)
        folders = closet / "folders"
        folders.mkdir(exist_ok=True, parents=True)
        print(f"folders: {folders}")

        #put appropriate file in a corresponding folder
        for item in path.iterdir():
            time.sleep(0.25)
            if item.is_dir() and item.stem == "closet":
                continue
            else:
                if item.is_file() and item.suffix == ".txt":
                    #rename into text_files
                    shutil.move(item, text_files / item.name)
                    print(f"Moved {item.name} to text_file shelf")
                elif item.is_file() and item.suffix == ".csv":
                    shutil.move(item, csv_files / item.name)
                    print(f"Moved {item.name} to csv_files shelf")
                elif item.is_dir() and "folder" in item.stem and "temp" not in item.stem:
                    shutil.move(item, folders / item.name)
                    print(f"Moved {item.name} to folder shelf")
                elif item.is_dir() and "temp"  in item.stem:
                    print(f"Dusting {item.name}")
                    shutil.rmtree(item)
                elif item.is_file() and item.suffix != ".txt" or item.suffix != ".csv":
                    shutil.move(item, closet / item.name)
                    print(f"Moved {item.name} to closet")
        time.sleep(2)
        print(f"Adding the last touches...")
    except KeyboardInterrupt:
        pass
    finally:
        loader.stop("Folder Cleanup Completed.")


