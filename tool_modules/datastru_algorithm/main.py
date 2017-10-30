#!/usr/bin/env python
# encoding: utf-8
'''
Created on Oct 23, 2017

@author: Jack
'''
from collections import Counter
from collections import OrderedDict
from collections import defaultdict
from collections import deque, ChainMap
from itertools import groupby
from operator import itemgetter
import heapq


def drop_first_last(grades):
    first, *middle, last = grades
    print(middle)


line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

rv = line.split(':')

record = ('ACME', 50, 123.45, (12, 18, 2012))

name, *_, (*_, year) = record


def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for li in lines:
        yield li, previous_lines
        previous_lines.append(li)
        test = previous_lines.popleft()
        print(test)


nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
d = defaultdict(list)

d['a'].append(1)
d['a'].append(2)
d['a'].append(1)
d['b'].append(4)

# d = defaultdict(set)
#
# d['a'].add(1)
# d['a'].add(2)
# d['a'].add(1)
# d['b'].add(4)

test = heapq.heapify(nums)


def ordered_dict():
    d = OrderedDict()
    d['foo'] = 1
    d['bar'] = 2
    d['spam'] = 3
    d['grok'] = 4
    for key in d:
        print(key, d[key])


prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75,
    'Jack': 10.75,
}


def _dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


0

a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
b = list(dedupe(a, key=lambda d: (d['x'], d['y'])))
record = '....................100 .......513.25 ..........'

SHARES = slice(20, 23)
PRICE = slice(31, 37)
cost = int(record[SHARES]) * float(record[PRICE])

a = slice(5, 1000, 2)

s = list(range(101))
sl = a.indices(len(s))


words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
word_counts = Counter(words)
top_three = word_counts.most_common(3)
morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']
# word_counts.update(morewords)
b = Counter(words)
a = Counter(morewords)
c = a - b

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

a = itemgetter('fname')
test = a({'fname': 'Brian', 'lname': 'Jones', 'uid': 1003})

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

rows_sorted = sorted(rows, key=itemgetter('date'))

rows_grouped = groupby(rows_sorted, key=itemgetter('date'))


nums = [1, 2]
s = sum(x * x for x in nums)

portfolio = [
    {'name': 'GOOG', 'shares': 50},
    {'name': 'YHOO', 'shares': 75},
    {'name': 'AOL', 'shares': 20},
    {'name': 'SCOX', 'shares': 65}
]

min_shares = min(portfolio, key=itemgetter('shares'))

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

c = ChainMap(a, b)
cc = c.new_child(m=dict(x=0))
cm = cc.parents
if __name__ == '__main__':
    pass
