from pathlib import Path
import shutil

src = Path.home() / 'Desktop' / 'python-automation' / 'python_file_automations' / 'copying_stuff' / 'another_folder'
dest = Path.home() / 'Desktop' / 'python-automation' /'python_file_automations' / 'moving_n_renaming' / 'another_folder'

if src.exists():
    shutil.move(src, dest)