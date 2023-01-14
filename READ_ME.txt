Итак, пока что я пишу тупо свои размышления по поводу программы.

Тех.Задание у меня следующее:
Сделать сортировщик PDF-страниц в файлах в соответствии с их порядковым номером, чтобы при печати в 4-ре листа,
разрезая, можно было получать стопки идущие от меньшего к большему (или наоборот). Форма страницы
разная и необходимо иметь возможность обработать каждый вариант.
Желательно, чтобы можно было перетащить в окно программы исходный файл, а получить уже обработанный.
[upd 04.01.23] Уже обработанный PDF-файл просто открывается и все (минимум сохранить).

03.11.22
Задачи вытекающие из Тех.Задания: [0/6]
[V] - Сортировщик от меньшего к большему (Вообще, делается в одну строчку (скорее всего))
[V] - Чтение необходимой части PDF файла (У нас есть несколько форматов и необходимо понять
каким обрахом их обрабатывать) | Эта задача являет собой наибольшую сложность.
[V/?] - Сортировка файлов по соответствию. (Можно сделать через Скопировать + Вставить в новый файл, например.)
[] - Окно, куда перетаскивать исходные файлы.
[] - Возможно, что стоит сделать возможным выбор папки для сохранения новых PDF-файлов.
[] - (!) - Сделать программу под ОС Windows (!) - Без этого она не имеет смысла.

Итак, какую структуру у программы я предполагаю?
1) Основной файл, откуда будут вызываться все функции и модули.
2) Файл-Ридер, где будет происходить чтение и запись данных из серии PDF-файлов.
    Тут есть 2 задачи, необходимых для решения.
    2.1) Выяснить кого закинули программе на переработку.
    2.2) Правильно считать то, что скинули.
3) Файл-Переработчик, где будет происходить создание нового ряда PDF-файла по необходимым критериям.
4) Файл для GUI, где будет реализована визуальная составляющая для конечного пользователя.


(!) Знаки препинания возникающие в этикетках:
/ + - — * .
(!) Если вместо знаков препинаний или цифр написаны БУКВЫ, то это должно быть в конце.


???????????

antonkuzmichev@Antons-iMac PDF-converter % /Users/antonkuzmichev/PycharmProjects/PDF-converter/pdf_dir/бокс\ \(1\).pdf
zsh: permission denied: /Users/antonkuzmichev/PycharmProjects/PDF-converter/pdf_dir/бокс (1).pdf

antonkuzmichev@Antons-iMac PDF-converter % python3 main.py

Drag and drop PDF-file here... /Users/antonkuzmichev/PycharmProjects/PDF-converter/pdf_dir/бокс\ \(1\).pdf

Traceback (most recent call last):
  File "/Users/antonkuzmichev/PycharmProjects/PDF-converter/main.py", line 25, in <module>
    page_count, list_of_names = read_write_make.pdf_reader_func(path)
  File "/Users/antonkuzmichev/PycharmProjects/PDF-converter/read_write_make.py", line 51, in pdf_reader_func
    reader = PdfReader(path)
  File "/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages/PyPDF2/_reader.py", line 317, in __init__
    with open(stream, "rb") as fh:
FileNotFoundError: [Errno 2] No such file or directory: '/Users/antonkuzmichev/PycharmProjects/PDF-converter/pdf_dir/бокс\\ \\(1\\).pdf '
antonkuzmichev@Antons-iMac PDF-converter %
