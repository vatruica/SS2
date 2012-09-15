import Tkinter
from Tkinter import *
import client_side as CS
import socket

import Tkinter as tk

HOST='127.0.0.1'
PORT=5432

class guiclass():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        self.other = tk.Toplevel()
        self.other.title("Victors Window")
        self.otherlabel = tk.Label(self.other, text='SEND COMMAND TO RS485', relief = tk.RIDGE)
        self.otherlabel.pack(side=tk.TOP, fill = tk.BOTH, expand = tk.YES)
        self.otherbutton = tk.Button(self.other, text='TURN ON', command=self.send_on).pack(side=tk.TOP)
        self.otherbutton = tk.Button(self.other, text='TURN OFF', command=self.send_off).pack(side=tk.TOP)
        self.otherbutton = tk.Button(self.other, text='SEND', command=self.send_input).pack(side=tk.TOP)
        self.otherbutton = tk.Button(self.other, text='QUIT', command=self.other.quit).pack(side=tk.BOTTOM)
        self.outputvalue = tk.StringVar()
        self.otherlabel1 = tk.Label(self.other, textvariable =self.outputvalue).pack(side=tk.BOTTOM)
        
        self.e = tk.Entry(self.other)
        self.e.pack(side=tk.TOP) 

    def send_on(self):
        #creating the socket
        cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #connecting to our server
        cl_soc.connect((HOST,PORT)) 
        MSG = '#020002'
        cl_soc.send(str(MSG))
        #receiving the answer
        #print( cl_soc.recv(100) )
        self.outputvalue.set(str(cl_soc.recv(100)))
        cl_soc.close()
        
    def send_off(self):
        #creating the socket
        cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #connecting to our server
        cl_soc.connect((HOST,PORT)) 
        MSG = '#020000'
        cl_soc.send(str(MSG))
        #receiving the answer
        self.outputvalue.set(str(cl_soc.recv(100)))
        cl_soc.close()
    
    def send_input(self):       
        #creating the socket
        cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        cl_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #connecting to our server
        cl_soc.connect((HOST,PORT))   
        #sending a message
        #MSG = raw_input("write here:")
        if self.e.get() != 'exit':
            cl_soc.send(self.e.get())
            #receiving the answer
            #print( cl_soc.recv(100) )
            self.outputvalue.set(str(cl_soc.recv(100)))
            #closing the socket
            cl_soc.close()
        else:
            cl_soc.close()
            exit()

        
if __name__ == '__main__':
    
    win = tk.Frame()
    win.pack()
    
    
    guiclass()
    
    win.mainloop( )
