'''
Created on 20.9.2014

@author: Joonas Turkka
'''

import csv
import os
from datetime import time, datetime
#from nmfParser.Events.EventContainer import EventContainer
#from nmfParser.Events.Event import Event
from nmfParser.Events.EventCELLMEAS import EventCELLMEAS
from nmfParser.Events.EventGPS import EventGPS
from nmfParser.Events.EventTAD import EventTAD
from nmfParser.Events.LteCell import CellLTE
from nmfParser.Events.WlanCell import CellWLAN
from nmfParser.Events.TraceInfo import TraceInfo


class parseInputFiles(object):
    '''
    classdocs
    '''
    def __init__(self, conf):
        '''
        Constructor
        '''
        self.topdir_ = conf.inputPath
        self.exten_ = conf.fileExtension
        self.headers_ = conf.nemoHeaders
        self.currentTrace = None            #Contains information about current nfm trace file
        self.currentGPS = EventGPS()
        self.tempEventHolder = list()
        self.tempDate = str()
        
    def ParseFilesTo(self, eventContainer):
        
        result = str()
        for dirpath, dirnames, files in os.walk(os.path.abspath(self.topdir_)): #gets parent directory 
            for name in files:
                if name.lower().endswith(self.exten_):
                    result = os.path.join(dirpath, name)
                    with open(result, newline='') as nmfFile:
                        reader = csv.reader(nmfFile)
                        self.UpdateCurrentTrace(name)
                        for row in reader:
                            if row[0] == "#START":
                                self.tempDate = row[3]
                                self.currentTrace.Start(self.CombineDateAndTime(row[1], row[3]))
                            if row[0] == "#STOP":                                
                                self.currentTrace.Stop(self.CombineDateAndTime(row[1], row[3]))
                            if row[0] in self.headers_: #compares nemoHeadears to nmf file row header
                                new_event = self.CreateEventFrom(row)
                                new_event.AddTraceInfo(self.currentTrace)
                                eventContainer.AddEvent(new_event)
                        print("Measurement duration: " + str(self.currentTrace.GetDuration()))   
    
    
    def UpdateCurrentTrace(self, new_filename):
        ''' this method keeps track of the current trace file'''
        if self.currentTrace is None:
            new_id = int(0)
        else:
            new_id = self.currentTrace.id_ + 1
            
        self.currentTrace = TraceInfo(new_id, new_filename)
        print(self.currentTrace)
    
    def CreateEventFrom(self, row):
        ''' 
        CreateEvent method checks row type and passes the row to right event constructor.
        This must have an implementation for all supported events.
        '''
            
        if row[0] == 'GPS':
            return self.CreateGPS(row)
        elif row[0] == 'TAD':
            return self.CreateTAD(row)
        elif row[0] == 'CELLMEAS':
            return self.CreateCELLMEAS(row)
        else: 
            print("FAILURE: Unsupported NemoHeader configured!")
            
            
    def CreateGPS(self, row):
        ''' 
        CreateGPS method knows how to parse row to create a GPSEvent
        fixme: now all events are base class objects
        '''
        event_type = row[0]
        event_time = row[1]

        if self.currentGPS != None:
            self.currentGPS.measured_CELLMEASevents = self.tempEventHolder
    
        new_event = EventGPS()       
        new_event.AddValuesTo(event_type, event_time, row)
        self.currentGPS = new_event
        return new_event
    
    def CreateTAD(self, row):
        ''' 
        CreateTAD method knows how to parse row to create a TADEvent
        fixme: now all events are base class objects
        '''
        event_type = row[0]
        event_time = row[1]
        
        new_event = EventTAD()
        new_event.AddValuesTo(event_type, event_time, row)
        return new_event
    
    
    def CreateCELLMEAS(self, row):
        ''' 
        CreateCELLMEAS method knows how to parse row to create a CELLMEASEvent
        fixme: now all events are base class objects currently. 
        '''
        
        event_type = row[0]
        event_time = row[1]
        
        new_event = EventCELLMEAS()
        new_event.AddValuesTo(event_type, event_time, row)
        if self.currentGPS != None:
            self.tempEventHolder.append(new_event)
        '''todo: for loop through the cells and Add them to new_event '''
        
        param_count = 1
        templist = list()
        for i in range(7,len(row)):
            templist.append(row[i])
            if param_count == int(new_event.num_of_params_per_cell):
                if new_event.system_ == 7:
                    tempCell = CellLTE()
                    tempCell.AddValuesTo(templist)
                    new_event.AddCellMeas(tempCell)
                elif new_event.system_ == 20:
                    tempCellb = CellWLAN()
                    tempCellb.AddValuesTo(templist)
                    new_event.AddCellMeas(tempCellb)
                templist.clear()
                param_count = 1
            else:
                param_count = param_count+1
        
        return new_event
    
    
    def CombineDateAndTime(self, timestmp, date):
        date_object = datetime.strptime(date, "%d.%m.%Y")
        time_object = datetime.strptime(timestmp, "%H:%M:%S.%f") #converts timestamp to datetime object.
        datetimeStmp = datetime.combine(date_object.date(), time_object.time()) 
        return datetimeStmp

    
    
        
            
        
