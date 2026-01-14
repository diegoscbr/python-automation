l1 = ['Max', 'Dog', 'bacon strips', 4754]
l2 = ['Julius', 'Catnip', 'catnip', 3215]
l3 = ['Cal', 'Cat', 'anything edible', 7142]
l4 = ['Lina', 'Cat', 'Sheba', 142]
l5 = ['Bruiser', 'Featherfin Catfish', 'fish pellets', 54]

import csv
with open('expensive_pets.csv', 'w', newline='') as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow(['name', 'species', 'favorite_snack', 'monthly_cost'])
    csv_writer.writerow(['Max', 'Dog', 'bacon strips', 4754])

    csv_writer.writerows([l1, l2, l3, l4])