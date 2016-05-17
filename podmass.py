import requests
import feedparser
import re

page_links = []
itunes_links = []
re.M

r = feedparser.parse('http://www.avclub.com/feed/rss/?feature_types=podmass')

for x in xrange(0,len(r)):
	page_links.append(requests.get(r.entries[x].link)) #parses feed of each link in the avclub feed
	
	for y in xrange(1,len(page_links)): 
		
		itunes_links.append(re.search('(?<=href=").*itunes.*(?=")', page_links[y].text).string)
		
#regex output tends to be way too long, so I output it to the file below
f = open('regex_out.txt', 'w')
f.write(page_links[1].text.encode('utf8'))
f.close()

