import socket
import select
import sys
import errno

header_length = 10
IP = "127.0.0.1"
PORT = 6667

my_username = input("Username: ")
# my_username = ""

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))
client_socket.setblocking(False)

username = my_username.encode("utf-8")
unsername_header = f"{len(username):<{header_length}}".encode("utf-8")
client_socket.send(unsername_header + username)

while True:
    #Sending recieving messages here
    # message = input(f"{my_username} > ")   ## Switch to this if you want to enter stuff
    message = ""                            ## Switch to this if you watn to be a bystander / reader
                                            ## DO NOT HAVE BOTH RUNNING comment one out.

    if message:
        message = message.encode("utf-8")
        message_header = f"{len(message) :<{header_length}}".encode("utf-8")
        client_socket.send(message_header + message)

    try:
        while True:
            #attempt to receive messages
            unsername_header = client_socket.recv(header_length)
            if not len(unsername_header):
                print("Connection closed by the server")
                sys.exit()

            username_length = int(unsername_header.decode("utf-8"))
            username = client_socket.recv(username_length).decode("utf-8")

            message_header = client_socket.recv(header_length)
            message_length = int(message_header.decode("utf-8"))
            message = client_socket.recv(message_length).decode("utf-8")

            print(f"{username} > {message}")


    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error',str(e))
            sys.exit()
        continue
