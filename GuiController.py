'''
Created on 29/09/2010

@author: veryweb
'''
from MainWindow import MainWindow
import Tkinter
from EncodingWindow import EncodingWindow
import ProcessModel
import DecryptWindow

class GuiController(object):
    def __init__(self,controller):
        self.__mainWindow = None
        self.__encodingWindow = None
        self.__decryptWindow = None
        self.__root = None
        # Points to the currently displayed frame
        self.__currentFrame = None
        # The process model
        self.__processModel = None
        #The application controller
        self.__controller = controller
    
    def init(self,model):
        """ Creates the Tk root, and initializes the view with the MainWindow frame"""
        
        #Create the model
        self.__processModel = model
        
        #Initializes GUI
        self.__root = Tkinter.Tk()
        self.__root.wm_geometry("500x300")
        self.__root.columnconfigure(0,weight=1)
        self.__root.rowconfigure(0,weight=1)
        self.__root.title("ENCRYPTION/DECRYPTION TOOL")
        self.__changeFrame(self.__getMainWindow().frame)
        #Link model with listeners
        self.__processModel.addListener(self.__getEncodingWindow())
        self.__processModel.addListener(self.__getDecryptWindow())
        self.__root.mainloop()
        
    """SERIES OF COMMANDS CALLABLE FROM THE DIFFERENT GUI PARTS"""
        
    def goToEncodeWindow(self):
        print "GO TO ENCODE WINDOW"
        self.__changeFrame(self.__getEncodingWindow().frame)
        
    def goToDecodeWindow(self):
        print "GO TO DECODE WINDOW"
        self.__changeFrame(self.__getDecryptWindow().frame)
        
    def goToMainWindow(self):
        print "GO TO MAIN WINDOW"
        self.__changeFrame(self.__getMainWindow().frame)
        self.__processModel.reset()
        
    def setSource(self,text):
        self.__controller.setSource(text)
        
    def setDestination(self,text):
        self.__controller.setDestination(text)
        
    def encrypt(self,password):
        self.__controller.encrypt(password)

    def decrypt(self,password):
        self.__controller.decrypt(password)
        
    """ A bunch of methods for lazy initialization"""
    def __getMainWindow(self):
        """Returns the main windows controlled by this controller. 
        Implements lazy initialization"""
        if self.__mainWindow is None:
            self.__mainWindow = MainWindow(self.__root,self)
            self.__mainWindow.init()
        return self.__mainWindow
    
    def __getEncodingWindow(self):
        """Returns the main windows controlled by this controller. 
        Implements lazy initialization"""
        if self.__encodingWindow is None:
            self.__encodingWindow = EncodingWindow(self.__root,self)
            self.__encodingWindow.init()
        return self.__encodingWindow
    
    def __getDecryptWindow(self):
        """Returns the main windows controlled by this controller. 
        Implements lazy initialization"""
        if self.__decryptWindow is None:
            self.__decryptWindow = DecryptWindow.DescryptWindow(self.__root,self)
            self.__decryptWindow.init()
        return self.__decryptWindow
    
    def __changeFrame(self,newFrame):
        if not self.__currentFrame is None:
            self.__currentFrame.grid_remove()
        newFrame.grid(column = 0, row = 0, sticky=Tkinter.NSEW);
        self.__currentFrame = newFrame
