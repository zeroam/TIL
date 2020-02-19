import requests

data = {'area': 3300}
response = requests.post('{}/'.format('http://127.0.0.1:5000'), json=data)
print('Print of the house should be ' + str(response.json()))