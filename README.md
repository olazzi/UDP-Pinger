# UDP-Pinger
We are asked to implement a ping client using the User Datagram Protocol (UDP). The
client sends ten pings to a server with a specified IP address and port number (12000) and
measures the round-trip time (RTT) for each ping. Our client uses the socket module to create a
UDP socket. After that, it sets a timeout value of one second. It then enters a loop that sends a
ping message to the server. And receives a response message. Lastly, it calculates the RTT. If
a response is not received within one second, the client prints a "Request timed out" message.
After sending ten pings, the client closes the socket. The client calculates the RTT as the
difference between the receive time and the send time.
