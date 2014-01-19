'''
Created on 03/10/2010

@author: veryweb
'''
import tkSimpleDialog
from Tkinter import Label,Entry

class PassWordDialog(tkSimpleDialog.Dialog):
    
    def __init__(self,parent):
        tkSimpleDialog.Dialog.__init__(self, parent, "PASSWORD")

    def body(self, master):

        Label(master, text="Password:").grid(row=0)
        Label(master, text="Confirm Password:").grid(row=1)

        self.e1 = Entry(master,show="*")
        self.e2 = Entry(master,show="*")

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = self.e1.get()
        second = self.e2.get()
        if first == second and first != "":
            self.result = first
        else:
            self.result = ""    
