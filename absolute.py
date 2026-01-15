'''
This is how you work with an absolute path
To get a file path on a Mac, select the file in
Finder, then hold the Option (⌥) key and
right-click (or Control-click) to choose
"Copy [File Name] as Pathname"
'''

path = '/Users/diegoescobar/Desktop/dad_jokes.txt'

with open(path) as file:
    print(file.read())


