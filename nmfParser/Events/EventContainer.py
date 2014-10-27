'''
Created on 20.9.2014

@author: Jussi
'''

#from nmfParser.Events.Event import Event
#from nmfParser.Events.EventCELLMEAS import EventCELLMEAS
from nmfParser.Math.Hist import Hist
from nmfParser.OutputWriters.WriteStats import WriteHistStats
from nmfParser.Events.IDContainer import IDContainer

class EventContainer(object):
    '''
    Event container stores all the nmf events and maintains various statistics
    @events_ is a list containing all parsed MeasurementEvents
    @stats_ is a histogram showing how many events of certain type has been recorded
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.events_ = list()                   #list of events
        self.eventStats_ = dict()               #for counting occurrence of different events
        self.uniqueIDs_ = IDContainer()        #for maintaining list of unique IDs
        
        self.cellStats_ = Hist('LTE CELLS')     #histogram of measured LTE cells
        self.wlanStats_ = Hist('WLAN APs')      #histogram of measured WLAN cells
        self.rsrpStats_ = Hist('LTE RSRP')      #histogram of RSRP for serving cell
        self.rsrqStats_ = Hist('LTE RSRQ')      #histogram of RSRP for serving cell
        self.rssiStats_ = Hist('WLAN RSSI')     #histogram of RSSI for strongest wlan cell
        self.lte_cgiStats_  = Hist('LTE/CGI')       #histogram of unique LTE CGIs
        self.wlan_cgiStats_ = Hist('WLAN/CGI')
        
    def AddEvent(self, event):
        '''
        Adds new event to the events_ list and updates stats_ histogram
        '''
        
        self.UpdateEventCounters(event)
        
        if event.IsType('CELLMEAS'):
            self.UpdateCellCounters(event)
            self.UpdateUniqueCellIDs(event)
            
        self.events_.append(event)
        
    def WriteHistogramsTo(self, writer):
            writer.WriteHistogram(self.rsrpStats_, "rsrp_histogram.txt")
            writer.WriteHistogram(self.rsrqStats_, "rsrq_histogram.txt")
            writer.WriteHistogram(self.rssiStats_, "rssi_histogram.txt")
            writer.WriteHistogram(self.cellStats_, "cells_LTE_histogram.txt")
            writer.WriteHistogram(self.wlanStats_, "cells_WLAN_histogram.txt")
            
            writer.WriteHistogram(self.lte_cgiStats_, "cgi_LTE_hist.txt")
            writer.WriteHistogram(self.wlan_cgiStats_, "cgi_WLAN_hist.txt")
            
            writer.WriteUIDList(self.uniqueIDs_, "uid_list.txt")
            
    def PrintEventHistograms(self):
        '''PrintEventHistogram prints how many times a certain event has occurred '''
        print("EventContainer Statistics:")
        for header in self.eventStats_:
            print( header + ": " + str(self.eventStats_[header]) )
            
        ''' print statistics for number of detected cells per measurement'''
        #print(self.cellStats_)
        #print(self.wlanStats_)
        
        ''' print rsrp histogram for serving cell'''
        #print(self.rsrpStats_)
        
        #print(self.lte_cgiStats_)
        #print(self.wlan_cgiStats_)
    
    
    def UpdateEventCounters(self, event):
        ''' 
        Check if event type is found and increment histogram by one,
        otherwise initialize to 1.
        '''
        event_type = event.GetType()
        if event.IsType('CELLMEAS'):
            event_type = event_type + "(" + event.GetSystemAsStr() + ")"
            
        if event_type in self.eventStats_:
            self.eventStats_[event_type] += 1
        else:
            self.eventStats_[event_type] = 1
    
           
    def UpdateCellCounters(self, event):
        ''' 
        Check if event type is found and increment histogram by one,
        otherwise initialize to 1.
        '''
        num_of_cells = event.GetNumOfCells()
        if event.GetSystemAsStr() == 'LTE-FDD' and num_of_cells > 0: 
            self.cellStats_.Add(num_of_cells)
            ''' update rsrp stats (similar to mdt log)'''
            rsrp = event.GetServingRSS()
            rsrq = event.GetServingRSQ()
            self.rsrpStats_.AddInt(rsrp)
            self.rsrqStats_.AddInt(rsrq)

        elif event.GetSystemAsStr() == 'WLAN' and num_of_cells > 0: 
            self.wlanStats_.Add(num_of_cells)
            rssi = event.GetServingRSS()
            self.rssiStats_.AddInt(rssi)

    def UpdateUniqueCellIDs(self, event):
        ''' 
        Check if CGI is found and add it to the CGI histogram
        '''
        
        for nth_cell in event.measured_cells:
            cgi = nth_cell.GetCGI()
            uid = self.uniqueIDs_.GetUID(nth_cell, event.GetSystem())
            nth_cell.SetUniqueID(uid)
            
            if event.GetSystemAsStr() == 'LTE-FDD': 
                self.lte_cgiStats_.Add(cgi)
                
            elif event.GetSystemAsStr() == 'WLAN': 
                self.wlan_cgiStats_.Add(cgi)
        '''
        num_of_cells = event.GetNumOfCells()
        if num_of_cells > 0:
            for nth_cell in range(num_of_cells):
                cgi = event.GetGlobalID(nth_cell)
                uid = self.uniqueIDs_.GetUID(cgi)
                event.SetUniqueID(nth_cell, uid)
                
                if event.GetSystemAsStr() == 'LTE-FDD': 
                    self.lte_cgiStats_.Add(cgi)
                
                elif event.GetSystemAsStr() == 'WLAN': 
                    self.wlan_cgiStats_.Add(cgi)
        '''
                    
    def GetEvents(self):
        return self.events_
            
        
