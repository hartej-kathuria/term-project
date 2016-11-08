from pymongo import MongoClient
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import csv

def stats(stat_technology,index_technology):
	labels=catlabels()
	fieldname=["ServerSideLang","ClientSideLang","MarkUPLang","CharEncodingUsed","ImageFormat","SiteELements","WebServers","Operating System","Countries","Languages","JavaLibraries"]
	client=MongoClient()
	db=client.webdd
	a=[[0 for x in range(len(stat_technology))]for x in range(len(labels))]
	v=0
	b=db.Web_details.find({"SiteELements":"HTTP/2"}).count()
	for j in labels:
		y=0
		for i in stat_technology:
			a[v][y]=db.Web_details.find({"category":j,fieldname[index_technology]:i}).count()
			y=y+1
		v=v+1

	df=pd.DataFrame(a,columns=stat_technology,index=labels)
	df.to_csv('MarkUpLang.csv')
	#print(my_list)
	print(df)
	print("No of websites using HTTP/2= ",b)
	#visual3d(stat_technology,df)
	barstacked(stat_technology,a)

def countcategory():
	#counting websites in each category
	labels=catlabels()
	client2=MongoClient()
	db2=client2.webdd
	number=[]
	for i in labels:
		number.append(db2.Web_details.find({"category":i}).count())

	total=0
	for i in range(0,len(number)):
		total=total+number[i]
	#assert(total==200)
	print(total)
	df=pd.DataFrame(number,columns=['Count'],index=labels)
	print(df)
	number_percn=[]
	for i in range(0,20):
		number_percn.append((number[i]/total)*100)
	df2=pd.DataFrame(number_percn,columns=['Percentage'],index=labels)
	print(df2)
	return number_percn,number,labels

def catlabels():
	with open('Websites_category_new.csv','r') as f:
		read=csv.reader(f)
		lt=[]
		lt2=[]
		for row in read:
			lt.append(row[1])
		lt2=sorted(set(lt))
	return lt2

def barchart():
#displaying the obatined data in barchart
	number_percn,number,labels=countcategory()
	labels_num=range(1,21)
	width=1
	plt.barh(labels_num,number,align='center')
	plt.yticks(labels_num,labels)
	plt.xlabel('Website count')
	plt.ylabel('Category')
	for i, v in enumerate(number):
		plt.text(v + .5, i + .75, str(v), color='black', fontweight='bold')
	plt.show()
	#plt.savefig('Website_category_barchart.png')

def barstacked(tech,a):
	bars=[]
	labels=catlabels()
	labels_num=range(0,len(labels))
	tech_num=range(0,len(tech))
	tech_num_reverse=range(len(tech)-1,-1,-1)
	c=['r','b','g','y','c','m','k','w','r']
	for i in labels_num:
		for j in tech_num:
			bars.append(plt.bar(i,a[i][j],color=c[j],bottom=a[i][j-1],label=tech[j]))
	handles, labels = plt.gca().get_legend_handles_labels()
	handle_list, label_list = [], []
	for handle, label in zip(handles, labels):
	    if label not in label_list:
	        handle_list.append(handle)
	        label_list.append(label)
	plt.legend(handle_list, label_list)
	#plt.gca().add_artist(plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.))
	ticksx = np.arange(0.5, 20, 1)
	plt.xticks(ticksx,labels,rotation=90)
	plt.ylabel('Count')
	plt.xlabel('Categories')
	plt.show()

def visual3d(y,df):
	fig=plt.figure()
	ax=fig.add_subplot(111,projection='3d')
	i=0
	zpos=np.zeros(20)
	xpos=range(0,len(labels))
	c=['r','b','g','y','c','m','k','w','r']
	for e in y:
		ypos=np.zeros(20)+i
		dz=df[y[i]].tolist()
		dx=np.ones(20)/2
		dy=np.ones(20)/2
		ax.bar3d(xpos,ypos,zpos,dx,dy,dz,alpha=0.5,color=c[i])
		i=i+1

	ticksx = np.arange(0.2, 16, 1)
	plt.xticks(ticksx,labels,rotation=90)

	ticksy = np.arange(0.2, len(y), 1)
	plt.yticks(ticksy,y,rotation=90)
	plt.show()

if __name__=='__main__':
	ServerSideLang_index0 = ["PHP","ASP.NET","Java","ColdFusion","Ruby","Perl","Python"]
	ClientSideLang_index1 = ["JavaScript","Flash","Silverlight"]
	MarkUPLang_index2 = ["HTML", "XHTML"]
	CharEncodingUsed_index3 = ["UTF-8","ISO-8859-1","Windows-1251","Shift JIS","Windows-1252","GB2312","EUC-KR","EUC-JP","GBK","ISO-8859-2","Windows-1250","ISO-8859-15","Windows-1256","ISO-8859-9","Big5","Windows-1254","Windows-874"]
	ImageFormat_index4 = ["PNG","JPEG","GIF","SVG","BMP","ICO"]
	SiteElements_index5 = ["CSS","Compression","Cookies","ETag","HTTP/2","SPDY","IPv6","HTTP Strict Transport Security","Frameset"]
	WebServers_index6 = ["Apache", "Nginx","Microsoft-IIS","LiteSpeed","Google Servers","Tomcat","IdeaWebServer","Apache Traffic Server","Node.js","Tengine","Cowboy","Lighttpd","Oracle Servers","IBM Servers"]
	os_index7 = ["Unix", "Windows"]
	Countries_index8 = ["United States","Germany","Japan","Russian Federation","France","United Kingdom","Netherlands","China","Canada","Italy","Spain","Poland","Turkey","Republic of Korea (South Korea)","Brazil","Australia","India","Singapore","Czech Republic","Ireland","Ukraine","Iran","Switzerland","Viet Nam","Sweden","Denmark","Romania","South Africa","Thailand","Taiwan","Indonesia","Hungary","Austria","Bulgaria","Argentina","Finland","Estonia","Portugal","Belgium","Malaysia","Slovakia","Norway","Lithuania","Belarus","Israel","Greece","Kazakhstan","Chile","New Zealand","Latvia","Slovenia","Mexico","Croatia","Luxembourg","Cyprus","Costa Rica","Serbia"]
	Languages_index9 = ["Hindi","Kannada","English","Russian","Japanese","German","Spanish","French","Portuguese","Italian","Chinese","Polish","Turkish","Persian","Dutch","Korean","Czech","Arabic","Vietnamese","Indonesian","Swedish","Greek","Romanian","Hungarian","Danish","Thai","Slovak","Finnish","Bulgarian","Hebrew","Norwegian","Lithuanian","Croatian","Ukrainian","Norwegian","Serbian","Valencian","Slovenian","Estonian","Latvian"]
	JavaLibraries_index10 = ["JQuery","Bootstrap","Modernizr","MooTools","ASP.NET Ajax","Prototype","Script.aculo.us","YUI Library","Shadowbox","Underscore","AngularJS","Spry","Backbone","GSAP","Dojo","Knockout","Ext JS"]
	stats(ClientSideLang_index1,1)
	#barchart()
	