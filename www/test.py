#!/usr/bin/env python3   
# -*- coding: utf-8 -*-
import asyncio
import orm
from models import User


@asyncio.coroutine
def test():
    yield from orm.create_pool(loop=loop, host='192.168.56.101', port=3306,
                               user='www-data', password='www-data', db='awesome')

    u = User(name='Admin', email='admin@admin.com', passwd='1234567890', image='about:blank')

    yield from u.insert()

loop = asyncio.get_event_loop()
loop.run_until_complete(test())
loop.close()
