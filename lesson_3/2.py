specification = input(
    'Введите Имя, Фамилия, Год рождения, Город проживания, Email, Телефон - через пробел: ').split()


def parameters(**kwargs):
    return ' '.join(kwargs.values())


print(parameters(nam=specification[0], surname=specification[1], year=specification[2],
      city=specification[3], email=specification[4], phone=specification[5]))
