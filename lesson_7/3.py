class Cell:
    def __init__(self, count: int):
        self._count = count

    def __add__(self, other):
        return Cell(self._count + other._count)

    def __sub__(self, other):
        if self._count > other._count:
            return Cell(self._count - other._count)

        return f"{self._count} - {other._count}: операция невозможна"

    def __mul__(self, other):
        return Cell(self._count * other._count)

    def __truediv__(self, other):
        return Cell(self._count // other._count)

    def make_order(self, other: int):
        rows, tail = self._count // other, self._count % other
        return '\n'.join(['*' * other] * rows + (['*' * tail] if tail else []))

    def __str__(self):
        return f"Клетка состоит из {self._count} ячеек"


cell_1 = Cell(25)
print(cell_1)
cell_2 = Cell(20)
print(cell_2)

print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_2 - cell_1)
print(cell_2 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print((cell_1 * cell_2).make_order(30))
