#!/usr/bin/python3
import geocoder

if __name__ == '__main__':
    address = '207 N. Defiance St, Archbold, OH'
    location = geocoder.osm(address)
    print(location.latlng)
