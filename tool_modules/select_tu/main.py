'''
Created on Nov 24, 2017
'''
import select
import socket
import sys
import queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server_address = ('localhost', 10000)
print(sys.stderr, '%s, %s' % server_address)
server.bind(server_address)
server.listen(5)

inputs = [server]
outputs = []

message_queues = {}

if __name__ == '__main__':
    pass
