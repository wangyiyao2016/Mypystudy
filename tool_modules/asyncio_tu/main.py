#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jan 19, 2017

@author: Jack
@reference: https://segmentfault.com/a/1190000007851357
'''
import asyncio


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


@asyncio.coroutine
def factorial(name, number):
    f = 1
    for i in range(2, number + 1):
        print("1Task %s: Compute factorial(%s)..." % (name, i))
        yield from asyncio.sleep(2)
#         print("2Task %s: Compute factorial(%s)..." % (name, i))
        f *= i
    print("Task %s: factorial(%s) = %s" % (name, number, f))


@asyncio.coroutine
def test(x):
    print("1Task")
    yield from asyncio.sleep(2)
    print("2Task")
    return x


@asyncio.coroutine
def test2(x):
    print("test2")
    yield from asyncio.sleep(2)
    print("test222")
    return x

loop = asyncio.get_event_loop()
# tasks = [
#     asyncio.ensure_future(factorial("A", 2)),
#     asyncio.ensure_future(factorial("B", 3)),
#     asyncio.ensure_future(factorial("C", 4))]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


if __name__ == '__main__':
    tasks = [
        asyncio.ensure_future(factorial("A", 100)),
        asyncio.ensure_future(factorial("B", 101)),
        asyncio.ensure_future(factorial("C", 102))]
    tasks = [wget(host) for host in ['www.sina.com.cn',
                                     'www.sohu.com',
                                     'www.163.com']]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
