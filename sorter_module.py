

"""Сортировка численного словаря по возрастанию с получением номеров страниц, уже без текста;
Соединение списка ЧИСЛА со списком номеров страниц ТЕКСТ;
Формирование матрицы и составление нового списка на вывод."""


def int_sorter(data):

    """Принимает на вход словарь, сортирует его и возвращает отсортированный словарь.
    На основе знания, что словари с 3.6 имеют порядок!)"""

    counter = 0
    int_data = {}
    str_data = {}
    sorted_data = {}
    while counter < len(data):
        code = data[counter]
        code_six_ptc = code[0:6]
        if code_six_ptc.isdigit() is True:
            int_data[counter] = data[counter]
        else:
            str_data[counter] = data[counter]
        counter += 1

    int_data = dict(sorted(int_data.items(), key=lambda item: item[1]))
    str_data = dict(sorted(str_data.items(), key=lambda item: item[1]))

    sorted_data.update(int_data)
    sorted_data.update(str_data)
# Какая-то фигня. Код и так, и эдак работает корректно... Вроде как. Уже не соображаю.
    list_of_nums = sorted_data.keys()

    print(sorted_data)
    return sorted_data, list_of_nums


def matrix_fin_line(data):

    """Принимает на вход список, создает матрицу и возвращает ее."""

    in_row = 4
    page_count = len(data) / in_row
    page_count_inted = int(page_count)
    cycle_counter = 0

    r_1 = []
    r_2 = []
    r_3 = []
    r_4 = []
    r_1_counter = 0
    r_2_counter = 0
    r_3_counter = 0
    r_4_counter = 0
    matrix = [r_1, r_2, r_3, r_4]

    if page_count - page_count_inted == 0 or 0.25 or 0.5 or 0.75:
        pages_limit_remain = page_count - page_count_inted
        count_page_above_for_row = pages_limit_remain / 0.25

        # Эта часть кода просто ужас, но я не знаю как это сделать лучше. (!)
        if count_page_above_for_row == 0:
            pass
        if count_page_above_for_row == 1:
            r_1_counter += 1
        if count_page_above_for_row == 2:
            r_1_counter += 1
            r_2_counter += 1
        if count_page_above_for_row == 3:
            r_1_counter += 1
            r_2_counter += 1
            r_3_counter += 1

        # Это тоже очень костыльная часть кода, которую наверняка можно уменьшить.
        for element in data:
            if cycle_counter < page_count_inted + r_1_counter:
                r_1.append(element)
                cycle_counter += 1
            elif cycle_counter < (2 * page_count_inted) + r_1_counter + r_2_counter:
                r_2.append(element)
                cycle_counter += 1
            elif cycle_counter < (3 * page_count_inted) + r_1_counter + r_2_counter + r_3_counter:
                r_3.append(element)
                cycle_counter += 1
            elif cycle_counter < (4 * page_count_inted) + r_1_counter + r_2_counter + r_3_counter + r_4_counter:
                r_4.append(element)
                cycle_counter += 1
            else:
                print("Sort mistake")
                print(matrix)

        print("Sorting is finished")
        print(matrix)

    return matrix
