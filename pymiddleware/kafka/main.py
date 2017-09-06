#!/usr/bin/env python
# encoding: utf-8
'''
Created on Sep 4, 2017

@author: Jack
@TODO: create topics with pykafka
'''
import queue

from pykafka import KafkaClient
# from pykafka.cluster import Cluster
# from pykafka.protocol import TopicMetadata
#
# new_topic = TopicMetadata('test_topic', )

# client = KafkaClient(hosts="TEST:9092")
client = KafkaClient(zookeeper_hosts="TEST:2181")

try:
    test_topic = client.topics[b'test']
except Exception as e:
    print(e)


def get_topics():
    kafka_topics = client.topics
    print(kafka_topics)


def main():
    pass


def producer():
    #     with test_topic.get_sync_producer() as producer:
    #         for i in range(4):
    #             print(b'test message %d' % i ** 2)
    #             producer.produce(b'test message %d' % i ** 2)
    with test_topic.get_producer(delivery_reports=True) as producer:
        count = 0
        while True:
            count += 1
            producer.produce(
                b'test msg', partition_key=(
                    '{}'.format(count)).encode())
            if count % 10 ** 5 == 0:  # adjust this or bring lots of RAM ;)
                while True:
                    try:
                        msg, exc = producer.get_delivery_report(block=False)
                        if exc is not None:
                            print('Failed to deliver msg {}: {}'.format(
                                msg.partition_key, repr(exc)))
                        else:
                            print('Successfully delivered msg {}'.format(
                                msg.partition_key))
                    except queue.Empty:
                        print("break")
                        break
#                 except Queue.Empty:
#                     break


def comsumer():
    #     consumer = test_topic.get_simple_consumer()
    #     for message in consumer:
    #         if message is not None:
    #             print(
    #                 message.offset,
    #                 message.value,
    #                 message.partition_key)
    #             print(message.partition_id)

    balanced_consumer = test_topic.get_balanced_consumer(
        consumer_group=b'testgroup',
        #         auto_commit_enable=True
    )
    for message in balanced_consumer:
        if message is not None:
            print(
                message.offset,
                message.value,
                message.partition_key)
            print(message.partition_id)


if __name__ == '__main__':
    comsumer()
    pass
