import asyncio

from .router import UrlDispatcher
from .server import Server
from .response import Response


class Application:
    def __init__(self, loop=None):
        if loop is None:
            loop = asyncio.get_event_loop()

        self._loop = loop
        self._router = UrlDispatcher()

    @property
    def loop(self):
        return self._loop

    @property
    def router(self):
        return self._router

    def _make_server(self):
        return Server(loop=self._loop, handler=self._handler, app=self)

    async def _handler(self, request, response_writer):
        """ Process incoming request """
        handler = self._router.resolve(request)
        resp = await handler(request)

        if not isinstance(resp, Response):
            raise RuntimeError(f'except Response instance but got {type(resp)}')

        response_writer(resp)


def run_app(app, host='127.0.0.1', port=8080, loop=None):
    if loop is None:
        loop = asyncio.get_event_loop()

    serv = app._make_server()
    server = loop.run_until_complete(
        loop.create_server(lambda: serv, host=host, port=port)
    )

    try:
        print(f'Started server on {host}:{port}')
        loop.run_until_complete(server.serve_forever())
    except KeyboardInterrupt:
        print('Stopping server...')
        server.close()
        loop.run_until_complete(server.wait_closed())
        loop.stop()