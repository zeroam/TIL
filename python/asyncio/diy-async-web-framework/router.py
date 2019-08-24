from .response import Response


class UrlDispatcher:
    def __init__(self):
        self._routes = {}

    async def _not_found(self, request):
        return Response(f'Not found {request.url} on this server', status=404)

    def add_route(self, method, path, handler):
        self._routes[(method, path)] = handler

    def resolve(self, request):
        key = (request.method, request.url.path)
        if key not in self._routes:
            return self._not_found
        return self._routes[key]
