'''
In python renaming files is the same as moving them
why? because name and location are the same
'''


from pathlib import Path
import shutil

src = Path.home() / 'Desktop' / 'python-automation' / 'python_file_automations' / 'moving_n_renaming' / 'dad_jokes.txt'
dest = Path.home() / 'Desktop' / 'python-automation' /'python_file_automations' / 'moving_n_renaming' / 'bad_jokes.txt'

if src.exists():
    shutil.move(src, dest)