with open(r"lesson_5/text_2.txt", "r") as my_file:
    lines = my_file.readlines()
    for i, v in enumerate(lines):
        number_of_words = len(v.split())
        print(f'Строка: {i+1} - Слов: {number_of_words}')
