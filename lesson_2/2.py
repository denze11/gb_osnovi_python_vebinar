num = int(input('Введите количество элиментов в списке: '))
my_list = []
item_1 = 1

while num > 0:
    new_list = input(f'Введите {item_1}-й элимент: ')
    my_list.append(new_list)
    item_1 += 1
    num -= 1

for i in my_list[1:len(my_list)+1:2]:
    list_1 = my_list.index(i)
    list_2 = my_list.index(i) - 1
    my_list[list_1], my_list[list_2] = my_list[list_2], my_list[list_1]

print(my_list)
