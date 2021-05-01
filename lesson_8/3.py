class NotNumberError(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return self.text


my_list = []

while True:
    user_number = input('Введите число, или stop для выхода: ')
    if user_number == 'stop':
        print(my_list)
        break

    try:
        if not user_number.isdigit():
            raise NotNumberError(f'{user_number} не является числом')

        my_list.append(int(user_number))
    except NotNumberError as err:
        print(err)
