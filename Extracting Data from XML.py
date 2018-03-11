import urllib
import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

#serviceurl = 'http://maps.googleapis.com/maps/api/geocode/xml?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    #url = serviceurl + urllib.parse.urlencode({'address': address})
    url = urllib.parse.urlencode({'address': address})
    print('Retrieving', address)
    data = urllib.request.urlopen(address).read()
    print('Retrieved', (len(data)), 'characters')
    #print(data.decode())
    tree = ET.fromstring(data)
    counts = tree.findall('.//count')
    print("Count: ", len(counts))
    results = tree.findall('result')
    #lat = results[0].find('geometry').find('location').find('lat').text
    #lng = results[0].find('geometry').find('location').find('lng').text
    #location = results[0].find('formatted_address').text

    #print('lat', lat, 'lng', lng)
    #print(location)
    total =0
    for count in counts:
        total = total + int(count.text)
    print("Sum: ", total)
