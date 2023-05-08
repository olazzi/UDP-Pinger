##############################################################
# cmpe 472 homework-2
# Server code
# Abdusselam koç - 
# Enes Yardım    - 
# Bahadır Ünal   - 
################################################################



# We will need the following module to generate randomized lost packets
import random
from socket import *
import time

# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind(('', 12000))

#show that server is ready nad running
print("Hello, your UDP server is ready.")
while True:
    # Generate random number in the range of 0 to 10
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client
    message = message.upper()

    # Simulate some delay in the server's response
    time.sleep(0.1)

    # If rand is less is than 4, we consider the packet lost and do not respond
    if rand < 4:
        continue
    # Otherwise, the server responds
    serverSocket.sendto(message, address)