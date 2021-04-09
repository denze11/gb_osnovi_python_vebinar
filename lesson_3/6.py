def int_func(words):
    result = ''
    for i in words:
        i = i[0].upper() + i[1:]
        result += i + ' '
    return ''.join(result)


words_list = input('Введите слова через пробел: ').split()
print(int_func(words_list))


def int_func(words):
    return words.title()


words_list = ' '.join(input('Введите слова через пробел: ').split())


print(int_func(words_list))
