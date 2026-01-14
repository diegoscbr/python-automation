import csv
def rating_category(rating):
    rating = int(rating)

    if rating <= -3:
        category = "abysmal"

    elif rating <= -1:
        category = 'awful'

    else: category = 'bad'

    return category

modified_dad_jokes = []

with open ("dad_jokes.csv", 'r') as file:
    reader = csv.reader(file)

    headers = next(reader)
    headers.append('rating category')
    modified_dad_jokes.append(headers)

    for row in reader:
        row.append(rating_category(row[2]))
        modified_dad_jokes.append(row)

with open("modified_dad_jokes.csv", 'w', newline= '') as file:
    writer = csv.writer(file)
    writer.writerows(modified_dad_jokes)

print(modified_dad_jokes)