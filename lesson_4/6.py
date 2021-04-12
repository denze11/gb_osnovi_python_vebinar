from sys import argv
from itertools import count
from itertools import cycle

file_name, number = argv

for el in count(int(number)):
    if el > 10:
        break
    else:
        print(el)

с = 0
for el in cycle(number):
    if с > 10:
        break
    print(el)
    с += 1
