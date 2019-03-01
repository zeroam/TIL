from wsgiref.simple_server import make_server

def application(envrion, start_response):
    response_body = [
        '{key}: {value}'.format(key=key, value=value) for key, value in sorted(envrion.items())
    ]
    response_body = '\n'.join(response_body)

    status = '200'

    response_headers = [
        ('Content-type', 'text/plain'),
    ]

    return [response_body.encode('utf-8')]

server = make_server('localhost', 8000, app=application)
server.serve_forever()