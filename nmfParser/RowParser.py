'''
Created on 12.10.2014

@author: Jussi Turkka
'''

from datetime import time, datetime, timedelta
import calendar
import pyproj
#import mpl_toolkits.basemap.pyproj as pyproj # Import the pyproj module

''' this file contains short methods needed to parse nmf files '''

def ReadInt(value, default=0):
    try:
        return int(value)
    except:
        return default
    

def ReadFloat(value, default=None):
    try:
        return float(value)
    except: 
        return default
        
def CalcTimeDifference(time1, time2):
    timeDiff = time2 - time1
    return timeDiff

def ConvertToDateTimeObject(timestmp):
    time_object = datetime.strptime(timestmp, "%H:%M:%S.%f") #converts timestamp to datetime object.
    return time_object

def ConvertLonLatToXY(lon, lat):
    ''' this method converts GPS coordinates latitude (y) and longitude(x) to XY plane'''
    #wgs84=pyproj.Proj("+init=EPSG:4326")    # LatLon with WGS84 datum used by GPS units
    #(x1,y1) = wgs84(lon, lat)
    
    #kkj = pyproj.Proj("+init=EPSG:2393")    # KKJ coordinate system
    #(x2,y2) = pyproj.transform(wgs84, kkj, x1, y1)
    
    if lon != None and lat != None:
        myProj = pyproj.Proj("+proj=utm +zone=34V, +north +ellps=WGS84 +datum=WGS84 +units=m +no_defs")
        (x3,y3) = myProj(lon, lat)
    
        DoProjection = True
        if DoProjection:
            return(x3,y3)

    return(lon, lat)

def ConvertToPOSIX(timestamp):
    return calendar.timegm(timestamp.timetuple())
     
    
                       
    