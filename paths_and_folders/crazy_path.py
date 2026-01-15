'''
One of the potential issues of
creating file paths with python
is to create one that doesn't exist
'''

from pathlib import Path

crazy_path = Path.home() / 'I' / 'dont' / 'exist.csv'
print(crazy_path)

with open(crazy_path) as f:
    print(f.read())
