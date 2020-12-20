import socket
import sys
import time
#https://www.techbeamers.com/create-python-irc-bot/
class botIRC:
 
    ircBot = socket.socket()
  
    def __init__(self):
        # Define the socket
        self.ircBot = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
    def send(self, channel, msg):
        # Transfer data
        self.ircBot.send(bytes("PRIVMSG " + channel + " " + msg + "\n", "UTF-8"))
 
    def connect(self, server, port, channel, botnick, botpass, botnickpass):
        # Connect to the server
        print("Connecting to: " + server)
        self.ircBot.connect((server, port))

        # Perform user authentication
        self.ircBot.send(bytes("USER " + botnick + " " + botnick +" " + botnick + " :python\n", "UTF-8"))
        self.ircBot.send(bytes("NICK " + botnick + "\n", "UTF-8"))
        self.ircBot.send(bytes("NICKSERV IDENTIFY " + botnickpass + " " + botpass + "\n", "UTF-8"))
        time.sleep(5)

        # join the channel
        self.ircBot.send(bytes("JOIN " + channel + "\n", "UTF-8"))
 
    def get_response(self):
        time.sleep(1)
        # Get the response
        resp = self.ircBot.recv(2040).decode("UTF-8")
 
        if resp.find('PING') != -1:                      
            self.ircBot.send(bytes('PONG ' + resp.split().decode("UTF-8") [1] + '\r\n', "UTF-8")) 
 
        return resp