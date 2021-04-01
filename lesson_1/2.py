number = int(input('Введите число: '))

hour = number // 3600
minute = (number // 60) % 60
second = number % 60
zero = '0'

if hour < 10:
    hour = zero + str(hour)

if minute < 10:
    minute = zero + str(minute)

if second < 10:
    second = zero + str(second)

print(f'{hour}:{minute}:{second}')
