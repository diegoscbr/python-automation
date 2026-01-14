import csv

products = {'P001' : ['Wireless Headphones', 100],
            'P002' : ['Laptop Backpack', 60],
            'P003' : ['Bluetooth Speaker', 50],
            'P004' : ['USB Flash Drive', 20],
            'P005' : ['Mobile Phone Case', 15],
            'P006' : ['Wireless Mouse', 30],
            'P007' : ['Laptop Stand', 40],
            'P008' : ['HDMI Cable', 15],
            'P009' : ['Smartphone', 600],
            'P010' : ['External Hard Drive', 100]
        }
#step one
def product_identifier(product_id):
        return products[product_id]
#read from a txt file

with open('product_sales.txt', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        #attributes is a list we will append
        attributes = product_identifier(row[0])
        row.append(attributes[0])
        row.append(attributes[1])
        print(row)

header = ['product_id', 'name', 'price']
with open('sales_tracker.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
