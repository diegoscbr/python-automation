from pathlib import Path

p = Path('.').resolve()

print(f"{p} is the working directory")

home = Path.home()
print(f"{home} is the home directory")

doc_path = home / 'Documents'
print(f"{doc_path} is the documents directory")

fiel_path = doc_path / 'my_file.txt'
print(f"{fiel_path} is the my_file path")

with open(fiel_path) as f:
    print(f.read())