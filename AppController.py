'''
Created on 03/10/2010

@author: veryweb
'''
from GuiController import GuiController
import ProcessModel
import Security

class AppController(object):
    
    def __init__(self):
        # The process model
        self.__processModel = None
        self.guiController = None
        
    def init(self):
        #Create the model
        self.__processModel = ProcessModel.ProcessModel()
        self.guiController = GuiController(self)
        self.guiController.init(self.__processModel)
        
    def setSource(self,text):
        print "SET SOURCE",text
        self.__processModel.setSource(text)
        
    def setDestination(self,text):
        print "SET Destination",text
        self.__processModel.setDestination(text)
        
    def encrypt(self,password):
        if (self.__processModel.getStatus() != ProcessModel.READY):
            return
        else:
            Security.Security().encrypt(self.__processModel, password)
            
    def decrypt(self,password):
        if (self.__processModel.getStatus() != ProcessModel.READY):
            return
        else:
            Security.Security().decrypt(self.__processModel, password)
        
        
AppController().init()