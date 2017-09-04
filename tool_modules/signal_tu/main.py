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
    print("alarm_received called")
    return


def test():
    signal.signal(signal.SIGALRM, alarm_received)
    signals_to_names = dict(
        (getattr(signal, n), n) for n in dir(signal)
        if n.startswith('SIG') and '_' not in n
    )
    for s, name in sorted(signals_to_names.items()):
        handler = signal.getsignal(s)
        if handler is signal.SIG_DFL:
            handler = 'SIG_DFL'
        elif handler is signal.SIG_IGN:
            handler = 'SIG_IGN'
        else:
            print()
        print('%-10s (%2d): ' % (name, s), handler)


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
    test()
    # main()
    pass
