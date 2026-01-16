from pathlib import Path
import shutil

dest = Path.home() / 'Desktop' / 'python-automation' /'python_file_automations' / 'moving_n_renaming' / 'doomed_folder'

if dest.exists():
    dest.rmdir()

p = Path.home() / 'Desktop' / 'python-automation' /'python_file_automations' / 'fun_with_folders'

if p.exists():
    #p.rmdir()
    shutil.rmtree(p)

