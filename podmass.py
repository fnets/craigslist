import requests
import feedparser
import re
import sys

page_links = []
itunes_links = []

f = open("regex_out.txt","w") #opens output file, because there are too many links to be readable on command line
r = feedparser.parse('http://www.avclub.com/feed/rss/?feature_types=podmass') #parses podmass page

for x in xrange(0,len(r)):
	page_links.append(requests.get(r.entries[x].link)) #scrapes link x in the podmmass feed and adds to list

for x in xrange(0,len(page_links)):
	itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[x].text)) #For some reason, this is picking up the URL in href and in data-track-label
	#searches through currently accessed podmass pages' download links for itunes links.
	'''if (str(itunes_links[x-1]) == str(itunes_links[x])):
		print "Repeat at: " + str(x)'''  #Trying to find location of repeat, but strings aren't being matched to each other

seen = set()
uniq = []
dupe = []

for x in xrange(len(itunes_links)):  #code found on stackoverflow to check to separate uniques and duplicates
    for y in xrange(len(itunes_links[x])):
		if itunes_links[x][y] not in seen:
			uniq.append((x,y))
			seen.add(itunes_links[x][y])
		else:
			dupe.append(itunes_links[x][y])

print str(len(dupe)) + ", " + str(len(dupe[0]))

for x in xrange(0,len(itunes_links)): 
	for y in xrange(0,len(itunes_links[x])):
		
		#f.write(itunes_links[x][y].encode('utf8')+"\n") #writes all itunes link to file, but somehow affects the if statements below it
		if (x>=1) and (y>=1): #prevents out-of-bounds error with 0, works corectly
			#print "Index at: " + str(x)+", " + str(y)
			if (str(itunes_links[x][y-1]) == str(itunes_links[x][y])):
				b=0
				#print "Repeat at: " + str(x)+", " + str(y) #Trying to find location of repeat, but only comparing neighbors yeilds weird results

f.close() #closes file

###Below is a bunch of junk code that was in this file when I opened.  I copy/pasted a previous working version of this code into the document, and commented the old code out.
'''
for x in xrange(1,len(r)):
	urls = requests.get(r.entries[x].link) #scrapes HTML of each page that is linked in RSS feed
	parsed_urls = feedparser.parse(urls.url)
	#links = parsed_urls.entries[0].link
	print type(parsed_urls)
	if len(r.entries[x].link) != len(urls.url):
		print "Error at: " + str(x)

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

for y in xrange(0,len(page_links)): 
		
		itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[y].text)) #searches through currently accessed podmass pages' download links for itunes links.
		f.write(itunes_links[0][y].encode('utf8')+"\n") #writes added link to file		

print page_links

f.close() #closes file'''
