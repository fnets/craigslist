import requests
import feedparser
import re

page_links = []
itunes_links = []

f = open('regex_out.txt', 'w') #opens output file, because there are too many links to be readable on command line

r = feedparser.parse('http://www.avclub.com/feed/rss/?feature_types=podmass') #loads podmass page

for x in xrange(0,len(r)):
	page_links.append(requests.get(r.entries[x].link)) #parses feed of each link in the avclub feed
	
	for y in xrange(0,len(page_links)): 
		
		itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[y].text)) #searches through currently accessed podmass pages' download links for itunes links.
		f.write(itunes_links[x][y].encode('utf8')+"\n") #writes added link to file

f.close() #closes file


