from itertools import count
from math import factorial


def fact():
    for el in count(1):
        def result(el): return result(el-1) * el if el > 0 else 1
        yield result(el)


# def fact():
#     for el in count(1):
#         yield factorial(el)


x = 0
for el in fact():
    if x < 15:
        print(el)
        x += 1
    else:
        break
