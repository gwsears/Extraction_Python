# This is a program to scrape Websummit.net's 2016 attendee list.
# To set the pages that the program scrapes change firstPage and lastPage variables.
# Target Site URL: https://websummit.net/attendees/featured-attendees
# JSON URL: https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&page=1

import csv
import requests
import time

# Our target url.  This URL returns the JSON information for a number of attendees.
baseURL = "https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=50&page="
firstPage = 1
lastPage = 672
pageNum = firstPage
targetURL = baseURL + str(pageNum)

# Open/create csvfile and prep for writing
csvFile = open("attendees_scrape.csv", 'w+', encoding='utf-8', newline='')
outputWriter = csv.writer(csvFile, dialect='excel')
outputWriter.writerow(['Name','Title','Company','Country','About','ID','Image'])

content = True
while content == True: #As long as we are getting content continue to loop.
    r = requests.get(targetURL, auth=('user', 'pass'))
    page = r.json()
    listAttend = page['attendees']
    n = 0
    while n < 50:
        name = listAttend[n]['name']
        title = listAttend[n]['career']
        company = listAttend[n]['company']
        country = listAttend[n]['country']
        about = listAttend[n]['bio']
        idNumber = listAttend[n]['id']
        image = listAttend[n]['medium_image']
        outputWriter.writerow([name, title, company, country, about, idNumber, image])
        n = n + 1
    #Stop Loop Temporary
    if pageNum == lastPage:
         content = False
    # Status Indicator
    print('Page ' + str(pageNum) + ' complete.')
    #While Loop Increment
    pageNum = pageNum + 1
    time.sleep(15)
