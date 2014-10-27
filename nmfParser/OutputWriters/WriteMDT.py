'''
Created on 27.9.2014

@author: Joonas Turkka
'''
from nmfParser.MDT.MDTContainer import MDTContainer

class WriteMDT(object):
    '''
    This class writes out MDTfile from given event information
    '''


    def __init__(self, conf):
        '''
        Constructor
        '''
        self.path = conf.outputPath
        self.filePrefix = conf.filePrefix
        self.IntialFilename = conf.mdtOutputFileName
        self.filename = str()
        
        
    def WriteOutMDT(self, mdtContainer):
        self.filename = self.path + "\\" + self.filePrefix + self.IntialFilename
        
        with open(self.filename, "w") as out_file:
            for mdtEvent in mdtContainer.mdtlog_:
                row = mdtEvent.GetRow()
                row_str = ','.join(map(str,row))
                out_file.write(row_str + "\n")
        