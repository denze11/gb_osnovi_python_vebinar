from google_trans_new import google_translator

translator = google_translator()

with open(r"lesson_5/text_4.txt", "r") as my_file:
    lines = my_file.readlines()

for i, value in enumerate(lines):
    new_item = value.split()
    ru_number = translator.translate(new_item[0], 'ru')
    with open(r"lesson_5/text_4_1.txt", "a") as write_f:
        write_f.write(f'{ru_number} {new_item[1]} {new_item[2]}\n')
