import socket

# convert a partial name to a fully qualified domain name
for host in ['google.com', 'pymotw.com']:
    print('{:>10} : {}'.format(host, socket.getfqdn(host)))
