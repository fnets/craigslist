import requests
import feedparser
import re
import sys

page_links = []
itunes_links = []
re.M

r = feedparser.parse('http://www.avclub.com/feed/rss/?feature_types=podmass')
<<<<<<< HEAD

<<<<<<< HEAD
page_links.append(requests.get(r.entries[0].link))
for y in xrange(0,len(page_links)): 
		
		itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[y].text)) #searches through currently accessed podmass pages' download links for itunes links.
		f.write(itunes_links[0][y].encode('utf8')+"\n") #writes added link to file
=======
>>>>>>> parent of 35aff13... Workable output

for x in xrange(1,len(r)):
	urls = requests.get(r.entries[x].link) #scrapes HTML of each page that is linked in RSS feed
	parsed_urls = feedparser.parse(urls.url)
	
<<<<<<< HEAD
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

=======
for x in xrange(0,len(r)):
	page_links.append(requests.get(r.entries[x].link)) #parses feed of each link in the avclub feed
	
	for y in xrange(1,len(page_links)): 
		
=======
	for y in xrange(1,len(page_links)): 
		
>>>>>>> parent of 35aff13... Workable output
		itunes_links.append(re.search('(?<=href=").*itunes.*(?=")', page_links[y].text).string)
		
#regex output tends to be way too long, so I output it to the file below
f = open('regex_out.txt', 'w')
f.write(page_links[1].text.encode('utf8'))
f.close()
<<<<<<< HEAD
>>>>>>> parent of 35aff13... Workable output
=======
>>>>>>> parent of 35aff13... Workable output

