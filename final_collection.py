from __future__ import division
import csv
from pymongo import MongoClient
import pandas as pd
import numpy as np


client=MongoClient()
db=client.testdb
#with open('Websites_category.csv','r') as f:
		#reader=csv.reader(f)
		#i=1
		#for row in reader:
			#result=db.Final_data.insert_one(
				#{
					#"name":row[0],
					#"category":row[1],
					#"rank":i
				#})
			#i=i+1

#counting websites in each category
number=[]
number.append(db.Final_data.find({"category":"Search Engine"}).count())
number.append(db.Final_data.find({"category":"News"}).count())
number.append(db.Final_data.find({"category":"Art"}).count())
number.append(db.Final_data.find({"category":"Social"}).count())
number.append(db.Final_data.find({"category":"E-Commerce"}).count())
number.append(db.Final_data.find({"category":"Banking"}).count())
number.append(db.Final_data.find({"category":"Computer"}).count())
number.append(db.Final_data.find({"category":"Government"}).count())
number.append(db.Final_data.find({"category":"Service Provider"}).count())
number.append(db.Final_data.find({"category":"Buissness"}).count())
number.append(db.Final_data.find({"category":"Adult"}).count())
number.append(db.Final_data.find({"category":"Job Search Engine"}).count())
number.append(db.Final_data.find({"category":"Ads"}).count())
number.append(db.Final_data.find({"category":"Education"}).count())
number.append(db.Final_data.find({"category":"Cloud Computing"}).count())
number.append(db.Final_data.find({"category":"Travel"}).count())
print(number)
total=0
for i in range(0,len(number)):
	total=total+number[i]
assert(total==200)
print(len(number))
df=pd.DataFrame(number,columns=['Website count'],index=["Search Engine","News","Art","Social","E-Commerce","Banking","Computer","Government","Service Provider","Buissness","Adult","Job Search Engine","Ads","Education","Cloud Computing","Travel"])
print(df)
print(number[0]/200)
number_percn=[]
for i in range(0,16):
	number_percn.append(np.around(number[i]/total,5))

#print(number_percn)

df2=pd.DataFrame(number_percn,columns=['Ratio out of total 200'],index=["Search Engine","News","Art","Social","E-Commerce","Banking","Computer","Government","Service Provider","Buissness","Adult","Job Search Engine","Ads","Education","Cloud Computing","Travel"])
print(df2)