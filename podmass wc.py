import requests
import feedparser
import re
import sys

page_links = []
itunes_links = []
re.M

r = feedparser.parse('http://www.avclub.com/feed/rss/?feature_types=podmass')

page_links.append(requests.get(r.entries[0].link))
for y in xrange(0,len(page_links)): 
		
		itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[y].text)) #searches through currently accessed podmass pages' download links for itunes links.
		f.write(itunes_links[0][y].encode('utf8')+"\n") #writes added link to file

for x in xrange(1,len(r)):
	urls = requests.get(r.entries[x].link) #scrapes HTML of each page that is linked in RSS feed
	parsed_urls = feedparser.parse(urls.url)
	
	#links = parsed_urls.entries[0].link
	#print links
print parsed_urls.entries[0].link

for itunes in links:
	print type(links) #.entries.link
	#page_links.append(links.entries[0].link)
	#if page_links[x][y] == page_links[x][y-1]:
		#print x,y	
	
	#for y in xrange(1,len(page_links)): 
		
		#itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[y].text)) #searches through currently accessed podmass pages' download links for itunes links.
		#f.write(itunes_links[x][y].encode('utf8')+"\n") #writes added link to file
		
		#if itunes_links[x][y] == itunes_links[x][y-1]:
		#	print x,y

print page_links

f.close() #closes file
