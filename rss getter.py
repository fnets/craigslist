 #all of this works, so implement it in a loop that reads your iTunes links.  Then output to CSV, then output to SQL DB
 
 driver.get('http://www.picklemonkey.net/feedflipper-home')
 text_here = driver.find_element_by_id('feed')
 text_here.send_keys('http://itunes.apple.com/us/podcast/comedy-bang-bang-the-podcast/id316045799?mt=2')
 result = driver.find_element_by_id("extracted_podcast")
  print result.text
http://rss.earwolf.com/comedy-bang-bang
 driver.get(result.text)
