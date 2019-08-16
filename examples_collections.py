#!/usr/bin/env python3
"""
Create some real world examples using collections
"""

from collections import Counter
from collections import defaultdict
from collections import OrderedDict


# first create some basic examples
some_list = [1, 2, 1, 4, 1, 2, 5, 1, 1, 3, 2, 8, 2, 3, 4, 5, 6]
cnt = Counter(some_list)
print(cnt)

# sort the list according to number
print(cnt.most_common())

# subtract some items
deduct = [1, 2, 1, 1, 2]
cnt.subtract(deduct)
print(cnt)

# defaultdic: useful when creating a dictionary without knowing in advance
# how many keys you will need - keys created automatically when missing
nums = defaultdict(int)
nums['one'] = 1
nums['two'] = 2
print(nums['three'])
print(nums)

count = defaultdict(int)
names_list = "Mike John Mike Sarah Alex Dino John Elvis Okja Mike".split()
for n in names_list:
    count[n] += 1
print(count)

# ordereddict
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
print(od)

for key, value in od.items():
    print(key, value)


# most frequently occurring letter will be first key and least occurring
# letter will be the last key
# TODO: understand why this prints out two lists
od_list = ["a", "b", "a", "a", "b", "c"]
od_count = Counter(od_list)
od_dict = OrderedDict(od_count.most_common())
for k, v in od_dict.items():
    print(k, v)

text_list = "some list of words to be used for an example of defaultdict"
word_count = defaultdict(int)
for w in text_list.split(' '):
    word_count[w] += 1



