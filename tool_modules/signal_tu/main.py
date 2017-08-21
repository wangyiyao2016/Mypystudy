#!/usr/bin/env python
# encoding: utf-8
'''
Created on Aug 17, 2017

@author: Jack
'''
import os
import signal
import time

PID = os.getpid()


def alarm_received(n, stack):
    return


def test():
    signal.signal(signal.SIGALRM, alarm_received)
    signals_to_names = dict(
        (getattr(signal, n), n) for n in dir(signal)
        if n.startswith('SIG') and '_' not in n
    )
    for s, name in sorted(signals_to_names.items()):
        handler = signal.getsignal(s)


def receive_signal(signum, stack):
    print("received:", signum)


def handler(signum, frame):
    print('Signal handler called with signal', signum)
    raise OSError("Couldn't open device!")


def main():
    while True:
        print("Waiting>>>>>>>")
        time.sleep(10)


if __name__ == '__main__':
    print(PID)
    main()
    pass
