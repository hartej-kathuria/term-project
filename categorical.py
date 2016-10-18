from __future__ import division
import csv
from pymongo import MongoClient
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.plotly as py

def creating_database(csvfile):
	client=MongoClient()
	db=client.testdb
	with open(csvfile,'r') as f:
			reader=csv.reader(f)
			i=1
			for row in reader:
				db.Only_category.insert_one(
					{
						"name":row[0],
						"category":row[1],
						"rank":i
					})
				i=i+1

def catlabels():
	with open('Websites_category_new.csv','r') as f:
		read=csv.reader(f)
		lt=[]
		lt2=[]
		for row in read:
			lt.append(row[1])
		lt2=sorted(set(lt))
		return lt2

def collectdata():
#counting websites in each category
	labels=catlabels()
	client2=MongoClient()
	db2=client2.testdb
	number=[]
	for i in labels:
		number.append(db2.Only_category.find({"category":i}).count())

	total=0
	for i in range(0,len(number)):
		total=total+number[i]
	assert(total==200)
	#print(total)
	df=pd.DataFrame(number,columns=['Website count'],index=labels)
	print(df)
	number_percn=[]
	for i in range(0,20):
		number_percn.append((number[i]/total)*100)
	df2=pd.DataFrame(number_percn,columns=['Ratio out of total 200'],index=labels)
	#print(df2)
	return number_percn,number,labels

def displaydata():#displaying the obatined data in barchart
	number_percn,number,labels=collectdata()
	labels_num=range(1,17)
	width=1
	#plt.pie(number_percn)
	#plt.show()

	plt.barh(labels_num,number,align='center')
	plt.yticks(labels_num,labels)
	plt.xlabel('Website count')
	plt.ylabel('Category')
	for i, v in enumerate(number):
	    plt.text(v + 1, i + .75, str(v), color='black', fontweight='bold')
	plt.show()
	#plt.savefig('Website_category_barchart.png')


if __name__=='__main__':
	#creating_database('Websites_category_new.csv')
	#displaydata()
	display=collectdata()
	#print(display)