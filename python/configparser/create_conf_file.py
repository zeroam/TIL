import configparser

config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'

config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'
topsecret['FowardX11'] = 'yes'

config['DEFAULT']['ForwardX11'] = 'yes'

with open('conf.ini', 'w') as configfile:
    config.write(configfile)
