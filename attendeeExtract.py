import csv
from bs4 import BeautifulSoup

# Open/create csvfile and prep for writing
csvFile = open("attendees.csv", 'w+', encoding='utf-8', newline='')
outputWriter = csv.writer(csvFile, dialect='excel')

# Open HTML and Prep BeautifulSoup
html = open('WEB SUMMIT _ LISBON 2016 _ Web Summit Featured Attendees.html', 'r', encoding='utf-8')
bsObj = BeautifulSoup(html.read(), 'html.parser')
itemList = bsObj.find_all("li", {"class":"item"})

def filter_non_printable(str):
  return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])

outputWriter.writerow(['Name','Title','Company','Country'])

for item in itemList:
    # Here we examine each candidate item and pull out their information.
    name = item.find("h4").get_text() # The candidate's name is in the first h4 html tags.
    title = item.find("strong").get_text() # The first text formatted strong in an item is the candidate's title.
    company = filter_non_printable(item.find_all("span")[1].get_text()) # The second span
    country = filter_non_printable(item.find_all("span")[2].get_text())
    about = filter_non_printable(item.find_all("p")[1].get_text())
    imageNumber = filter_non_printable(str(item.find('div', {'class':'item-image'})))
    # This writes the data collected above as a new row on attendees.csv.
    outputWriter.writerow([name,title,company,country,about,imageNumber])
