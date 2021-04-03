gds = [
(1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
(2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}), 
(3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

while True:
    command = input('Введите цифру:\n1 - Если хотите посмотреть список товаров.\n2 - Если хотите создать товар.\n3 - Если хотите посмотреть аналитику\nexit - Если хотите выйти\n')
    if command == '1':
        if gds != []:
            for ind, el in enumerate(gds, 1):
                print(f'\n{ind}\nНазвание: {el[1]["название"]}\nЦена: {el[1]["цена"]}\nКоличество: {el[1]["количество"]}\nЕденица измерения: {el[1]["eд"]}\n')
        else:
            print('Список товаров пуст')
    elif command == '2':
        name = input('Введите название товара: ')
        price = input('Введите цену товара: ')
        quantity = input('Введите количество товара: ')
        measure = input('Введите единицу измерения товара (шт.): ')
        num_gds = len(gds) + 1
        gds.append((num_gds, {'название': name, 'цена': price, 'количество': quantity, 'eд': measure}))
    elif command == '3':
        analytics = {}
        i_analytics = []
        for i in range(len(gds)):
            i_analytics.append(gds[i][1]['название'])
            i_analytics.append(gds[i][1]['цена'])
            i_analytics.append(gds[i][1]['количество'])
            i_analytics.append(gds[i][1]['eд'])
            analytics['Название'] = i_analytics[::4]
            analytics['Цена'] = i_analytics[1::4]
            analytics['Количество'] = i_analytics[2::4]
            analytics['Еденица измерения'] = i_analytics[3::4]
        print(analytics)
    elif command == 'exit':
        break
    else:
        print('Команда не найдена!!!')
