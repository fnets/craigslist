import requests
import feedparser

page_links = []
itunes_links = []

r = feedparser.parse('http://www.avclub.com/feed/rss/?feature_types=podmass')

for x in xrange(0,len(r)):
	#page_links.append(requests.get(r.entries[x].link)) #parses feed of each link in the avclub feed
	for y in xrange(0,len(r.entries[x].links)):
		page_links.append(r.entries[x].links[y].href) 
'''* for y in xrange(0,len(page_links)):
		#itunes_links = itunes_links.append(page_links.entries[y].link) 
		

'''
print page_links

