

"""Создание PDF-файла на печать, используя список для вызова необходимых страниц из изначального PDF-файла."""


from PyPDF2 import PdfReader, PdfWriter
import datetime as time


def making_pdf(data, path):

    reader = PdfReader(path)
    writer = PdfWriter()
    num_pages = len(reader.pages)
    print("Page count: " + str(num_pages) + "\nLength of line: " + str(len(data)))

    for page in data:
        # current_page = reader.getPage(page)
        current_page = reader.pages[page]
        writer.add_page(current_page)
    current_time = time.datetime.now()
    output_filename = "pdf_working_dir/File_{}.pdf".format(current_time)
    with open(output_filename, "wb") as out:
        writer.write(out)
    print("New Files Are Ready")
