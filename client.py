import time
from socket import *

##############################################################
# cmpe 472 homework-2
# Client code
# Abdusselam koc -
# Enes Yardim    - 
# Bahadir Unal   - 
################################################################


# initial values to set up client side.
# Set the server IP address and port number
serverName = 'localhost'
serverPort = 12000

# Create a UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Set timeout value of one second
clientSocket.settimeout(1)


def call_server(index):
    # Get the current time
    sendTime = time.time()
    # Create the message to send to the server
    message = f'Ping {index} sent time: {sendTime}'

    try:
        # Send the message to the server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        # Receive the response from the server
        modifiedMessage, serverAddress = clientSocket.recvfrom(1024)

        # Get the current time
        receiveTime = time.time()

        # Calculate the round trip time
        rtt = receiveTime - sendTime

        # Print the response message and received time and  round trip time
        print(f'{modifiedMessage.decode()}  Received Time:{receiveTime} RTT: {rtt} seconds')

    except timeout:
        # Print "Request timed out" if no response is received within one second
        print(f'Ping {index} Request timed out')


# Send 10 pings to the server
for i in range(1, 11):
    call_server(i)

# Close the socket
clientSocket.close()
