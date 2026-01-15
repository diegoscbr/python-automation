from pathlib import Path
from datetime import datetime
path = Path.home() / 'Desktop' / 'python-automation'

for item in path.iterdir():
    if item.is_file() and item.suffix == '.py':
        print('============================')
        print('============================')
        print(item.stem, 'is a python file')
        stats = item.stat()
        print('Size',stats.st_size,'bytes')
        print('Last Modified',datetime.fromtimestamp(stats.st_mtime))
    if item.is_dir():
        print(item.name, 'is a directory')

    if 'read' in item.name.lower():
        print(item.name, 'contains the word READ')