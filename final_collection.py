import csv
from pymongo import MongoClient

client=MongoClient()
db=client.testdb
with open('Websites_category.csv','r') as f:
		reader=csv.reader(f)
		i=1
		for row in reader:
			result=db.Final_data.insert_one(
				{
					"name":row[0],
					"category":row[1],
					"rank":i
				})
			i=i+1
			