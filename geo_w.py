#!/bin/env python
# -*- coding: utf-8 -*-

""" 
* author Allen.L
* \last modified 2022-09-06 10:27:26
""" 

# from geopy.geocoders import Nominatim
# from geopy.distance import geodesic
from math import sin, asin, cos, radians, fabs, sqrt
import sys


# geolocator = Nominatim(user_agent="geoapiExercises")

Longitude = 99.902768
Latitude = 20.461323

# location = geolocator.reverse(str(Latitude) + "," + str(Longitude))

# address = location.raw['address']
# print(address)


EARTH_RADIUS = 6371.137      # 地球平均半径大约6371km

def hav(theta):
    s = sin(theta / 2)
    return s * s
 
def get_distance_hav(lat0, lng0, lat1, lng1):
    # 用haversine公式计算球面两点间的距离
    # 经纬度转换成弧度
    lat0 = radians(lat0)
    lat1 = radians(lat1)
    lng0 = radians(lng0)
    lng1 = radians(lng1)
    dlng = fabs(lng0 - lng1)
    dlat = fabs(lat0 - lat1)
    h = hav(dlat) + cos(lat0) * cos(lat1) * hav(dlng)
    distance = 2 * EARTH_RADIUS * asin(sqrt(h))      # km
    return distance
 
if __name__ == "__main__":
    for line in sys.stdin:
        uid,lon,lat = line.strip().split('\t')
        # print(uid,float(lon),float(lat),sep='\t')
        long2 = float(lon)
        lati2 = float(lat)
        result = get_distance_hav(Latitude, Longitude, lati2, long2)
        if result < 1.00:
            print(uid,"%f"%(result),sep='\t')
