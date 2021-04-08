u_text = input('Введите любой текст или цифры через пробел: ')

u_text = u_text.split(' ')

for i in u_text:
    if len(i) > 10:
        i = i[:10]
        print(i)
    else:
        print(i)
