from pymongo import MongoClient
import pandas as pd

def stats(stat_technology,index_technology):
	fieldname=["ServerSideLang","ClientSideLang","MarkUPLang","CharEncodingUsed","ImageFormat","SiteElements","WebServers","Operating System","Countries","Languages"]
	client=MongoClient()
	db=client.testdb
	a=[[0 for x in range(len(stat_technology))]for x in range(16)]
	v=0
	for j in labels:
		y=0
		for i in stat_technology:
			a[v][y]=db.Final_data.find({"category":j,fieldname[index_technology]:i}).count()
			y=y+1
		v=v+1

	df=pd.DataFrame(a,columns=stat_technology,index=labels)
	print(df)

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
	labels=["Search Engine","News","Art","Social","E-Commerce","Banking","Computer","Government","Service Provider","Buissness","Adult","Job Search Engine","Ads","Education","Cloud Computing","Travel"]
	stats(Languages_index9,9)
	