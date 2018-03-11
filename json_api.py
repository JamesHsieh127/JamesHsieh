import urllib
import json
import urllib.request, urllib.parse, urllib.error

serviceurl = "http://python-data.dr-chuck.net/geojson?"
while True:
    address = input("Enter location: ")
    if len(address) < 1: break

    url = serviceurl + urllib.parse.urlencode({'address': address})
    print('Retrieving', url)

    data = urllib.request.urlopen(url).read()
    print('Retrieved', len(data), 'characters')


    try:
        js = json.loads(data)
    except:
        js = None

    if 'status' not in js or js['status'] != 'OK':
        print ('==== Failure To Retrieve ====')
        print (data)
        continue

    # print json.dumps(js, indent=4)
    id = js['results'][0]['place_id']
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
    print ("Place id", id)
