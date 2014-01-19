'''
Created on 03/10/2010

@author: veryweb
'''
from EncodingWindow import EncodingWindow
from PasswordDialog import PassWordDialog
import Tkinter

class DescryptWindow(EncodingWindow):
    def __init__(self,parent,controller):
        EncodingWindow.__init__(self,parent,controller)
    
    def init(self):
        EncodingWindow.init(self)
        self.buttonEncode.config(text="DECRYPT")
        Tkinter.Label(self.frameTop,text="DECRYPT A FILE",font=self.fontTitle).grid(row=0,columnspan=4)
        
    def getPassword(self):
        res = PassWordDialog(self.frame)
        if len(res.result) > 0:
            self.controller.decrypt(res.result)
            self.controller.goToMainWindow()