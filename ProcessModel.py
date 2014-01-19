'''
Created on 02/10/2010

@author: veryweb
'''

NOT_READY = 0
READY = 1

class ProcessModel(object):
    
    def __init__(self):
        self.__source = ""
        self.__destination = ""
        self.__status = NOT_READY
        self.__listeners = list()
        
    def setSource(self,text):
        if len(text)> 0:
            self.__source = text
            self.__updateStatus()
            self.__notify()
            
    def getSource(self):
        return self.__source
    
    def getDestination(self):
        return self.__destination
    
    def getStatus(self):
        return self.__status
            
    def setDestination(self,text):
        if len(text)> 0:
            self.__destination = text
            self.__updateStatus()
            self.__notify()
            
    def reset(self):
        self.__source = ""
        self.__destination = ""
        self.__status = NOT_READY
        self.__notify()
            
    def addListener(self,listener):
        self.__listeners.append(listener)
        self.__notify()
            
    def __updateStatus(self):
        if len(self.__source) > 0 and len(self.__destination) > 0:
            self.__status = READY
            
    def __notify(self):
        for x in self.__listeners:
            x.onModelChanged(self)