import socket

# do a "reverse" lookup for the name
hostname, aliases, addresses = socket.gethostbyaddr('172.217.26.14')

print('Hostname :', hostname)
print('Aliases  :', aliases)
print('Addresses:', addresses)
