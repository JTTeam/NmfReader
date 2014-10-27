'''
Created on 19.9.2014

@author: Jussi
'''

class Event(object):
    '''
    Event Class is the base class for all NFM events containing to member variables:
    @var type is the string for event type e.g., GPS, CELLMEAS, etc.
    @var time is the time variable for the sampling the of the event.
    '''


    def __init__(self, event_type = 'NOT_DEF', event_time = '00:00:00.0'):
        '''
        Constructor
        '''
        self.type_ = str(event_type)     #type as string e.g., 'GPS', 'TAD' or 'CELLMEAS'
        self.time_ = str(event_time)
        self.traceInfo_ = None
        
        
    def IsType(self, event_type):
        ''' IsType(event) returns true if self.event_ is event type 
            e.g., GPS, TAD or CELLMEAS '''
        if self.type_ == event_type:
            return True
        else: 
            return False
        
    def GetType(self):
        ''' GetType() returns the event type.'''
        return self.type_
    
    
    def AddTraceInfo(self, traceInfo):
        self.traceInfo_ = traceInfo
        
    def GetTraceId(self):
        return self.traceInfo_.GetId()
    
    def GetTraceStartTime(self):
        return self.traceInfo_.GetStartTime()