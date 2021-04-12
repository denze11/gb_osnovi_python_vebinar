def my_f(item_1, item_2):
    '''Функция деления двух чисел'''
    try:
        return int(item_1) / int(item_2)
    except (ZeroDivisionError, ValueError):
        return 'Можно вводить только цифры и на ноль делить нельзя'


print(my_f(input('Введите первое число: '), input('Введите второе число: ')))
