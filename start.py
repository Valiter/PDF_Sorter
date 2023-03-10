from PyQt5.QtWidgets import (QTreeView, QFileSystemModel, QApplication, QMainWindow, QLabel, QWidget,
                             QVBoxLayout, QListWidget, QPushButton)
from PyQt5.QtCore import QDir

import read_write_make
import dict_maker
import sorter_module
import make_and_print


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


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Drag & Drop')
        self.setGeometry(500, 100, 500, 400)

        # Даем разрешение на Drop
        self.setAcceptDrops(True)

        self.list_files = QListWidget()
        self.label_total_files = QLabel()

        model = QFileSystemModel()
        model.setRootPath(QDir.currentPath())
        model.setReadOnly(False)

        self.tree = QTreeView()
        self.tree.setModel(model)
        self.tree.setRootIndex(model.index(QDir.currentPath()))
        self.tree.setSelectionMode(QTreeView.SingleSelection)
        self.tree.setDragDropMode(QTreeView.InternalMove)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.tree)
        main_layout.addWidget(QLabel('Перетащите файл:'))
        main_layout.addWidget(self.list_files)
        main_layout.addWidget(self.label_total_files)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)
        # button1 = QPushButton("Button1", self)
        # button1.clicked.connect(self.buttonCliched)
        self._update_states()

    def _update_states(self):
        self.label_total_files.setText('Files: {}'.format(self.list_files.count()))

    def dragEnterEvent(self, event):
        # Тут выполняются проверки и дается (или нет) разрешение на Drop

        mime = event.mimeData()

        # Если перемещаются ссылки
        if mime.hasUrls():
            # Разрешаем
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Обработка события Drop

        for url in event.mimeData().urls():
            file_name = url.toLocalFile()
            self.list_files.addItem(file_name)
            main(file_name)

        self._update_states()

        return super().dropEvent(event)

    # def buttonCliched(self):
    #     c = self.list_files
    #     self.list_files


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
