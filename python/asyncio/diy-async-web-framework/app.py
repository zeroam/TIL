import asyncio

from .response import Response
from .application import Application, run_app

app = Application()


async def handler(request):
    return Response(f'Hello at {request.url}')

app.router.add_route('GET', '/', handler)

if __name__ == '__main__':
    run_app(app)