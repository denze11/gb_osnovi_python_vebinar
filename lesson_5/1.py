for user_f in iter(input, ""):
    with open(r"lesson_5/text_1.txt", "a") as write_f:
        write_f.write(f'{user_f}\n')
