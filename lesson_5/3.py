salary = 0
item = 0

with open(r"lesson_5/text_3.txt", "r") as my_file:
    lines = my_file.readlines()

for _, value in enumerate(lines):
    new_item = value.split()
    salary += float(new_item[1])
    item += 1
    if float(new_item[1]) < 20000:
        print(f'{new_item[0]} - {new_item[1]}')
salary_sum = salary / item
print(f'Средняя зарплата сотрудников - {salary_sum}')
