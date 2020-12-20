import socket
import threading
import randfacts
import os
import random
from ircBotStuff import *
import os
import random
from datetime import datetime

p_host = '127.0.0.1'
p_port = 6667

## IRCBot Config
channel = "#python"
botnick = "TheZucc"
botnickpass = "zucc"
botpass = "<%= @zucc_password %>"
irc = botIRC() # calling bot irc class
irc.connect(p_host, p_port, channel, botnick, botpass, botnickpass)

while True:
    text = irc.get_response()
    print(text)
 
    if "PRIVMSG" in text and channel in text:
        x = randfacts.getFact()
        irc.send(channel, x)

    if "!slap" in text and channel in text:
        irc.send(channel, "You have been slapped!")
    
    if "!hello" in text and channel in text:
        irc.send(channel, "Hello! It is :"+ datetime.now() )


