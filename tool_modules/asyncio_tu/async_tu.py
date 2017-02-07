#!/usr/bin/env python
# encoding: utf-8
'''
Created on Feb 8, 2017

@author: Jack
'''
import asyncio


@asyncio.coroutine
def test_old(content, delay):
    yield from asyncio.sleep(delay)
    print(content)


async def test(content, delay):
    await asyncio.sleep(delay)
    print(content)

loop = asyncio.get_event_loop()
tasks = [
        asyncio.tasks.Task(test("one", 1.5)),
        asyncio.ensure_future(test("two", 2)),
        asyncio.ensure_future(test_old("three", 3)),
        asyncio.ensure_future(test_old("four", 3.5)),
        ]
if __name__ == '__main__':
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
    pass
