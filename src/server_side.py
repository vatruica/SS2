'''
Created on Sep 4, 2012

@author: art3

http://docs.python.org/howto/sockets.html
http://www.devshed.com/c/a/Python/Sockets-in-Python/1/
'''

import socket

HOST='192.168.1.106'
PORT=5432
#creating the socket (INET, STREAMing socket)
src_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a host, and a well-known port
# use -> socket.gethostname() <- instead of 127.0.0.1, to be visible
#reuse socket for no TIME_WAIT
src_soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

src_soc.bind((HOST,PORT)) 
#become a server socket
# queues 5 connection requests
src_soc.listen(5) 
#creating a loop where we wait for connections
#it will display to the client its ip
#what hes writing and send a message back
while True:
    channel, details = src_soc.accept()
    print 'We have opened a connection with', details
    INCOMING_MESSAGE = channel.recv ( 100 )
    print details,'---->', INCOMING_MESSAGE
    channel.send ("acknowledged, i received:")
    channel.send (INCOMING_MESSAGE)
    channel.close()


