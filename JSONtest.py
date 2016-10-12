import requests

URLtarg = 'https://api.cilabs.net/v1/conferences/ws16/info/attendees?limit=1&page=400000'
r = requests.get(URLtarg, auth=('user', 'pass'))
page = r.json()
print(type(page))
print(page)
print(page['attendees'])
if page['attendees'] == []:
    print('true')