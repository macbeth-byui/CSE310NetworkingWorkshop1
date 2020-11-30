"""
CSE310 Networking Workshop - Example 1

This example will explore a client/server architecture using
Python sockets.  
"""

import socketserver
import socket
import pandas  # pip install pandas

# Load up the NBA data so we can respond to client requests

nba_data = pandas.read_csv("basketball_players.csv", low_memory=False)

class NBA_Stat_Server(socketserver.BaseRequestHandler):
    """
    This class provides a handler function for our server.
    """

    def handle(self):
        # Obtain the source ip address and port form the self.client_address.
        # The self.client_address is inherited form socketserver.BaseRequestHandler
        source_ip_address = None
        source_port = None

        # Convert the bytes to a string using UTF-8 encoding
        source_msg = None
        print("[{}:{}] => {}".format(source_ip_address, source_port, source_msg))

        # Process the request and provide a value of -1 if there is any
        # error (e.g. invalid stat column provided by client)

        result = ""

        # To send a response, we will need the server socket which is available
        # in self.request[1].  We also need the client address which is available
        # in self.client_address
        sock = None
        

        print("[{}:{}] <= {}".format(source_ip_address, source_port, result))
        

# Get the ip address of the server
host_name = None
ip_address = None
server_address = None
print("Starting Server: [{}:{}]".format(server_address[0], server_address[1]))

# Create the UDP server and run forever

