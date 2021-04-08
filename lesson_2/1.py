my_list = [1, 1.2, 'это, строка', ('это', 'кортеж'), {'это', 'множество'}, {'это': 'словарь'}, True, bytes('bytes', encoding = 'utf-8'), bytearray('bytearray', encoding = 'utf-8'), None]

for i in my_list:
    print(type(i))
