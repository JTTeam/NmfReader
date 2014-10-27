'''
Created on 24.9.2014

@author: Jussi
'''
from nmfParser import RowParser

class Hist(object):
    '''
    Class for creating histogram objects based on dictionary.
    Note: this could be inherited from Dictionary...
    '''


    def __init__(self, header="no-title-given"):
        '''
        Constructor for histogram object.
        '''
        self.header_ = header
        self.histogram_ = dict()
        self.count_     = 0;
        
    def AddInt(self, key):
        self.Add(RowParser.ReadInt(key))
        
        
    def Add(self, key):
        '''
        Increase the count of key (and total count)
        '''
        if key in self.histogram_:
            self.histogram_[key] += 1
        else:
            self.histogram_[key] = 1
            
        self.count_ += 1
        
    def __str__(self):
        '''
        __str__ is executed when object is call by print( obj )
        '''
        print("-Histogram of " + self.header_)
        sum_ = int(0)
        for key_name in self.histogram_:
            val_ = self.histogram_[key_name]
            sum_ += val_
            print( str(key_name) + ": " + str(val_) + ": " + str(round(sum_/self.count_,2)) )
            
        return "-end of histogram (" + str(self.count_) + " samples in " + str(len(self.histogram_))  + " elements)-"