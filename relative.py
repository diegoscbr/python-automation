'''
This shows how a relative filepath is described
Note we are currently in /Desktop/python-automation/Product Sales Tracker
So we need to go to ../../dad_joke.txt to be at the desktop location
'''
absolute_path = '/Users/diegoescobar/Desktop/dad_jokes.txt'
relative_path = '../dad_jokes.txt'
with open(relative_path, 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())