'''
Created on 22.9.2014

@author: Joonas Turkka
'''
from nmfParser.Events.Event import Event
from nmfParser import RowParser
from nmfParser.RowParser import ConvertLonLatToXY

class EventGPS(Event):
    '''
    This class is inherited from Event and contains GPS event
    related variables.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.lon = float()  
        self.lat = float()
        self.height = int() #TODO find a way to define height as int and still input null value.
        self.distance = int()
        self.gps_fix = int()
        self.satellites = int()
        self.velocity = int()
        self.measured_CELLMEASevents = list() #Empty list for CELLMEAS events linked to GPS
         
    def AddValuesTo(self, event_type, event_time, row):
        super().__init__(event_type, event_time)    #pass type and time to base class
        self.lon = RowParser.ReadFloat(row[3]) 
        self.lat = RowParser.ReadFloat(row[4])
        self.height = row[5] #TODO find a way to define height as int and still input null value.
        self.distance = row[6]
        self.gps_fix = row[7]
        self.satellites = row[8]
        self.velocity = row[9]
        
    def AddCellMeasEvent (self, cellmeas_):
        self.measured_CELLMEASevents.append(cellmeas_)
        
    def GetLongitude(self):
        return self.lon
    
    def GetLatitude(self):
        return self.lat
    
    def GetXY(self):
        return ConvertLonLatToXY(self.lon, self.lat)
    
        