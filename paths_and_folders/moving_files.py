'''
The only diff between copying and moving is
that a move copys then deletes prev location
'''

from pathlib import Path
import shutil

src = Path.home() / 'Desktop' / 'python-automation' / 'python_file_automations' / 'copying_stuff' / 'dad_jokes.txt'
dest = Path.home() / 'Desktop' / 'python-automation' /'python_file_automations' / 'moving_n_renaming' / 'dad_jokes.txt'

if src.exists():
    shutil.move(src,dest)
