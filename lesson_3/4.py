def my_func(x, y):
    '''Функция возведения в степень'''
    item = 1
    for i in range(abs(y)):
        item *= x
    if y >= 0:
        return item
    else:
        return 1 / item


print(my_func(float(input('Введите X: ')), int(input('Введите Y: '))))


def my_func(x, y):
    return f'{x ** y}'

print(my_func(float(input('Введите X: ')), int(input('Введите Y: '))))
