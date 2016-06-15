import sqlite3

def enter_data(db_cursor, url, sublocation, title, text):
    db_cursor.execute("SELECT last_update FROM listings WHERE title = ?", (title,))
	db_cursor.execute('''
		INSERT INTO listings
		(url, sublocation, title, text, last_update, new, found)
		VALUES (?, ?, ?, ?, ?, ?, ?)''',
		(url, sublocation, title, text, 1) 
		)

def retrieve_and_enter_data(db_cursor, rss_links):
          
	enter_data(db_cursor, rss_links)
	
def main():
     
	g = open("rss.txt","r")
	
    ### Search Parameters ###
    locations = ["washingtondc"]
    sublocations = ["doc", "nva", "mld"]
    search_terms = []
    listings = ["cta"] # cta is the listing for cars and trucks
    price = [3000, 7500] # min and max price
    year = [2004, 2010] # min and max year
    makes = ["honda", "toyota", "hyundai"]
    title_status = 1 # Clean title
    has_pic = 1 # has pic

    ### Database Information ###
    csv_file = "search_result.csv"
    db_file = "search_result.db"
    
    # Database connection
    db = sqlite3.connect(db_file)
    db_cursor = db.cursor()

    # Retrieve and parse rss
    retrieve_and_enter_data(db_cursor, g.readlines())

    # Commit the change to sqlite database
    db.commit()
    
    # Convert the sqlite3 database to csv
    db_cursor.execute('SELECT * FROM listings')
    with open("search_result.csv", "wb") as f:
        csv_writer = ucsv.UnicodeWriter(f)
        csv_writer.writerow([i[0] for i in db_cursor.description]) # Write the header
        csv_writer.writerows(db_cursor)

    # Close the database
    db.close()

if __name__ == '__main__':
    main()