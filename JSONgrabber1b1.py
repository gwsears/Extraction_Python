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
pageNum = firstPage

# Open/create csvfile and prep for writing
csvFile = open("attendees_scrape.csv", 'w+', encoding='utf-8', newline='')
outputWriter = csv.writer(csvFile, dialect='excel')
outputWriter.writerow(['Name','Title','Company','Country','About','ID','Image'])

content = True

targetURL = baseURL + str(pageNum)
r = requests.get(targetURL, auth=('user', 'pass'))
page = r.json()

while content == True: #As long as we are getting content continue to loop.
    listAttend = page['attendees']
    name = listAttend[n]['name']
    title = listAttend[n]['career']
    company = listAttend[n]['company']
    country = listAttend[n]['country']
    about = listAttend[n]['bio']
    idNumber = listAttend[n]['id']
    image = listAttend[n]['medium_image']
    outputWriter.writerow([name, title, company, country, about, idNumber, image])
    # Status Indicator
    print('Page ' + str(pageNum) + ' complete.')
    #While Loop Increment
    pageNum = pageNum + 1
    targetURL = baseURL + str(pageNum)
    r = requests.get(targetURL, auth=('user', 'pass'))
    page = r.json()
    if page['attendees'] == []:
        print("No more data.")
        content = False
    else:
        time.sleep(5)
