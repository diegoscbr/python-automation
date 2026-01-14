print("THIS IS A PYTHON TEXT FILE EDITOR")
filename = input("Give file a name\n")
filename = filename + ".txt"
print(f"File name is {filename}")
print("USAGE: ")
print("Press i to write to file")
print("Press x to quit writing to file")
print("Press q to quit the program")
if filename:
    while True:
        print("==:", end="")
        user = input()
        if user == "q":
            break
        elif user == "i":
            print("WRITING TO FILE")
            with open(filename, 'w') as file:
                while True:
                    i = input(">")
                    if i.lower() == "x":
                        break
                    file.write(i + "\n")
