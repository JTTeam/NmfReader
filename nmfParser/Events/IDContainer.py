'''
Created on 10.10.2014

@author: Jussi
'''

class IDContainer(object):
    '''
    This object maintains a database of unique IDs for LTE/WLAN access nodes
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.uniqueIDs_ = dict()
        self.count_ = dict()
        
    def GetUID(self, nth_cell, sys_num):
        '''
        This method gets cells global id and maps it to simple unique id 
        '''
        cgi = nth_cell.GetCGI()
        
        sys_id = sys_num * 10000 #fixme: very brutal hard coded == not-so-nice-code
        
        if cgi in self.uniqueIDs_:
            # if cgi exists, then return the uid
            return self.uniqueIDs_[cgi]
        else:
            #.. otherwise, update uid
            self.uniqueIDs_[cgi] = sys_id + self.GetCount(sys_num)
            return self.uniqueIDs_[cgi]

    def GetCount(self, sys_num):
        if sys_num in self.count_:
            self.count_[sys_num] += 1
        else:
            self.count_[sys_num] = 0
            
        return self.count_[sys_num]
