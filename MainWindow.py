'''
Created on 29/09/2010

@author: veryweb
'''
import Tkinter
from Tkinter import tkinter, Tk
class MainWindow(object):
    def __init__(self,parent,controller=None):
        #fonts used in title and buttons
        self.fontTitle = ("arial",14,"bold")
        self.__fontButton = ("arial",12,"bold")
        
        #the GUI controller
        self.controller = controller
        
        # The parent Tk
        self.parent = parent
        
        #The frame that is going to support the whole GUI
        self.frame = Tkinter.Frame(parent)
        #Two buttons 
        self.buttonEncode = Tkinter.Button(self.frame,text="ENCRYPT",font=self.__fontButton)
        self.buttonDecod = Tkinter.Button(self.frame,text="DECRYPT",font=self.__fontButton)
        
    def init(self):
        ''' '''
        """ The following code forces the columns and rows to 
        take the whole space, and redimensions the frame
        """
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=10)
        
        """Add a label"""
        Tkinter.Label(self.frame,font=self.fontTitle,text="ENCRYPTION/DECRYPTION TOOL").grid(row = 0,columnspan=2)
        """Dimension the buttons"""
        self.buttonEncode.config(width=10,height=2)
        self.buttonDecod.config(width=10,height=2)
        self.buttonEncode.grid(column = 0, row = 1,sticky=Tkinter.N)
        self.buttonDecod.grid(column = 1, row = 1,sticky=Tkinter.N)
        
        # Add commands to the buttons
        self.buttonEncode.config(command=self.controller.goToEncodeWindow)
        self.buttonDecod.config(command=self.controller.goToDecodeWindow)
    