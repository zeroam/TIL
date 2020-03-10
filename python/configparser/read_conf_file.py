import configparser

config = configparser.ConfigParser()
# empty sections
print(config.sections())

config.read('conf.ini')
# ['bitbucket.org', 'topsecret.server.com']
print(config.sections())

print('bitbucket.org' in config)    # True
print('bytebong.com' in config)     # False

topsecret = config['topsecret.server.com']
print(topsecret['ForwardX11'])      # yes
print(topsecret['Port'])            # 50022

for key in config['bitbucket.org']:
    print(key)

print(config['bitbucket.org']['ForwardX11'])


# get value
print(config.get('bitbucket.org', 'user'))
print(config.get('bitbucket.org', 'no-user', fallback='no-user not exist'))