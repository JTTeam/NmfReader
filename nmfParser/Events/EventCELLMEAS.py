'''
Created on 21.9.2014

@author: Jussi
'''
from nmfParser.Events.Event import Event

class EventCELLMEAS(Event):
    '''
    This class is inherited from Event and contains CELLMEAS event
    related variables.
    '''


    def __init__(self):
        '''
        Constructor for EventCELLMEAS
        '''
        self.system_ = int()                  #7=LTE-FDD, 20=WLAN (int)
        self.num_of_headers = int()           #!maybe no need to store
        self.num_of_cells = int()             #number of measured cells(int)
        self.num_of_params_per_cell = int()   #!maybe no need to store
        self.measured_cells = list()          #empty list of cells
        
        
    def AddValuesTo(self, event_type, event_time, row):
        super().__init__(event_type, event_time)    #pass type and time to base class
        self.system_ = int(row[3])                  
        self.num_of_headers = row[4]                
        self.num_of_cells = int(row[5])             
        self.num_of_params_per_cell = row[6]
        
    def AddCellMeas(self, a_cell):
        '''This method is called to add the individual cell measurement objects '''
        self.measured_cells.append(a_cell)


    def GetSystem(self):
        return self.system_

    
    def GetSystemAsStr(self):
        if self.system_ == 7:
            return 'LTE-FDD'
        elif self.system_ == 20:
            return 'WLAN'
        else:
            return 'NOT_DEF'

        
    def GetNumOfCells(self):
        return self.num_of_cells

    
    def GetServingRSS(self):

        rss = float() #'NOT_DEF'

        if self.system_ == 7 and self.measured_cells[0].IsServing():
            rss = self.measured_cells[0].GetReceivedSignalStrength()
            
        elif self.system_ == 20:
            rss = self.measured_cells[0].GetReceivedSignalStrength()
            
        return (rss)
    
    def GetServingRSQ(self):

        rsq = float(-30) #'NOT_DEF'

        if self.system_ == 7 and self.measured_cells[0].IsServing():
            rsq = self.measured_cells[0].GetReceivedSignalQuality()
            
        elif self.system_ == 20:
            rsq = self.measured_cells[0].GetReceivedSignalQuality()
            
        return (rsq)

    
    def GetGlobalID(self, nth_cell):
        if nth_cell < self.num_of_cells:
            if self.system_ == 7:
                return self.measured_cells[nth_cell].GetCGI()
            elif self.system_ == 20:
                return self.measured_cells[nth_cell].GetCGI()
            else:
                print("Cellmeas: System not supported!")


    def SetUniqueID(self, nth_cell, uid):
        if nth_cell < self.num_of_cells:
            self.measured_cells[nth_cell].SetUniqueID(uid)
