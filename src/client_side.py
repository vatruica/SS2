'''
Created on Sep 4, 2012

@author: art3
'''
import socket

#defining some variables for later use
HOST='127.0.0.1'
PORT=5432

class client():
    
    HOST='127.0.0.1'
    PORT=5432
    
    def send_on(self):
        #creating the socket
        cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cl_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #connecting to our server
        cl_soc.connect((HOST,PORT)) 
        MSG = '#020002'
        cl_soc.send(str(MSG))
        #receiving the answer
        print( cl_soc.recv(100) )
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
        print( cl_soc.recv(100) )
        cl_soc.close()
    
    def send_input(self):
        while True: 
            #creating the socket
            cl_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            cl_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            #connecting to our server
            cl_soc.connect((HOST,PORT))   
            #sending a message
            MSG = raw_input("write here:")
            if MSG != 'exit':
        
                cl_soc.send(str(MSG))
                #receiving the answer
                print( cl_soc.recv(100) )
                #closing the socket
                #cl_soc.close()
            else:
                cl_soc.close()
                exit()



 
