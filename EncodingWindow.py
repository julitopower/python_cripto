'''
Created on 29/09/2010

@author: veryweb
'''
import ProcessModel
from PasswordDialog import PassWordDialog
'''
Created on 29/09/2010

@author: veryweb
'''
import Tkinter, tkFileDialog
from Tkinter import tkinter, Tk
class EncodingWindow(object):
    """This window is responsible for capturing SOURCE and DESTINATION.
    it also captures the password to be used and request the encrypt
    operation"""
    def __init__(self,parent,controller):
        #fonts used in title and buttons
        self.fontTitle = ("arial",14,"bold")
        self.__fontButton = ("arial",12,"bold")
        self.__fontSmall = ("arial",9)
        
        #the GUI controller
        self.controller = controller
        
        # The parent Tk
        self.parent = parent
        
        #The frame that is going to support the whole GUI
        self.frame = Tkinter.Frame(parent)
        
        # In this case the GUI is composed of two frames:
        # top: To gather source and destination
        # bottom: to hold the Encryp and Cancel cuttons
        self.frameTop = Tkinter.Frame(self.frame)
        self.frameBottom = Tkinter.Frame(self.frame)
        
        #Buttons to select source and destination, and to encode or cancel
        self.buttonSelectSource = Tkinter.Button(self.frameTop,text="SOURCE",font=self.__fontButton)
        self.buttonSelectDestination = Tkinter.Button(self.frameTop,text="DESTINATION",font=self.__fontButton)
        self.buttonEncode = Tkinter.Button(self.frameBottom,text="ENCRYPT",font=self.__fontButton,
                                           state=Tkinter.DISABLED)
        self.buttonCancel = Tkinter.Button(self.frameBottom,text="CANCEL",font=self.__fontButton)
        
        #Labels to reflect the state of the source and destination
        self.labelSource = Tkinter.Label(self.frameTop,font=self.__fontSmall,text="...")
        self.labelDestination = Tkinter.Label(self.frameTop,font=self.__fontSmall,text="...")
        
        
    def init(self):
        ''' '''
        """ The main fram will hold another two frames, thus it is just 
        1 column, and 2 rows"""
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        self.frame.rowconfigure(1, weight=5)

        # Configure the top frame layout
        self.frameTop.rowconfigure(0,weight=1)
        self.frameTop.rowconfigure(1,weight=1)
        self.frameTop.rowconfigure(2,weight=1)

        
        # Configure the bottom frame layout
        self.frameBottom.columnconfigure(0,weight = 10)
        self.frameBottom.columnconfigure(1,weight = 1)
        self.frameBottom.rowconfigure(0,weight=10)
        self.frameBottom.rowconfigure(1,weight=1)
        
        self.buttonEncode.grid(column=0,row=1,sticky = Tkinter.E)
        self.buttonCancel.grid(column=1,row=1)
        
        
        #Add elements to the top frame
        Tkinter.Label(self.frameTop,text="ENCRYPT A FILE",font=self.fontTitle).grid(row=0,columnspan=4)
        self.buttonSelectSource.grid(column = 0,row=1,sticky = Tkinter.W)
        # SET THE COMMAND
        self.buttonSelectSource.config(command=self.setSource)
        self.labelSource.grid(column =1 ,row=1,sticky = Tkinter.W)
        self.buttonSelectDestination.grid(column = 0,row=2,sticky = Tkinter.W)
        # SET THE COMMAND
        self.buttonSelectDestination.config(command=self.setDestination)
        self.labelDestination.grid(column = 1,row=2,sticky = Tkinter.W)
        
        self.buttonEncode.config(command=self.getPassword)
        self.buttonCancel.config(command=self.controller.goToMainWindow)

        self.frameTop.grid(column=0,row=0, sticky=Tkinter.NSEW)
        self.frameBottom.grid(column=0,row=1, sticky=Tkinter.NSEW)
    
    def setSource(self):
        name = tkFileDialog.askopenfilename()
        if len(name) > 0:
            self.controller.setSource(name)
            self.controller.setDestination(name[:name.rfind('/')])
            
    def setDestination(self):
        name = tkFileDialog.askdirectory()
        if len(name) > 0:
            self.controller.setDestination(name)
            
    def getPassword(self):
        res = PassWordDialog(self.frame)
        if len(res.result) > 0:
            self.controller.encrypt(res.result)
            self.controller.goToMainWindow()
            
    def chopText(self,text,size=20):
        if len(text) <= 20:
            return text
        else:
            return "".join(["../...",text[-size:]])
        
    def onModelChanged(self,model):
        """Model listener callback method, used to update gui elements"""
        if len(model.getSource())>0:
            self.labelSource.config(text = self.chopText(model.getSource(),40))
        else:
            self.labelSource.config(text = "...")
        if len(model.getDestination())>0:
            self.labelDestination.config(text = self.chopText(model.getDestination(),40))
        else:
            self.labelDestination.config(text="...")
        if model.getStatus() == ProcessModel.READY:
            self.buttonEncode.config(state=Tkinter.ACTIVE)
        else:
            self.buttonEncode.config(state=Tkinter.DISABLED)
            
            
            
    