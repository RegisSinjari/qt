import ctypes
import platform;
from ctypes import *
import os
from math import radians, cos, sin, asin, sqrt
from time import time
def haversiness(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance in kilometers between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    return c * r
# print(platform.architecture())

"""

start=time()
my_functions = CDLL(os.path.abspath("my_functionss.so"))
my_functions.haversine.restype=ctypes.c_float
my_functions.haversine.argtypes=[ctypes.c_float,ctypes.c_float,ctypes.c_float,ctypes.c_float]
for a in range(1000000):
    #print(my_functions.haversine(41.324191662543235, 19.821685354484984,41.33424587468876, 19.87095199805423))
    lat1 = 41.324191662543235 + a
    lon1 = 19.821685354484984 + a
    lat2 = 41.33424587468876 + a
    lon2 = 19.87095199805423 + a
    print(my_functions.haversine(lat1, lon1, lat2, lon2))
end=time()
print("time",end-start)


"""
start2=time()

for a in range(1000000):
    lat1 = 41.324191662543235+a
    lon1 = 19.821685354484984+a
    lat2 = 41.33424587468876+a
    lon2 = 19.87095199805423+a

    print(haversiness(lat1, lon1,lat2, lon2))
end2=time()
print("time",end2-start2)