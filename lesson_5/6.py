import re

my_dict = {}

with open(r"lesson_5/text_6.txt", "r") as my_file:
    for i in my_file.readlines():
        subject = [v for v in re.findall(r'^\w+', i)]
        sum_hours = sum([int(v) for v in re.findall(r'\d+', i)])
        my_dict[f'{subject[0]}'] = sum_hours

print(my_dict)
