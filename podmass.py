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
	itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[x].text)) #For some reason, this is picking up the URL in href and in data-track-label.  Tried eliminating duplicates by requiring itunes-link to precede.  Works in Notepad++ but not in execution.
	#searches through currently accessed podmass pages' download links for itunes links.

seen = set()
uniq = []
dupe = []

for x in xrange(len(itunes_links)):  #code found on stackoverflow to check to separate uniques and duplicates
    for y in xrange(len(itunes_links[x])):
		if itunes_links[x][y] not in seen:
			uniq.append(itunes_links[x][y])
			seen.add(itunes_links[x][y])
		else:
			dupe.append(itunes_links[x][y])

for x in xrange(len(uniq)): #Loops through uniq array and write all to a file
	f.write(str(uniq[x]) + "\n")
			

f.close() #closes file

