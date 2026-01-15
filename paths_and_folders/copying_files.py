from pathlib import Path
import shutil

src = Path.home() / 'Desktop' / 'dad_jokes.txt'
dest = Path.home() / 'Desktop' / 'python-automation' / 'python_file_automations' /'copying_stuff'
'''
Always check if the source exists 
AND if the destination exists 
SO you DO NOT overrite it
'''
dest_file_path = dest / 'dad_jokes.txt'

if not(src.exists()):
    print('Source does not exist')
elif dest_file_path.exists():
    print('The file destination already exists')
else:
    shutil.copy(src,dest)
