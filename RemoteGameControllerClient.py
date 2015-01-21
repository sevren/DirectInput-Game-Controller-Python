# Python Direct X game controller client
# DirectX works with Scancodes for Direct Input
# Sends keys to UDP server running a DirectX game in the foreground
# Quick project test for playing a game running on a laptop connected to a TV with a keyboard from another computer through the Network.
#Tested on Fallout 3, Tales of Monkey Island

# TODO: Create a UDP broadcast function for auto discovery of clients
# TODO: Try to fix some of the lag, currently holding down the keys for long periods of time creates problems.
# TODO: Simulate Mouse movements from a mouse through networking.


import socket,sys
import msvcrt
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#TODO Change the hard coded addr to a function that will find the server
server_address =('192.168.2.4',3056)
#sock.connect(server_address)


print 'type anything on the keyboard:\n'
while True:
    pressedKey = msvcrt.getch()
    if pressedKey == 'x':    
       sys.exit()
    else:
       print "Key Pressed:" + str(pressedKey) 
       print ord(pressedKey)
    sock.sendto(str(ord(pressedKey)),server_address)