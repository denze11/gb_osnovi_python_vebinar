current_result = int(input('Введите ваш текущий результат: '))
desired_result = int(input('Введите желаемый результат: '))
percent = int(input('На сколько % Вы будете прибавлять каждый день?: '))
last_day = 1
print(f'{last_day}-й день: {current_result}')

while True:
    if current_result < desired_result:
        current_result += (current_result / 100 * percent)
        last_day += 1
        print(f'{last_day}-й день: {current_result:.3}')
    else:
        break
