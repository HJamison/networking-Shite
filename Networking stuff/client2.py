import socket
import threading

p_host = '127.0.0.1'
p_port = 6667

nickname = "The_ZUCC"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((p_host,p_port))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

#Replying with fact JUST HELLO ATM
while True:
    text = client.get_response()
    print text
    if "PRIVATE" in text and channel in text and "hello" in text:
        irc.send(channel, "Hello!")

# Sending Messages To Server
def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
