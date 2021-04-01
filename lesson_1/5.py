proceeds = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if proceeds - costs > 0:
    profit = 100 * ( proceeds - costs) // proceeds
    print(f'У вашей фирмы прибыль {profit}%')
    worker = int(input('Введите количество работников: '))
    w_profit = proceeds // worker
    print(f'Прибыль на одного работника составила {w_profit} тысяч')

elif proceeds - costs < 0:
    loss = 100 * (proceeds - costs) // costs
    print(f'У вашей фирмы убыток "{loss}%"')
else:
    print('Ваша фирма отработала в ноль')
