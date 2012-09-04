'''
Created on Sep 4, 2012

@author: art3

http://docs.python.org/howto/sockets.html
http://www.devshed.com/c/a/Python/Sockets-in-Python/1/
'''

import socket

#creating the socket (INET, STREAMing socket)
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to a host, and a well-known port
# use -> socket.gethostname() <- instead of 127.0.0.1, to be visible
soc.bind(('127.0.0.1',5432)) 
#become a server socket
# queues 5 connection requests
soc.listen(5) 

#creating a loop where we wait for connections
#it will display to the client its ip
#what hes writing and send a message back
while True:
   channel, details = soc.accept()
   print 'We have opened a connection with', details
   print channel.recv ( 100 )
   channel.send ( 'Green-eyed monster.' )
   channel.close()

