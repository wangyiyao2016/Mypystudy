#!/usr/bin/env python
# encoding: utf-8
'''
Created on Sep 4, 2017

@author: Jack
'''
from pykafka import KafkaClient


client = KafkaClient(hosts="test:9092")

kafka_topics = client.topics

try:
    test_topic = client.topics[b'test']
except Exception as e:
    print(e)


def main():
    print(kafka_topics)


def producer():
    with test_topic.get_sync_producer() as producer:
        for i in range(4):
            print(b'test message %d' % i ** 2)
            producer.produce(b'test message %d' % i ** 2)


def comsumer():
    consumer = test_topic.get_simple_consumer()
    for message in consumer:
        if message is not None:
            print(message.offset, message.value)


if __name__ == '__main__':
    comsumer()
    pass
