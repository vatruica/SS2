'''
Created on Sep 4, 2012

@author: art3
'''
import socket

#defining some variables for later use
HOST='127.0.0.1'
PORT=5432
#creating the socket
clientsoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting to our server
clientsoc.connect((HOST,PORT))
#sending a message
while True:
    DATA=raw_input("command me >>> ")
    clientsoc.send(DATA)
    #receiving the answer
    clientsoc.recv(100)
    #closing the socket
    #clientsoc.close()