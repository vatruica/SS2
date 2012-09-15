import Tkinter
from Tkinter import *
import client_side as cl

if __name__ == '__main__':
    #defining the frame
    win = Frame()
    win.pack( )
    
    #label
    Label(win, text="Send your command to the RS485").pack(side=TOP)
    
    #button widget
    Button(win, text="Quit", command=win.quit).pack(side=BOTTOM)
    
    #button widget
    Button(win, text="TURN ON", command=cl.send_on()).pack(side=BOTTOM)
    Button(win, text="TURN OFF", command=cl.send_off()).pack(side=BOTTOM)
    
    #entry widget
    e = Entry(win)
    e.pack(side=TOP)
    e.get() # get the inputed text
    
    #ending
    win.mainloop( ) 
