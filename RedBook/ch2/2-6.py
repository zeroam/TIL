import urllib.request

url = 'http://www.example.com'
proxyServer = 'http://www.proxy.com:3128'

# 프록시 서버를 통해 웹 서버로 요청을 보냅니다.
proxy_handler = urllib.request.ProxyHandler({'http': proxyServer})

# 프록시 서버 설정을 무시하고 웹 서버로 요청을 보냅니다.
#proxy_handler = urllib.request.ProxyHandler({})

# 프록시 서버에 대한 인증을 처리합니다.
proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm', 'host', 'username', 'password')

# 2개의 핸들러를 오프너에 등록합니다.
opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)

# 디폴트 오프너로 지정하면, urlopen() 함수로 요청을 보낼 수 있습니다.
urllib.request.install_opener(opener)

# opener.open() 대신에 urlopen()을 사용했습니다.
f = urllib.request.urlopen(url)

print("geturl():", f.geturl())
print(f.read(300).decode('utf-8'))