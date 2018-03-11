import json
import urllib
import urllib.request, urllib.parse, urllib.error

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'

while True:
    json_address = input('Enter location: ')
    if len(json_address) < 1: break

    print('Retrieving', json_address)

    data = urllib.request.urlopen(json_address).read().decode('utf-8')
    print('Retrieved', len(data), 'characters')

    json_info = json.loads(data)
    #print('User count:', len(info))

    #for item in info:
    #    print('Name', item['name'])
    #    print('Id', item['id'])
    #    print('Attribute', item['x'])
    total =0
    counter =0
    for comment in json_info["comments"]:
        total +=int(comment["count"])
        counter +=1
    print("Count: ", counter)
    print("Sum: ", total)
