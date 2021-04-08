months = {
    1: 'Январь',
    2: 'Февраль',
    3: 'Март',
    4: 'Апрель',
    5: 'Май',
    6: 'Июнь',
    7: 'Июль',
    8: 'Август',
    9: 'Сентябрь',
    10: 'Октябрь',
    11: 'Ноябрь',
    12: 'Декарь'
}

seasons = {
    1: 'Зима',
    2: 'Весна',
    3: 'Лето',
    4: 'Осень'
}

num = int(input('Введите номер месяца: '))
if num == 12 or num <= 2:
    print(f'{seasons[1]} - {months[num]}')
elif 2 < num <= 5:
    print(f'{seasons[2]} - {months[num]}')
elif 5 < num <= 8:
    print(f'{seasons[3]} - {months[num]}')
elif 8 < num < 12:
    print(f'{seasons[4]} - {months[num]}')
else:
    print('Такого месяца нет')

# --------------------------------------------

# months = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декарь']
# seasons = ['', 'Зима', 'Весна', 'Лето', 'Осень']

# num = int(input('Введите номер месяца: '))
# if num == 12 or num <= 2:
#     print(f'{seasons[1]} - {months[num]}')
# elif 2 < num <= 5:
#     print(f'{seasons[2]} - {months[num]}')
# elif 5 < num <= 8:
#     print(f'{seasons[3]} - {months[num]}')
# elif 8 < num < 12:
#     print(f'{seasons[3]} - {months[num]}')
# else:
#     print('Такого месяца нет')
