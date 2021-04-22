class Stationery:
    title: ''

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    title = "ручка"

    def draw(self):
        print(f'Это - {self.title}')


class Pencil(Stationery):
    title = 'карандаш'

    def draw(self):
        print(f'Это - {self.title}')


class Handle(Stationery):
    title = 'маркер'

    def draw(self):
        print(f'Это - {self.title}')

stationery = Stationery()
stationery.draw()
pen = Pen()
pen.draw()
pencil = Pencil()
pencil.draw()
handle = Handle()
handle.draw()
