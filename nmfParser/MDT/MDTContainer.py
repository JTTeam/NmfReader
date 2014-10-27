'''
Created on 9.10.2014

@author: Jussi
'''
from nmfParser.Events.Event import Event
from nmfParser.MDT.MDTEvent import MDTEvent

class MDTContainer(object):
    '''
    MDT container class reads events from event container and creates MDT log file
    '''


    def __init__(self, conf, events):
        '''
        Constructor
        '''
        self.conf_ = conf           # store reference to configuration
        self.mdtlog_ = list()       # empty list of mdt_rows
        self.latest_events = dict() #
        self.latest_gps_ = Event()  # fixme: use proper constructor
        self.latest_lte_ = Event()  # fixme: use proper constructor
        self.latest_wlan_= Event()  # fixme: use proper constructor
 
        self.counter_ = int(0)      # number of created MDT events      
        
        #for loop the events and create MDT
        self.LoopEvents(events)
        
        
        
    def LoopEvents(self, events):
        '''
        This method goes through all events, stores the latest and 
        creates corresponding MDT samples
        '''
        
        NumOfEvents = len(events)
        
        for i in range(0, NumOfEvents):
    
            if events[i].IsType('GPS'):
                ''' if event type is GPS, store it as latest GPS'''
                self.latest_gps_ = events[i]
                
            elif events[i].IsType('CELLMEAS'):
                if events[i].GetSystemAsStr() == 'WLAN':
                    ''' if WLAN CELLMEAS, store it as latest wlan'''
                    self.latest_wlan_ = events[i]
                    
                elif events[i].GetSystemAsStr() == 'LTE-FDD':
                    ''' if LTE CELLMEAS, create a new MDT row'''
                    self.latest_lte_ = events[i]
                    self.mdtlog_.append( self.CreateMDTEvent() )
                    

    def CreateMDTEvent(self):
        '''
        This method creates a row in mdtlog using latest gps and cellmeas logs
        '''
        self.counter_ += 1
        
        mdt_event = MDTEvent(self.latest_gps_,
                             self.latest_lte_,
                             self.latest_wlan_,
                             self.counter_)
        
        #row = mdt_event.GetRow()
        
        return mdt_event
            
        
        