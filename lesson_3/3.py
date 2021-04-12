def my_f(*args):
    '''Функция суммы наибольших двух аргументов'''
    return sum(sorted(args)[-2:])


print(my_f(20, 3, 10))
