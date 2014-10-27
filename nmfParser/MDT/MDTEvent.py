'''
Created on 9.10.2014

@author: Jussi
'''
from nmfParser.Events.Event import Event
from nmfParser.Events.EventGPS import EventGPS
from nmfParser.Events.EventCELLMEAS import EventCELLMEAS
from nmfParser.MDT.RFMeasurement import RFMeasurement
from nmfParser import RowParser
from nmfParser.RowParser import ConvertLonLatToXY


class MDTEvent(object):
    '''
    classdocs
    '''


    def __init__(self, latest_gps, latest_lte, latest_wlan, event_count):
        '''
        Constructor
        '''
        self.traceReference_ = int(latest_lte.GetTraceId())         #TR
        self.traceRecordingSessionReference_ = int(event_count)     #TRSR
        tempTime = RowParser.CalcTimeDifference(latest_lte.GetTraceStartTime(), RowParser.ConvertToDateTimeObject(latest_lte.time_)) #calculates time from start to current event
        self.time_ = RowParser.ReadInt(((tempTime.seconds *1000) + (tempTime.microseconds / 1000))) #changes time to milliseconds
        self.latitude_ = latest_gps.GetLatitude()       # fixme: validity time should be checked
        self.longitude_ = latest_gps.GetLongitude()     # fixme: validity time should be checked
        
        self.measurements_ = list()
        
        # fill list of measurements from LTE
        if not latest_lte.IsType('NOT_DEF'):
            for i in range(0, latest_lte.num_of_cells):
                rf_meas = RFMeasurement( latest_lte.measured_cells[i] )
                self.measurements_.append( rf_meas )
            
        # .. the fill list with WLAN measurements
        if not latest_wlan.IsType('NOT_DEF'):
            for i in range(0, latest_wlan.num_of_cells):
                rf_meas = RFMeasurement( latest_wlan.measured_cells[i] )
                self.measurements_.append( rf_meas )
        
        
        # .. update num of RF measurements
        self.numOfLteCells = latest_lte.num_of_cells
        self.numOfWlanAPs = latest_wlan.num_of_cells
        self.numOfRFMeasurements_ = len(self.measurements_)
        
    def GetRow(self):
        '''
        this method returns mdt event in a list format for easy printing 
        '''
        row_ = list()
        row_.append(self.traceReference_)
        row_.append(self.traceRecordingSessionReference_)
        row_.append(self.time_)
        (x,y) = ConvertLonLatToXY(self.longitude_, self.latitude_)    #do projection xy plane
        row_.append(x)
        row_.append(y)
        row_.append(self.numOfRFMeasurements_)
        
        ''' extend row with the measurements '''
        row_.extend(self.measurements_)
        return row_