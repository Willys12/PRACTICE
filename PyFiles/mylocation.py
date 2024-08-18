#!/usr/bin/env python3
import geocoder

if __name__ == '__main__':
    latitude = -1.2833
    location = geocoder.osm([latitude, 0], method='reverse')
    print("Latitude: ", location.latlng[0])
    print("Longitude: ", location.latlng[1])
