'''
Created on 26.9.2014

@author: Joonas
'''
from nmfParser.Math.Hist import Hist

class WriteHistStats(object):
    '''
    This class writes out histogram statistics to txt file.
    '''
    def __init__(self, conf):
        '''
        Constructor
        '''
        self.path = conf.outputPath
        self.filePrefix = conf.filePrefix
        self.filename = str()

    '''   
    def writeOutHist(self, eventContainer, filename="hist_test.txt"):
        #define output file
        self.filename = self.path + "\\" + self.filePrefix + filename
        
        with open(self.filename, "w") as out_file:
            out_file.write("EventContainer Statistics:\n")
            for header in eventContainer.eventStats_:
                out_file.write(header + ": " + str(eventContainer.eventStats_[header]) + "\n")
            self.writeEventStat(eventContainer.cellStats_, out_file)
            self.writeEventStat(eventContainer.wlanStats_, out_file)
            self.writeEventStat(eventContainer.rsrpStats_, out_file) 
    '''
            
    def GetAbsolutePath(self, filename):
        return self.path + "\\" + self.filePrefix + filename
               
               
    def WriteHistogram(self, histogram, filename="hist_test.txt"):
        ''' this method writes histogram to file'''
        
        self.filename = self.GetAbsolutePath(filename)
        with open(self.filename, "w") as out_file:
            self.WriteHistObject(histogram, out_file)

                    
    def WriteHistObject(self, obj, out_file):
        
        #header line
        out_file.write("#bin, count, cdf\n")
        
        #cumulative sum for the cdf
        cumsum_ = int(0)
            
        for key_name in obj.histogram_:
            val_ = obj.histogram_[key_name]
            cumsum_ += val_
            out_file.write(str(key_name) + ", " + str(val_) + ", " + str(round(cumsum_/obj.count_,2)) + "\n")
       
       
    def WriteUIDList(self, uidlist, filename="uid_list.txt"):
        ''' 
        this method writes UID list to file
        '''
        
        self.filename = self.GetAbsolutePath(filename)
        
        with open(self.filename, "w") as out_file:
            for cgi in uidlist.uniqueIDs_:
                uid = uidlist.uniqueIDs_[cgi]
                out_file.write(str(uid) + " = " + str(cgi) + "\n")
            