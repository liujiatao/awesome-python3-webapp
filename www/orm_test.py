#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
import asyncio
import aiomysql

#sample from aiomysql documentation
async def test_example(loop):
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='', db='mysql',
                                  loop=loop)

    async with conn.cursor() as cur:
        await cur.execute("SELECT Host,User FROM user")
        print(cur.description)
        r = await cur.fetchall()
        print(r)
    conn.close()

#sample from self-learning
async def orm_test(loop):
	await orm.create_pool(loop=loop, user='www-data', password='Xiao_yu0922', db='awesome')

	from models import User
	u = User(name='Test2', email='test2@example.com', passwd='1234567890', image='about:blank')

	await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(orm_test(loop))
