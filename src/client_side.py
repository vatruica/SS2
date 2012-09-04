'''
Created on Sep 4, 2012

@author: art3
'''
import socket

#creating the socket
clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting to our server
clientsoc.connect(('127.0.0.1',5432))
#sending a message
clientsoc.send("heyy, this is client")
#receiving the answer
clientsoc.recv(100)
#closing the socket
clientsoc.close()