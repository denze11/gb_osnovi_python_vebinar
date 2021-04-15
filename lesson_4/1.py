from sys import argv

file_name, working_hours, rate, premium = argv
try:
    print(f'Ваша зарплата составляет - ',
          int(working_hours) * int(rate) + int(premium))
except ValueError:
    print('Пожалуйста введите значения в цифрах')
