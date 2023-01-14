

"""Проверка текста в txt файле, получение данных, составление пары в формате: ///номер страницы : текст/// ,
возвращая маленький словарь обратно."""

"""Проверка полученных данных в словаре, сортировка словаря на текст и числа (числа + сложные числа),
составление двух словарей."""


def dictionary_maker(page_count, list_of_names):
    counter = 0
    dictionary = {}
    while counter < page_count:
        dictionary[counter] = list_of_names[counter]
        counter += 1
    return dictionary
