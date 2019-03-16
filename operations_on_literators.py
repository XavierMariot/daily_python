import typing
import operator
import random
import collections
import itertools

# create a dict from two lists
my_list_1 = range(10)
my_list_2 = range(6)
my_keys = range(10)
# create dict based on shortest list.
# note: most of the time make sure key is the longest list.
d1 = dict(zip(my_keys, my_list_1))
# fill dict with constant value for every keys
d2 = dict(zip(my_keys, itertools.repeat("-")))
# create dict based on longest key list, with default value to fill in missing ones.
d3 = dict(itertools.zip_longest(my_keys, my_list_2, fillvalue="-"))
print(d1)
print(d2)
print(d3)

# count items
c: collections.Counter = collections.Counter()
c["hero"] += 1
print(c)

# find first in iterator.
my_iterator = [1, 2, 3, 4, 5, 6, 7]  # here a list
my_condition = lambda x_: x_ == 10
my_condition_1 = lambda x_: x_ ** 2 == 16


a = None
b = None
a_bis = None
b_bis = None

try:
    a = next(x for x in my_iterator if my_condition_1(x))
    b = next(x for x in my_iterator if my_condition(x))
except StopIteration:  # raised if end of iterator reached without a match
    pass
if a:
    print(f"a == {a}")
if b:
    print(f"b == {b}")

try:
    a_bis = next(filter(my_condition_1, my_iterator))
    b_bis = next(filter(my_condition, my_iterator))
except StopIteration:  # raised if end of iterator reached without a match
    pass
if a_bis:
    print(f"a == {a}")
if b_bis:
    print(f"b == {b}")

# find first index of an item in a list
my_mapped_list = list(map(str, my_iterator))
print(my_mapped_list)
result_index = my_mapped_list.index("1")
print(result_index)

# slicing operations
s = list(range(10))
print(s[2:5])  # extract from index 2 to 5 included
print(s[0 : len(s) : 2])  # extract every even index from index 0 to end of sequence


def f(any_dict: dict):
    return any_dict.keys()


# use a generator to minimize computations.
d = {"a": 0, "b": 1, "c": 2}
infinite_key_generator = map(f, itertools.repeat(d))
c = next(infinite_key_generator)
print(c)

# apply a function on multiple elements of a list with a 2nd constant argument
def make_a_string(x: int, my_constant_arg: str) -> str:
    return f"{x}__{my_constant_arg}"


my_numbers = range(10)
my_cst = "carrots"

my_string_generator = map(make_a_string, my_numbers, itertools.repeat(my_cst))
my_list_of_str = list(my_string_generator)
print(my_list_of_str)


# same with iterable used as argument (here tuples)
my_args = list(zip(my_numbers, itertools.repeat(my_cst)))
print(my_args)
my_string_generator_star = itertools.starmap(make_a_string, my_args)
my_list_of_str_star = list(my_string_generator_star)
print(my_list_of_str_star)

# checking condition on all elements of a list
def even(number: int):
    return number % 2 == 0


def odd(number: int):
    return number % 2 == 1


even_list = range(0, 10, 2)
odd_list = range(1, 10, 2)
l = range(10)


# combing all/any with map for efficient testing
print(all(map(even, even_list)))
print(all(map(odd, odd_list)))
print(all(map(even, l)))
print(any(map(even, l)))
print(any(map(even, l)))


# sort items in a list
random_list = list(range(10))
random_list = random_list * 2
random.shuffle(random_list)
print(random_list)


class HomeMadeSort:
    def __init__(self, number_):
        self.number = number_

    def __lt__(self, b: "HomeMadeSort"):
        return self.number > b.number

    def __le__(self, b: "HomeMadeSort"):
        return self.__lt__(b) or operator.eq(self, b)


one = HomeMadeSort(1)
two = HomeMadeSort(2)
print(operator.eq(one, two))
print(operator.lt(one, two))
print(operator.le(one, two))
print(operator.gt(one, two))
print(operator.ge(one, two))
print(operator.ne(one, two))


print(sorted(random_list))
print(sorted(random_list, key=HomeMadeSort))
