import typing
import collections
import itertools

# usefull dict handeling shemes

# create a dict from two lists
my_list_1 = range(10)
my_list_2 = range(6)
my_keys = range(10)
print(my_list_1)
print(my_list_2)
print(my_keys)

# make sure key is the longest list.
d1 = dict(itertools.zip_longest(my_keys, my_list_2, fillvalue="-"))
# if both lists have same length
d2 = dict(zip(my_keys, my_list_1))
# fill dict with constant value for every keys
d3 = dict(zip(my_keys, itertools.repeat("-")))
print(d1)
print(d2)
print(d3)

l = [1, 2, 3, 4, 5, 6, 7]
n = range(8, 12)
reversed(l)

try:
    a = next(x for x in reversed(l) if x == 10)
except StopIteration:
    pass
