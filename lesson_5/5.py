numbers = input('Введите числа через пробел')

with open(r"lesson_5/text_5.txt", "w+") as write_f:
    write_f.write(f'{numbers}')
    write_f.seek(0)
    content = write_f.read().split()
    sum_numbers = [int(i) for i in content]

print(sum(sum_numbers))
