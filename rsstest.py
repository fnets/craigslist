import itunes_feed_extractor
import feedparser
import datetime
import sqlite3
import unicode_csv as ucsv
from lxml.html.clean import Cleaner


def main():

	rss = []
	update_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	cleaner = Cleaner(remove_unknown_tags=False, allow_tags=['img', 'p', 'a', 'b', 'em', 'div']);
	
	### Database Information ###
	csv_file = "search_result.csv"
	db_file = "search_result.db"
    
    # Database connection
	db = sqlite3.connect(db_file)
	db_cursor = db.cursor()
	
	with open('C:/Users/Frank/Documents/GitHub/craigslist/regex_out_top.txt') as f:
		iTunesLinks = f.readlines()# reads through output of TopPodasts.py
	g = open("rsstestout.txt","w") #opens output file, because there are too many links to be readable on command line

	for link in iTunesLinks: #go through output of TopPodasts.py and use them in the itunes_feed_extractor.py
		g.write(str(itunes_feed_extractor.ConvertItunesLink(link)) + "\n") #writes rss URLs to a file
		rss.append(itunes_feed_extractor.ConvertItunesLink(link)) #collects rss feeds into array
		
	for link in rss: #go through rss array, link by link
		r = feedparser.parse(str(link)) #parse each link
		url = r['feed']["link"]
		for items in r.entries: #Go through episodes of each podcast
			print items["title"] #prints each episode title
			title = items["title"]
			text = items["description"]
            
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
	print "clean_expired"
	
	db_cursor.execute("""
    DELETE FROM listings
    WHERE last_update != ?
    """,
    (update_time,)
    )
	
if __name__ == '__main__':
    main()