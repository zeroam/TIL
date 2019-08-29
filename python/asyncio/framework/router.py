import re

from functools import partialmethod

from .response import Response
from .exception import HTTPNotFound, HTTPBadRequest


class UrlDispatcher:
    _param_regex = r'{(?P<param>\w+)}'

    def __init__(self):
        self._routes = {}

    async def _not_found(self, request):
        return Response(f'Could not find {request.url.raw_path}')

    async def _method_not_allowed(self, request):
        return Response(f'{request.method} not allowed for {request.url.raw_path}')

    def resolve(self, request):
        for (method, pattern), handler in self._routes.items():
            match = re.match(pattern, request.url.raw_path)

            if match is None:
                raise HTTPNotFound(reason=f'Could not find {request.url.raw_path}')

            if method != request.method:
                raise HTTPBadRequest(reason=f'{request.method} not allowed for {request.url.raw_path}')

            return match.groupdict(), handler

    def _format_pattern(self, path):
        if not re.search(self._param_regex, path):
            return path

        regex = r''
        last_pos = 0

        for match in re.finditer(self._param_regex, path):
            regex += path[last_pos: match.start()]
            param = match.group('param')
            regex += r'(?P<%s>\w+)' % param
            last_pos = match.end()

        return regex

    def add_route(self, method, path, handler):
        pattern = self._format_pattern(path)
        self._routes[(method, pattern)] = handler

    add_get = partialmethod(add_route, 'GET')

    add_post = partialmethod(add_route, 'POST')

    add_put = partialmethod(add_route, 'PUT')

    add_head = partialmethod(add_route, 'HEAD')

    add_options = partialmethod(add_route, 'OPTIONS')

