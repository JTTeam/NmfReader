'''
Created on 19.9.2014

@author: Jussi Turkka
'''
from nmfParser.Configuration import Configuration
from nmfParser.parseInputFiles import parseInputFiles
from nmfParser.Events.EventContainer import EventContainer
from nmfParser.OutputWriters.WriteStats import WriteHistStats
from nmfParser.OutputWriters.WriteMDT import WriteMDT
from nmfParser.OutputWriters.WriteNEF import WriteNEF
from nmfParser.MDT.MDTContainer import MDTContainer
from nmfParser.NEF.NefContainer import NefContainer

def main():
    
    # 1.) read configuration
    conf_ = Configuration()
    conf_.readConfigFile()
    print(conf_)
  
    # 2.) initialize eventContainer
    eventContainer = EventContainer()
    
    # 3.) parse inputfiles
    fileParser = parseInputFiles(conf_)
    fileParser.ParseFilesTo(eventContainer)
    
    # 4.) print some overview stats
    eventContainer.PrintEventHistograms()
    
    # 5.) export data
    outputWriter = WriteHistStats(conf_)
    eventContainer.WriteHistogramsTo(outputWriter)
    
    # 6.) create MDT log file
    mdtContainer = MDTContainer(conf_, eventContainer.GetEvents())
    mdtWriter = WriteMDT(conf_)
    mdtWriter.WriteOutMDT(mdtContainer)
    
    # 7.) create NEF log file
    nefContainer = NefContainer(mdtContainer)
    nefWriter = WriteNEF(conf_)
    nefWriter.WriteOutNEF(nefContainer)
    pass



if __name__ == '__main__':
    main()