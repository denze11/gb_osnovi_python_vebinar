proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if proceeds - costs > 0:
    print(f'У Вашей фирмы прибыль {proceeds - costs}')
elif proceeds - costs < 0:
    print(f'У Вашей фирмы убыток "{proceeds - costs}"')
else:
    print('Ваша фирма отработала в ноль')
