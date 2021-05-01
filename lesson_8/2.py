class DivisionMyNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Делить на ноль нельзя")


div = DivisionMyNull(10, 100)
print(DivisionMyNull.divide_null(10, 0))
print(DivisionMyNull.divide_null(10, 0.1))
print(div.divide_null(100, 0))
