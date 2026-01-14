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

    for row in reader:
        print(rating_category(row[2]))