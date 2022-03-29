import io
import os
import gzip
import json
import csv


class Exo2:
    def __init__(self, pathname):
        self.pathname = pathname

    def parse_json(self):
        pathname = self.pathname
        with gzip.open(pathname, 'rb') as f:
            data = f.read()
            j = json.loads(data.decode('utf-8'))
            return j

    def get_products(self, content):
        available_prod = []
        for product in content['Bundles']:
            # check if we have product or products key
            if 'Product' in product.keys():
                key = 'Product'
            elif 'Products' in product.keys():
                key = 'Products'
            else:
                continue
            # check if products dict not empty
            if product[key]:
                # get keys to use it like columns of the csv file
                useful_columns = list(product[key][0].keys())
                if 'Name' in product[key][0].keys():
                    product_name = product[key][0]['Name'][:30]
                    product[key][0]['Name'] = product_name
                # check if Product is available
                if 'IsAvailable' in product[key][0].keys():
                    id = str(product[key][0]['Stockcode'])
                    if(product[key][0]['IsAvailable'] == True):
                        price = format(product[key][0]['Price'], '.1f')
                        # add product to table of available product to use it in the csv files
                        available_prod.append(product[key][0])
                        print("You can buy "+product_name +
                              " at our store at "+str(price))
                    else:
                        print("Product not available ! -->  id : " +
                              id+" , productName: "+product_name)
                else:
                    print(
                        "Error : the clue of the product’s availability can’t be found")
            else:
                continue

        return available_prod, useful_columns

    def generate_csv_file(self, data, useful_columns):
        default_value = ""
        with open('results.csv', mode='w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=useful_columns)
            writer.writeheader()
            for obj in data:
                row = {}
                for column in useful_columns:
                    if column in obj.keys():
                        row[column] = obj[column]
                    else:
                        row[column] = default_value
                writer.writerow(row)
