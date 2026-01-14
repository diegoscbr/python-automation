import csv

with open("dad_jokes.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(f"ID: {row[0]}, Joke: {row[1]}, Rating: {row[2]}")
