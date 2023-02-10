

"""Чтение PDF-файла, запись данных в txt формат, получение нужных слов в формате словарей, составление словаря."""


from PyPDF2 import PdfReader


def word_and_num_seeker(page_text):

    """Функция поиска опорных слов, чтобы подтвердить читаемость файла."""

    def del_slash_n(info):

        """Функция для 'отброса' такой неприятной штуки как '\n' в строке."""

        tale = info[-1:]  # ?
        tale = len(tale)
        length = len(info)
        new_info = info[0:(length-tale)]
        return new_info

    returning_info = None
    counter = 0

    for element in page_text:  # enumerate - внутренний сч>тчик for

        if element == "СЕЛТОП\n":  # ? Может /n и не нужен? Чек
            returning_info = page_text[counter - 1]  # Чек регулярные выражения.
        else:
            find = element.find("№ ИМ")
            if find == 0:
                returning_info = element
                returning_info = returning_info[5:]
            else:
                returning_info = "None"

        counter += 1

    returning_info = del_slash_n(returning_info)

    if returning_info is None:
        returning_info = False
        print("!")

    return returning_info


def pdf_reader_func(path):

    """Функция с открытием PDF-файла и записью в TXT формат данных из него"""

    reader = PdfReader(path)
    num_pages = len(reader.pages)
    print("Page count: " + str(num_pages))
    counter = 0
    ls_file = []
    ls_word = []

    while counter < num_pages:
        # Первая обработка файла.
        file = open("pdf_dir/text_working.txt", "w")
        page = reader.pages[counter]
        file.write(page.extract_text())
        file.close()

        # with open("", "w") as file:
        #     page = reader.pages[counter]
        #     file.write(page.extractText())

        # Вторая обработка файла.
        file = open("pdf_dir/text_working.txt", "r")
        txt = file.readlines()
        # Может быть код, связанный с длинной теста уже и не нужен.
        txt_length = len(txt)
        ls_file.append(txt_length)

        body = word_and_num_seeker(txt)

        ls_word.append(body)

        file.close()
        counter += 1

    # print(ls_file)
    # print(ls_word)
    return num_pages, ls_word


def making_line(matrix_data):

    """Функция для создания нового списка по срезам"""

    max_row_len = len(matrix_data[0])
    new_line = []
    row_index = 0
    row_length = 0

    while row_length < max_row_len:
        while row_index < 4:
            if row_length < len(matrix_data[row_index]):
                new_line.append(matrix_data[row_index][row_length])
            row_index += 1
        row_index = 0
        row_length += 1
    # print(new_line)
    return new_line
