### 웹 서버용 파이썬 라이브러리 주요 클래스

- HTTPServer
  - 웹 서버를 만들기 위한 클래스로, 서버 IP와 PORT를 바인딩함
  - HTTPServer 객체 생성 시, 핸들러 클래스가 반드시 필요함
- BaseHTTPRequestHandler
  - 핸들러를 만들기 위한 기반 클래스로, HTTP 프로토콜 처리 로직이 들어있음
  - 이 클래스를 상속받아, 자신의 로직 처리를 담당하는 핸들러 클래스를 만듬
- SimpleHTTPRequestHandler
  - BaseHTTPRequestHandler 클래스를 상속받아 만든 클래스
  - GET 과 HEAD 메소드 처리가 가능한 핸들러 클래스
- CGIHTTPRequestHandler
  - SimpleHTTPRequestHandler 클래스를 상속받아 만든 클래스
  - 추가적으로 POST 메소드와 CGI 처리가 가능한 핸들러 클래스



### WSGI/CGI

- WSGI(Web server Gateway Interface)
  - 웹 서버와 웹 애플리케이션을 연결하는 규격으로, 장고(Django)와 같은 파이썬 웹 프레임워크를 개발하거나, 이런 웹 프레임워크를 아파치(Apache)와 같은 웹 서버와 연동할 때 사용
  - 파이썬의 WSGI 규격은 전통적인 웹 CGI 기술의 단점을 개선하고 파이썬 언어에 맞게 재구성 한 것

- CGI(Common Gateway Interface)
  - 웹 서버가 사용자의 요청을 애플리케이션에 전달하고 애플리케이션의 처리 결과를 애플리케이션으로부터 돌려받기 위한, 즉 웹 서버와 애플리케이션 간에 데이터를 주고받기 위한 규격
  - 파이썬의 경우 WSGI 기술을 사용하여 CGI 처리를 하므로 cgi 모듈을 사용할 일은 많지 않음

