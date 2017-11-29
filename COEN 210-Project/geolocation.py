import geocoder
import requests
location = geocoder.google('500 El Camino Real, Santa Clara University')
lat = location.lat
long= location.lng
url =  'https://maps.googleapis.com/maps/api/elevation/json?locations=39.7391536,-104.9847034&key=AIzaSyArk1eMR0FxKIPft3DXbnpzgZ2-pE3YF-c'.format(lat,long)
response = requests.get(url)
attributes=response.json()
results= attributes

elevation = results[u'results']

for i in elevation:
    Altitude= i[u'elevation']
altraw = "%.2f" %Altitude
alt= "%.2f m" %Altitude

