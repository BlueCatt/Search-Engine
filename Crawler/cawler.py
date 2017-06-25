import urllib2
from bs4 import BeautifulSoup
import re
import json

class RedirectHandler(urllib2.HTTPRedirectHandler):
    def http_error_301(self, req, fp, code, msg, headers):
        pass
    def http_error_302(self, req, fp, code, msg, headers):
        pass

class Crawler(object):
	"""docstring for ClassName"""
	def __init__(self):
		global pages
		pages = set()

	def craw(self,url,urlName):
		# url = 'https://www.nytimes.com/?mcubz=0'
		global pages
		data = {}
		try:
			opener = urllib2.build_opener(RedirectHandler)
			response = opener.open(url)
		except urllib2.HTTPError, e:
		    print e.code
		    return [],[]
		pages.add(url)
		print(url)
		print('craw ',len(pages),' links')
		html = response.read()
		soup = BeautifulSoup(html,'html.parser')
		soup.originalEncoding
		soup.prettify
		url_list = soup.findAll(name='a',href=re.compile('^https://www.nytimes.com'))
		links = []
		linklist = []
		for link in url_list:
			newlink = {}
			# print(link)
			if 'href' in link.attrs:
				if link.attrs['href'] not in pages:
					newPage = link.attrs['href']
					newlink['name'] = link.string
					newlink['url'] = newPage
					linklist.append(newPage)
					links.append(newlink)
		data['urlName'] = urlName
		data['url'] = url
		data["title"] = soup.title.string
		data['links'] = linklist
		# print(links)
		return data,links


	def BFS(self,node,nodeName,depth):
		if depth == 5:
			return
		else:
			data,links = self.craw(node,nodeName)
			if len(data) > 0:
				self.SaveAsJson("data",data)
			if len(links) > 0:
				for i in links:
					# print(i)
					self.BFS(i['url'],i['name'],depth + 1)

	def SaveAsJson(self,fileName,data):
			with open(fileName,"a") as json_file:
				json_file.write(json.dumps(data)+"\n")

	def LoadJson(self,fileName):
		with open(fileName) as json_file:
			data = json.load(json_file)
			return data

# json
# {
# 	urlNamestring
# 	url:string
# 	title:sring
# 	links:[string]
# }

