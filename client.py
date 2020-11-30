"""
CSE310 Networking Workshop - Example 1

This example will explore a client/server architecture using
Python sockets.  
"""

import socket

ip_address = input("Enter NBA Server IP Address: ")
request = input("Which stat do you want: ")

# Addresses are a two part tuple including ip/hostname and port
server_address = None

