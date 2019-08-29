import asyncio

from framework.response import Response
from framework.application import Application, run_app
from framework.exception import HTTPNotFound


async def on_startup(app):
    # you may query here actual db, but for example let's just use simple set.
    app.db = {'john_doe', }


async def log_middleware(request, handler):
    print(f'Received request to {request.url.raw_path}')
    return await handler(request)


async def handler(request):
    username = request.match_info['username']
    if username not in request.app.db:
        raise HTTPNotFound(reason=f'No such user with as {username} :(')

    return Response(f'Welcome, {username}')


app = Application(middlewares=[log_middleware])

app.on_startup.append(on_startup)

app.router.add_route('GET', '/{username}', handler)

if __name__ == '__main__':
    run_app(app)
