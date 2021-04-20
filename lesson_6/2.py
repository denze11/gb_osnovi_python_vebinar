class Road:
    __length = None
    __width = None
    mass = None
    height = None
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def asphalt_calculation(self):
        self.mass = 25
        self.height = 0.05
        calculation = self.length * self.width * self.mass * self.height / 1000
        print(f'Для строительства необходимо {calculation} тон асфальта')

calculation = Road(5000, 20)
calculation.asphalt_calculation()