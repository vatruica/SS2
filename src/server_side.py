'''
Created on Sep 4, 2012

@author: art3

http://docs.python.org/howto/sockets.html
http://www.devshed.com/c/a/Python/Sockets-in-Python/1/
'''

import socket
import time
import serial

HOST='127.0.0.1'
PORT=5432

SERIAL_PORT = '/dev/ttyUSB0'
BAUDRATE = 9600

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
    
def serial_connection(message):
    # opening serial port
    ser = serial.Serial(
    port=SERIAL_PORT,
    baudrate=BAUDRATE,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS
    )
    ser.open()
    # sending the MSG to the serial port
    ser.write(message + '\r')
    out = ''
    # let's wait one second before reading output (let's give device time to answer)
    time.sleep(1)
    print (ser.inWaiting())
    while ser.inWaiting() > 0:           
        out += ser.read(1)
    if out != '':
        print "answer: " + out
    #src_soc.send ("rs485 says: "+str(out)) 
    #closing the serial connection
    ser.close()
    return out

#creating a loop where we wait for connections
#it will display to the client its ip
#what hes writing and send a message back

while True:
    channel, details = src_soc.accept()
    print 'We have opened a connection with', details
    MSG = channel.recv ( 100 )
    if MSG == '':
        print details, ' is either disconnected, either sent a blank link'
        exit()
    else:
        print 'the client says: ', MSG
        #channel.send ("acknowledged, i received:"+str(MSG))     
        print "sending ",str(MSG)," to rs485."
        serial_connection(MSG)
        channel.send ("server has received: "+str(MSG)+"\n-forwarding command to rs485-\nrs485 says: "+str(serial_connection(MSG)))
        #closing the socket connection
        channel.close()


