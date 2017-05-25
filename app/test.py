import asyncio
import random

import sys

from models import User, Marker
from orm import select, create_pool, execute


async def test(loop):
    await create_pool(loop=loop, host='127.0.0.1', user='root', password='1234', db='appdemo')
    for i in range(1, 100):
        lat = random.uniform(90, 100)
        lng = random.uniform(100, 110)
        m = Marker(lat=lat, lng=lng, show_name='Test' + str(i), item_id='11111')
        await m.save()
        # print(u)


loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
    sys.exit(0)
