'''
Created on 22.9.2014

@author: Joonas
'''
from nmfParser.Events.Event import Event

class EventTAD(Event):
    '''
    This class is inherited from Event and contains TAD event
    related variables.
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.measured_sys = int() 
        self.ta = int()  
        
    def AddValuesTo(self, event_type, event_time, row):
        super().__init__(event_type, event_time)    #pass type and time to base class
        self.measured_sys = row[3] #Measured system, 1 = GSM, 6 = UMTS TD-SCDMA, 7 = LTE FDD, 8 = LTE TDD, 53 = DAMPS
        self.ta = row[4]  #Timing advance. for LTE range 0-1282. 
        
    def GetMeasuredSystem(self):
        return self.measured_sys
    
    def GetMeasuredSystemAsStr(self):
        if self.measured_sys == 1:
            return 'GSM'
        elif self.system_ == 6:
            return 'UMTS TD-SCDMA'
        elif self.system_ == 7:
            return 'LTE FDD'
        elif self.system_ == 8:
            return 'LTE TDD'
        elif self.system_ == 53:
            return 'DAMPS'
        else:
            return 'NOT_DEF'