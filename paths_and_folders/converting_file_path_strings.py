from pathlib import Path
# this is a string
# /Users/diegoescobar/Desktop/python-automation/paths_and_folders
#this is a raw string
p = r'/Users/diegoescobar/Desktop/python-automation/paths_and_folders'

path = Path(p)

if path.exists():
    print('I exist!')

