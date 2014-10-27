'''
Created on 12.10.2014

@author: Jussi
'''

class TraceInfo(object):
    '''
    TraceInfo object holds information nmf file statistics
    '''


    def __init__(self, id, name):
        '''
        Constructor
        '''
        self.id_ = id
        self.name_ = name
        self.start_ = None          #todo: think what is needed
        self.stop_ = None           #todo: think what is needed
        
    def Start(self, start):
        self.start_ = start
        
    def Stop(self, stop):
        self.stop_ = stop
        
    def GetDuration(self):
        return self.stop_ - self.start_
    
    def GetId(self):
        return self.id_
    
    def GetStartTime(self):
        return self.start_
    
    def __str__(self):
        return str(self.id_) + ' = ' + str(self.name_)