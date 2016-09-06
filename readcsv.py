import csv
with open('Websites.csv', 'r') as f:
     reader = csv.reader(f)
     for row in reader:
            print(row)
