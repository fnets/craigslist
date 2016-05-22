 #all of this works, so implement it in a loop that reads your iTunes links.  Then output to CSV, then output to SQL DB
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()
rss = [] #store rss links
 
driver.get('http://www.picklemonkey.net/feedflipper-home') #load webtool

 
with open('C:/Users/Frank/Desktop/''craigslist regex bk''/regex_out.txt') as f:
	iTunesLinks = f.readlines()

for link in iTunesLinks: #go through regex output of podmass.py and add use them in the webtool
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "feed")))
	text_here = driver.find_element_by_id('feed') #find input field
	text_here.send_keys(link)
	element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "extracted_podcast")))
	result = driver.find_element_by_id("extracted_podcast") #read rss feed, timing may need to be added
	rss.append(result) #writes output of field to list.
	print result
	driver.refresh() #reloads page

f.close()
driver.close()
