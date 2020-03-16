"""
Network programs written in C use the data type struct sockaddr to represent
IP addresses as binary value (instead of the string addresses usually found in
Python programs)
"""
import binascii
import socket
import struct
import sys


for string_address in ['192.168.1.1', '127.0.0.1']:
    packed = socket.inet_aton(string_address)
    print('Original:', string_address)
    print('Packed  :', binascii.hexlify(packed))
    print('Unpacked:', socket.inet_ntoa(packed))
    print()
