# This is a program to scrape Websummit.net's 2016 attendee list.
# To set the pages that the program scrapes change firstPage and lastPage variables.
# Target Site URL: https://websummit.net/attendees/featured-attendees
# JSON URL: https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=25&page=1

import csv
import requests # resquests is not a standard library in Python3.  You can get it through pip3
import time

# Our target url.  This URL returns the JSON information for a number of attendees.
baseURL = "https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=50&page="
firstPage = 100
lastPage = 105
pageNum = firstPage
delay = 5 # How many seconds to delay between each pull so the site isn't flooded with requests.
outputTitle = "attendees_scrape2.csv"

# Open/create csvfile and prep for writing
csvFile = open(outputTitle, 'w+', encoding='utf-8', newline='')
outputWriter = csv.writer(csvFile, dialect='excel')
outputWriter.writerow(['Name','Title','Company','Country','About','ID','Image'])

content = True

# Pulls the first page.
targetURL = baseURL + str(pageNum)
r = requests.get(targetURL, auth=('user', 'pass'))
page = r.json()

# Sets up a list of IDs to check for duplicates.
idList = []
n = 0

while content == True: #As long as we are getting content continue to loop.
    listAttend = page['attendees']
    idNumber = listAttend[n]['id']
    if idNumber in idList: # Check for duplicate IDs
        print("Duplicate!")
    else: # IF NOT a duplicate add to the file.
        idList.append(idNumber)
        name = listAttend[n]['name']
        title = listAttend[n]['career']
        company = listAttend[n]['company']
        country = listAttend[n]['country']
        about = listAttend[n]['bio']
        image = listAttend[n]['medium_image']
        outputWriter.writerow([name, title, company, country, about, idNumber, image])
    # Status Indicator
    print('Page ' + str(pageNum) + ' complete.')
    # Reset variables, not sure if this is nessasary, but better safe than sorry.
    idNumber = ''
    name = ''
    title = ''
    company = ''
    country = ''
    about = ''
    image = ''
    #While Loop Increment
    pageNum = pageNum + 1
    targetURL = baseURL + str(pageNum)
    r = requests.get(targetURL, auth=('user', 'pass'))
    page = r.json()
    if page['attendees'] == []: # Stop if there is no data in the next page.
        print("No more data.")
        content = False
    elif pageNum == lastPage: # Stop if the last page is reached.
        print("Last page reached.")
        content = False
    else:
        time.sleep(delay)
