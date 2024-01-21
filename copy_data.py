from return_data_file import data_file


def copy_file():
    copy_from, nf = data_file()
    count_rows = len(copy_from)
    number_row = int(input(f"Введите номер строки "
                           f"от 1 до {count_rows}: "))
    while number_row < 1 or number_row > count_rows:
        number_row = int(input(f"Ошибка!"
                               f"Введите номер строки "
                               f"от 1 до {count_rows}: "))
    if nf == 1:
        copy_to_file_number = 2
    else:
        copy_to_file_number = 1
    name = copy_from[number_row - 1].split(';')[1]
    surname = copy_from[number_row - 1].split(';')[2]
    birthdate = copy_from[number_row - 1].split(';')[3]
    town = copy_from[number_row - 1].split(';')[4]
    with open(f'db/data_{copy_to_file_number}.txt', 'r', encoding='utf-8') as file:
        copy_to = file.readlines()
    now_number_row = len(copy_to) + 1
    with open(f'db/data_{copy_to_file_number}.txt', 'a', encoding='utf-8') as file:
        file.write(f'\n{now_number_row};{name};'
                   f'{surname};{birthdate};{town}\n')
    print("Данные успешно скопированы!")
    answer = input("Вы желаете удалить скопированные данные из исходного файла?/n"
                   "Напишите 'Да' или 'Нет' ").lower()
    while answer != 'да' and answer != 'нет':
        answer = input('Введите корректный ответ! ').lower()
    if answer == 'да':
        del copy_from[number_row - 1]
        copy_from = [f'{i + 1};{copy_from[i].split(";")[1]};'
                f'{copy_from[i].split(";")[2]};'
                f'{copy_from[i].split(";")[3]};'
                f'{copy_from[i].split(";")[4]}'
                for i in range(len(copy_from))]
        with open(f'db/data_{nf}.txt', 'w', encoding='utf-8') as file:
            file.writelines(copy_from)
        print("Строка успешно удалена!")