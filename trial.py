import re
import sys

page_links = []
itunes_links = []

f = open("regex_out.txt","w")
g = open("test.txt","r")

for x in xrange(0,len(page_links)):
	itunes_links.append(re.findall('(?<=href=").*itunes.*(?=")', g.read()))
	
for x in xrange(0,len(itunes_links)): 
	for y in xrange(0,len(itunes_links[x])):
		
		f.write(itunes_links[x][y].encode('utf8')+"\n") 

f.close()
g.seek(0)
#g.close()