import csv
import datetime
today = datetime.date.today()
print(today)
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
#funct to return dict
def product_identifier(product_id):
        return products[product_id]
#read from a txt file
product_list = []
with open('product_sales.txt', 'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        #attributes is a list we will append
        attributes = product_identifier(row[0])
        row.append(attributes[0])
        row.append(attributes[1])
        product_list.append(row)
        print(row)
for i, product in enumerate(product_list, start=1):
    product.insert(0,today)
    product.insert(1, i)
header = ['current_date', 'sale_id', 'product_id', 'name', 'price']
with open('sales_tracker.csv', 'w', newline = '') as csv_file:
    writer = csv.writer(csv_file)
    #adding the header
    writer.writerow(header)
    writer.writerows(product_list)


