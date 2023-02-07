

"""Модуль вызова всех функций программы."""


import read_write_make
import dict_maker
import sorter_module
import make_and_print

import sys
from pathlib import Path


# path = "pdf_dir/print-barcodes (14).pdf"
# path = "pdf_dir/stickers (11).pdf"
# path = "pdf_dir/бокс (1).pdf"
# path = "pdf_dir/бокс (2).pdf"
# path = "pdf_dir/бокс (3).pdf"
# path = "pdf_dir/сдек (1).pdf"
# path = "pdf_dir/сдек (2).pdf"

# if __name__ == "__main__":

    # print("Please, drag and drop needed file: ")
    # user_inp = sys.stdin.readline()
    #
    # if len(user_inp) > 2:
    #     # path = sys.argv[1]
    #     path = user_inp


def main(path):
    if path:

        page_count, list_of_names = read_write_make.pdf_reader_func(path)

        dictionary = dict_maker.dictionary_maker(page_count, list_of_names)

        sorted_dictionary, list_of_keys = sorter_module.int_sorter(dictionary)

        matrix = sorter_module.matrix_fin_line(list_of_keys)

        data = read_write_make.making_line(matrix)

        make_and_print.making_pdf(data, path)

    else:
        print("No file found in arguments!")
