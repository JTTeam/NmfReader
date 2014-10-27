'''
Created on 24.9.2014

@author: Joonas Turkka
'''

class CellWLAN(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.cellType = int()
        self.band = int()
        self.quality = float()
        self.channel = int()
        self.rssi = float()
        self.ssid = str()
        self.mac_addr = str()
        self.security = int()
        self.max_transfer_rate = int()
        
        self.unique_id = int(-20)
        
        '''
        print(" celltype: " + cellList[0] + 
              " band: " + cellList[1] + 
              " quality: " + cellList[2] +
              " channel: " + cellList[3] +
              " rssi: " + cellList[4] +
              " ssid: " + cellList[5] +
              " MAC addres: " + cellList[6] + 
              " security: " + cellList[7] +
              " max transfer rate: " + cellList[8])
        '''
        
    def AddValuesTo(self, cellList):
        
        #self =  CellWLAN()
        self.cellType = cellList[0]
        self.band = cellList[1]
        self.quality = cellList[2]
        self.channel = cellList[3]
        self.rssi = cellList[4]
        self.ssid = cellList[5]
        self.mac_addr = cellList[6]
        self.security = cellList[7]
        self.max_transfer_rate = cellList[8]
        
    def GetReceivedSignalStrength(self):
        return self.rssi
    
    def GetReceivedSignalQuality(self):
        return self.quality        
        
    def GetCGI(self):
        return str(self.mac_addr)
    
    def SetUniqueID(self, uid):
        self.unique_id = uid
    
    def GetUniqueID(self):
        return self.unique_id