number = int(input('Введите число: '))
item = number % 10
number //= 10

while number > 0:
    if number % 10 > item:
        item = number % 10
    number //= 10

print(f'Самое большое число - {item}')
