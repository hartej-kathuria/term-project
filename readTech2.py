from __future__ import division
import glob, os
import csv
from pymongo import MongoClient
import json
from json import JSONEncoder



# FILE_PATH = "/home/manick/term1Project/w3tech"

# os.chdir(FILE_PATH)
class readW3techPage:

	def __init__(self):
		self._javaLibraries = ["JQuery","Bootstrap","Modernizr","MooTools","ASP.NET Ajax","Prototype","Script.aculo.us","YUI Library","Shadowbox","Underscore","AngularJS","Spry","Backbone","GSAP","Dojo","Knockout","Ext JS"]
		self._serverLang = ["PHP","ASP.NET","Java","ColdFusion","Ruby","Perl","Python"]
		self._clientLang = ["JavaScript","Flash","Silverlight"]
		self._markupLang = ["HTML", "XHTML"]
		self._charEncode = ["UTF-8","ISO-8859-1","Windows-1251","Shift JIS","Windows-1252","GB2312","EUC-KR","EUC-JP","GBK","ISO-8859-2","Windows-1250","ISO-8859-15","Windows-1256","ISO-8859-9","Big5","Windows-1254","Windows-874"]
		self._imageFormats = ["PNG","JPEG","GIF","SVG","BMP","ICO"]
		self._siteElements = ["CSS","Compression","Cookies","ETag","HTTP/2","SPDY","IPv6","HTTP Strict Transport Security","Frameset"]
		self._webServers = ["Apache", "Nginx","Microsoft-IIS","LiteSpeed","Google Servers","Tomcat","IdeaWebServer","Apache Traffic Server","Node.js","Tengine","Cowboy","Lighttpd","Oracle Servers","IBM Servers"]
		self._os = ["Unix", "Windows"]
		self._countries = ["United States","Germany","Japan","Russian Federation","France","United Kingdom","Netherlands","China","Canada","Italy","Spain","Poland","Turkey","Republic of Korea (South Korea)","Brazil","Australia","India","Singapore","Czech Republic","Ireland","Ukraine","Iran","Switzerland","Viet Nam","Sweden","Denmark","Romania","South Africa","Thailand","Taiwan","Indonesia","Hungary","Austria","Bulgaria","Argentina","Finland","Estonia","Portugal","Belgium","Malaysia","Slovakia","Norway","Lithuania","Belarus","Israel","Greece","Kazakhstan","Chile","New Zealand","Latvia","Slovenia","Mexico","Croatia","Luxembourg","Cyprus","Costa Rica","Serbia"]
		self._languages = ["Hindi","Kannada","English","Russian","Japanese","German","Spanish","French","Portuguese","Italian","Chinese","Polish","Turkish","Persian","Dutch","Korean","Czech","Arabic","Vietnamese","Indonesian","Swedish","Greek","Romanian","Hungarian","Danish","Thai","Slovak","Finnish","Bulgarian","Hebrew","Norwegian","Lithuanian","Croatian","Ukrainian","Norwegian","Serbian","Valencian","Slovenian","Estonian","Latvian"]
		self._obtainedJavaLibraries = []
		self._obtainedServerLang = []
		self._obtainedClientLang = []
		self._obtainedmarkUpLang = []
		self._obtainedCharEncode = []
		self._obtainedImageFormat = []
		self._obtainedSiteElements = []
		self._obtainedWebServers = []
		self._obtainedOS = []
		self._obtainedcountries = []
		self._obtainedlanguages = []

	def checkLibraries(self,file):
		i = 0
		for i in range(len(self._javaLibraries)):
			if self._javaLibraries[i] in file:
				self._obtainedJavaLibraries.append(self._javaLibraries[i])

	def checkServerLang(self,file):
		i = 0
		for i in range(len(self._serverLang)):
			if self._serverLang[i] in file:
				self._obtainedServerLang.append(self._serverLang[i])

	def checkClientLang(self,file):
		i = 0
		for i in range(len(self._clientLang)):
			if self._clientLang[i] in file:
				self._obtainedClientLang.append(self._clientLang[i])

	def checkMarkupLang(self,file):
		i = 0
		for i in range(len(self._markupLang)):
			if self._markupLang[i] in file:
				self._obtainedmarkUpLang.append(self._markupLang[i])

	def checkCharEncode(self,file):
		i = 0
		for i in range(len(self._charEncode)):
			if self._charEncode[i] in file:
				self._obtainedCharEncode.append(self._charEncode[i])

	def checkImageFormat(self,file):
		i = 0
		for i in range(len(self._imageFormats)):
			if self._imageFormats[i] in file:
				self._obtainedImageFormat.append(self._imageFormats[i])

	def checkSiteElememt(self,file):
		i = 0
		for i in range(len(self._siteElements)):
			if self._siteElements[i] in file:
				self._obtainedSiteElements.append(self._siteElements[i])

	def checkWebServer(self,file):
		i = 0
		for i in range(len(self._webServers)):
			if self._webServers[i] in file:
				self._obtainedWebServers.append(self._webServers[i])


	def checkOS(self,file):
		i = 0
		for i in range(len(self._os)):
			if self._os[i] in file:
				self._obtainedOS.append(self._os[i])


	def checkCountries(self,file):
		i = 0
		for i in range(len(self._countries)):
			if self._countries[i] in file:
				self._obtainedcountries.append(self._countries[i])

	def checkLanguages(self,file):
		i = 0
		for i in range(len(self._languages)):
			if self._languages[i] in file:
				self._obtainedlanguages.append(self._languages[i])

	
	def buildJSONandInsertInDB(self,websitename):
		# jsonString = JSONEncoder().encode({
		# 	"Websitename" : websitename,
		# 	"ServerSideLang": self._obtainedServerLang,
		# 	"ClientSideLang": self._obtainedClientLang,
		# 	"MarkUPLang" : self._obtainedmarkUpLang,
		# 	"CharEncodingUsed" : self._obtainedCharEncode,
		# 	"ImageFormat" : self._obtainedImageFormat,
		# 	"Site ELements" : self._obtainedSiteElements,
		# 	"Web Servers" : self._obtainedWebServers,
		# 	"Operating System" : self._obtainedOS,
		# 	"Countries" : self._obtainedcountries,
		# 	"Languages" : self._obtainedlanguages
		# })  
		""" Creat a client and create a new DB """       
		client=MongoClient()
		db=client.testdb2
		result=db.Final_data.update_one(
					{
						"name":websitename	
					},
					{
					"$set":
					{
						"JavaLibraries":self._obtainedJavaLibraries,
						"ServerSideLang": self._obtainedServerLang,
						"ClientSideLang": self._obtainedClientLang,
						"MarkUPLang" : self._obtainedmarkUpLang,
						"CharEncodingUsed" : self._obtainedCharEncode,
						"ImageFormat" : self._obtainedImageFormat,
						"Site ELements" : self._obtainedSiteElements,
						"Web Servers" : self._obtainedWebServers,
						"Operating System" : self._obtainedOS,
						"Countries" : self._obtainedcountries,
						"Languages" : self._obtainedlanguages
					}})            

		#print json.dumps(jsonString,indent=4)

if __name__ == '__main__':

	FILE_PATH = "/home/hartej/term-project/w3techs"
	os.chdir(FILE_PATH)

	for fileName in glob.glob("*"):
		file = open(fileName).read()
		rlistofLib = readW3techPage()
		rlistofLib.checkLanguages(file)
		rlistofLib.checkCountries(file)
		rlistofLib.checkOS(file)
		rlistofLib.checkLibraries(file)
		rlistofLib.checkWebServer(file)
		rlistofLib.checkSiteElememt(file)
		rlistofLib.checkImageFormat(file)
		rlistofLib.checkCharEncode(file)
		rlistofLib.checkClientLang(file)
		rlistofLib.checkServerLang(file)
		rlistofLib.checkMarkupLang(file)

		"""get filename (Actually get the website name)"""
		base=os.path.basename(fileName)
		websitename = os.path.splitext(base)[0]
		rlistofLib.buildJSONandInsertInDB(websitename)
		

		#print '##################################################################################################################'

