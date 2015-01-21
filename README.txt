DirectX Game controller Server/Client

This is a quick project done in the summer of 2014 to play directX games remotely from a diffrent keyboard.

I created this project as a way to play Tales of Monkey island on a TV by sending commands from a diffrent keyboard
(i.e: one embedded in another laptop). I did this because at the time we did not have a wireless keyboard to attach
to the laptop by the TV. 

To use: start the server on the computer intended to run the game, then start the game. Ensure it is in the foreground.
On the other computer start the client, make sure the ip address in the python file matches the server's ip shown in the
console window.

You will have to edit the ip adress in the client script and run it through python.

Requires Python 2.7

Also included setup utils to create a python exe for the client.

Kiril Tzvetanov Goguev