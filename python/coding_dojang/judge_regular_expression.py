import re

p = re.compile('^(http(s)?://)?[\w\-]+\.[\w\-]+[\w\-_.?=/&#:]+$')

urls = [
    'https://www.example.com',
    'http://www.example.com',
    'www.example.com',
    'example.com',
    'http://blog.example.com',
    'http://www.example.com/product',
    'http://www.example.com/products?id=1&page=2',
    'http://www.example.com#up',
    'http://255.255.255.255',
    '255.255.255.255',
    'http://invalid.com/perl.cgi?key= | http://web-site.com/cgi-bin/perl.cgi?key1=value1&key2',
    'http://www.site.com:8008'
    ]

for url in urls:
    print(p.match(url) != None, end=' ')
    print(p.match(url))
    
