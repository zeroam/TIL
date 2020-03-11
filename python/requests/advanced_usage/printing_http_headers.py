import requests
import http

http.client.HTTPConnection.debuglevel = 1

requests.get('https://www.google.com/')
