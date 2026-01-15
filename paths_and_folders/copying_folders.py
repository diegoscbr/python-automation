from pathlib import Path
import shutil

src = Path.home() / 'Desktop' / 'python-automation' / 'python_file_automations' / 'fun_with_folders'
dest = Path.home() / 'Desktop' / 'python-automation' /'python_file_automations' / 'copying_stuff'

shutil.copytree(src,dest, dirs_exist_ok=True)
