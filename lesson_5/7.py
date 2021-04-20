from re import findall
from json import dumps

all_profit = 0
number_of_firms = 0
list_profit = []
dict_company = {}
dict_average_profit = {}

with open(r'lesson_5/text_7.txt', 'r') as my_file:
    for i in my_file.readlines():
        company_name = [v for v in findall(r'^\S+', i)]
        company_data = [int(v) for v in findall(r'\d+', i)]
        company_profit = company_data[0] - company_data[1]
        if company_profit > 0:
            number_of_firms += 1
            all_profit += company_profit
        dict_company[f'{company_name[0]}'] = company_profit

list_profit.append(dict_company)
average_profit = all_profit / number_of_firms
dict_average_profit['average_profit'] = average_profit
list_profit.append(dict_average_profit)

with open(r'lesson_5/text_7_1.json', "w") as fhd:
    fhd.write(dumps(list_profit, ensure_ascii=False, indent=4))
