import requests
import feedparser
#import re
import sys

page_links = []
itunes_links = []

f = open("regex_out_top.txt","w") #opens output file, because there are too many links to be readable on command line
r = feedparser.parse('https://itunes.apple.com/us/rss/toppodcasts/limit=10/xml') #parses Apple RSS page

for x in xrange(0,len(r.entries)):
	itunes_links.append(r.entries[x].link)
	'''itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', page_links[x].text)) #For some reason, this is picking up the URL in href and in data-track-label.  Tried eliminating duplicates by requiring itunes-link to precede.  Works in Notepad++ but not in execution.
	#searches through feed for itunes links.'''

print itunes_links

seen = set()
uniq = []
dupe = []

for x in xrange(len(itunes_links)):  #code found on stackoverflow to check to separate uniques and duplicates
	if itunes_links[x] not in seen:
		uniq.append(itunes_links[x])
		seen.add(itunes_links[x])
	else:
		dupe.append(itunes_links[x])
		
for x in xrange(len(uniq)): #Loops through uniq array and write all to a file
	f.write(str(uniq[x]) + "\n")
			

f.close() #closes file

