from pathlib import Path
new_folder = Path.home() / 'Desktop' / 'python-automation' / 'python_file_automations'
new_folder.mkdir(exist_ok=True)

another_folder = new_folder / 'fun_with_folders' / 'another_folder'
another_folder.mkdir(parents=True, exist_ok=True)