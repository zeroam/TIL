import asyncio

from httptools import HttpRequestParser

from .http_parser import HttpParserMixin
from .request import Request
from .response import Response


class Server(asyncio.Protocol, HttpParserMixin):
    def __init__(self, loop, handler, app):
        self._loop = loop
        self._encoding = 'utf-8'
        self._url = None
        self._headers = {}
        self._body = None
        self._transport = None
        self._request_parser = HttpRequestParser(self)
        self._request = None
        self._request_class = Request
        self._request_handler = handler
        self._request_handler_task = None
        self._app = app

    def response_writer(self, response):
        self._transport.write(str(response).encode(self._encoding))
        self._transport.close()

    def connection_made(self, transport):
        self._transport = transport

    def connection_lost(self, *args):
        self._transport = None

    def data_received(self, data):
        # Pass data to our parser
        self._request_parser.feed_data(data)

        self._request_handler(self._request, self.response_writer)
        # resp = Response(body=f'Received request on {self._request.url}')
        # self._transport.write(str(resp).encode(self._encoding))
        # self._transport.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    serv = Server(loop)
    server = loop.run_until_complete(loop.create_server(lambda: serv, port=8080))

    try:
        print('Started server on ::8080')
        loop.run_until_complete(server.serve_forever())
    except KeyboardInterrupt:
        print('Stopping server gracefully...')
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.stop()
