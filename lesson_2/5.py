my_list = [7, 5, 3, 3, 2]

num = int(input('Введите новый элемент рейтинга: '))

for i in range(len(my_list)):
    if num > my_list[i]:
        my_list.insert(i, num)
        break
    elif num <= my_list[-1]:
        my_list.append(num)
        break
print(my_list)
