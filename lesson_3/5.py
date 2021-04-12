my_sum = []
idx = True

while idx:
    command = (input('Введите цифры через пробел или Q для выхода: ').upper().split())
    for i in command:
        if i == 'Q':
            idx = False
            break
        elif True == i.isdigit():
            my_sum.append(int(i))
        else:
            print(f'{i} - это не цифра')
    print(sum(my_sum))
