class Car:
    def __init__(self, color, name, is_police: bool = False):
        self.color = color
        self.name = name
        self.is_police = True if is_police else False
        self.speed = 0
        self._direction = ''

    def go(self, speed):
        self.speed = speed

    def stop(self):
        self.speed = 0

    def turn(self, direction):

        self._direction = direction

        if self.speed:
            if direction == 'лево':
                print('Машина повернула на лево')
            elif direction == 'право':
                print('Машина повернула на право')
            else:
                print(f'неправильное направление')
        else:
            print('Не могу повернуть на месте')

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')

class TownCar(Car):

    _max_speed = 60

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_speed:
            print('Скорость превышена')


class SportCar(Car):
    def __init__(self, *args):
        super().__init__(*args)


class WorkCar(Car):
    _max_speed = 40

    def __init__(self, *args):
        super().__init__(*args)

    def show_speed(self):
        super().show_speed()
        if self.speed > self._max_speed:
            print('Скорость превышена')


class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


car = WorkCar('Red', 'Niva')
car.turn('лево')
car.go(30)
car.show_speed()
car.turn('лево')
car.go(75)
car.show_speed()
car.turn('право')
car.stop()
car.show_speed()
car.turn('право')
