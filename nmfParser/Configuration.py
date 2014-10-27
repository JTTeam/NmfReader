'''
Created on 19.9.2014

@author: Jussi
'''
import csv
import os
from inspect import stack

class Configuration(object):
    '''
    classdocs
    '''
    
    def __init__(self):
        '''
        Constructor
        '''

        self.configFile = "config.txt"
        
        self.inputPath = ""
        self.inputFile =  []
        
        self.filePrefix = ""
        self.fileExtension = ""
        
        self.outputPath = ""
        
        self.nemoHeaders = []
        
        # 7=LTE-FDD, 20=WLAN
        self.readSystems = []
        
        # -1 = read all available LTE cells / WLAN APs
        self.maxNumberOfCells = 0
        self.maxNumberOfAPs = 0
        
        self.mdtOutputFileName = ""
        self.nefOutputFileName = ""
        
                  
    def __str__(self):
        print()
        print("inputPath: \t"  + self.inputPath)
        print("inputFiles: \t" + ', '.join(self.inputFile))
        print("fileExtension: \t" + self.fileExtension)
        print("outputPath: \t" + self.outputPath)
        print("nemoHeaders: \t" + ', '.join(self.nemoHeaders))
        print("readSystems: \t" + ', '.join(self.readSystems))
        
        return "- end of configuration -"
    
    def readConfigFile(self):
        test = os.path.join(os.getcwd(), self.configFile)
        with open(test, newline='') as confFile:
            reader = csv.reader(confFile, delimiter="=")
            for row in reader:
                print(row[0])
                if row[0] == "inputPath":
                    self.inputPath = row[1]

                elif row[0] == "inputFile":
                    self.inputFile = row[1]

                elif row[0] == "filePrefix":
                    self.filePrefix = row[1]

                elif row[0] == "fileExtension":
                    self.fileExtension = row[1]

                elif row[0] == "outputPath":
                    self.outputPath = row[1]

                elif row[0] == "nemoHeaders":
                    headerList = row[1].split(",")
                    for header in headerList:
                        self.nemoHeaders.append(header)

                elif row[0] == "readSystems":
                    systemList = row[1].split(",")
                    for system in systemList:
                        self.readSystems.append(system)

                elif row[0] == "mdt.maxNumberOfCells":
                    self.maxNumberOfCells = row[1]

                elif row[0] == "mdt.maxNumberOfAPs":
                    self.maxNumberOfAPs = row[1]

                elif row[0] == "mdt.OutputFileName":
                    self.mdtOutputFileName = row[1]
                    
                elif row[0] == "nef.OutputFileName":
                    self.nefOutputFileName = row[1]

                                                            

                        
        
