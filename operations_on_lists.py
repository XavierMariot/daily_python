import typing

l = [1, 2, 3, 4, 5, 6, 7]
n = range(8, 12)
reversed(l)

try:
    a = next(x for x in reversed(l) if x == 10)
except StopIteration:
    pass

print(zip(l, n))

