import itunes_feed_extractor
import feedparser
feedparser._FeedParserMixin.can_contain_dangerous_markup.remove('description')
feedparser._HTMLSanitizer.acceptable_elements.remove('p')
feedparser._HTMLSanitizer.acceptable_attributes.remove('href') 
feedparser._FeedParserMixin.can_contain_relative_uris.remove('description')
import datetime
import sqlite3
import unicode_csv as ucsv
from bs4 import BeautifulSoup
from lxml.html.clean import Cleaner
import re

def main():
	rss = []
	update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	#cleaner = Cleaner(remove_unknown_tags=True, allow_tags=None);

	### Database Information ###
	csv_file = "search_result.csv"
	db_file = "search_result.db"
    
    # Database connection
	db = sqlite3.connect(db_file)
	db_cursor = db.cursor()
	
	with open('regex_out_top.txt') as f:
		iTunesLinks = f.readlines()# reads through output of TopPodasts.py
	g = open("rsstestout.txt","w") #opens output file, because there are too many links to be readable on command line

	for link in iTunesLinks: #go through output of TopPodasts.py and use them in the itunes_feed_extractor.py
		g.write(str(itunes_feed_extractor.ConvertItunesLink(link)) + "\n") #writes rss URLs to a file
		rss.append(itunes_feed_extractor.ConvertItunesLink(link)) #collects rss feeds into array

	for link in rss: #go through rss array, link by link
		soup = BeautifulSoup(str(link), 'html.parser')
		r = feedparser.parse(str(link)) #parse each link
		url = r['feed']["link"]
		for items in r.entries: #Go through episodes of each podcast
			#print items["title"] #prints each episode title
			title = items["title"]
			text1 = items["summary"]
			text = re.sub(ur'<.*?>',"", text1,re.U)
			#text = text.split("<")[0].strip()
			
			#text = soup.get_text(text)
			#text = text.encode('ascii','ignore')

			enter_data(db_cursor, url, title, text, update_time)
			#Should I just create CSV here?  

    # Uncomment this line to clean existing entries from the database
    # clean_expired_entries(db_cursor, update_time)

    # Commit the change to sqlite database
	db.commit()
    
    # pdb.set_trace()
    # Convert the sqlite3 database to csv
	db_cursor.execute('SELECT * FROM listings')
	with open("search_result.csv", "wb") as f:
		csv_writer = ucsv.UnicodeWriter(f)
		csv_writer.writerow([i[0] for i in db_cursor.description]) # Write the header
		csv_writer.writerows(db_cursor)

    # Close the database
	db.close()
		
	g.close()
	f.close()

def enter_data(db_cursor, url, title, text, update_time):
	db_cursor.execute("SELECT last_update FROM listings WHERE title = ?", (title,))
	

	
	if db_cursor.fetchone() == None: # Meaning that this tile does not exist yet
		db_cursor.execute('''
            INSERT INTO listings
            (url, title, text, last_update, new, found)
            VALUES (?, ?, ?, ?, ?, ?)''',
        (url, title, text, update_time, 1, update_time) 
        )
		
	else: # If this title exists then update the update_time
		db_cursor.execute( '''
			UPDATE listings
			SET last_update = ?
			WHERE title = ?''',
			(update_time, title)
		)

def clean_expired_entries(db_cursor, update_time):
	#print "clean_expired"
	
	db_cursor.execute("""
    DELETE FROM listings
    WHERE last_update != ?
    """,
    (update_time,)
    )
	
if __name__ == '__main__':
    main()