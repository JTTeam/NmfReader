'''
Created on 9.10.2014

@author: Jussi
'''

class RFMeasurement(object):
    '''
    Class definition for MDT RF measurement
    '''

    def __init__(self, event):
        '''
        Constructor
        '''
        
        self.id_ = event.GetUniqueID()
        self.rss_ = event.GetReceivedSignalStrength()
        self.rsq_ = event.GetReceivedSignalQuality()
        
    def __str__(self):
        return str(self.id_) + ',' + str(self.rss_)