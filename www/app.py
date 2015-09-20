#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import logging
import asyncio
# import os
# import json
# import time
# from datetime import datetime
from aiohttp import web
import orm

logging.basicConfig(level=logging.INFO)


@asyncio.coroutine
def init():
    yield from orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='root', db='awesome')
    app = web.Application(loop=loop)
    srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()
