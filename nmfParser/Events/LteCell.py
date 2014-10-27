'''
Created on 24.9.2014

@author: Joonas Turkka
'''

import nmfParser.RowParser
from nmfParser.RowParser import ReadFloat

class CellLTE(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cellType = int()               # 0=serving, 1=listed, 2=detected
        self.band = int()                   # 70007 = band7, 70009 = band9, 70020 = band20 etc.
        self.ch = int()                     # channel number e.g., earfcn
        self.pci = int()                    # pci = [0-503]
        self.rssi = float()                 # rssi = total received power
        self.rsrp = float()                 # rsrp = reference signal received power
        self.rsrq = float()                 # rsrq = reference signal received quality [-30 .. 0]
        self.uknown_param8 = str()
        self.uknown_param9 = str()

        
        
    def AddValuesTo(self, cellList):
        
        self.cellType = int(cellList[0])    #note: Doesn't work without int(row[0])??
        self.band = cellList[1]
        self.ch = cellList[2]
        self.pci = cellList[3]
        self.rssi = cellList[4]             #note: but doesn't work either with float(row[4])
        self.rsrp = cellList[5]             
        self.rsrq = ReadFloat(cellList[6])
        self.uknown_param8 = cellList[7]
        self.uknown_param9 = cellList[8]
        
        self.unique_id = int(-7)
        
        
    def IsServing(self):
        if self.cellType == 0:
            return True
        else:
            return False
        
    def GetReceivedSignalStrength(self):
        return self.rsrp
    
    def GetReceivedSignalQuality(self):
        return self.rsrq
        
    def GetCGI(self):
        return str(self.ch) + "_" + str(self.pci)
    
    def SetUniqueID(self, uid):
        self.unique_id = uid
    
    def GetUniqueID(self):
        return self.unique_id