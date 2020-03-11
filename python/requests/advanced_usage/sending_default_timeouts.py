import requests

from transport_adapter import TimeoutHTTPAdapter


http = requests.Session()

# Mount it for both http and https usage
adapter = TimeoutHTTPAdapter(timeout=2.5)
http.mount('https://', adapter)
http.mount('http://', adapter)

# Use the default 2.5s timeout
response = http.get('https://api.twilio.com/')
print(response)

# Override the timeout as usual for specific requests
response = http.get('https://api.twilio.com/', timeout=10)
print(response)
