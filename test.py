from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QVBoxLayout, QListWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Drag & Drop')

        # Даем разрешение на Drop
        self.setAcceptDrops(True)

        self.list_files = QListWidget()
        self.label_total_files = QLabel()

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel('Drag and drop the file:'))
        main_layout.addWidget(self.list_files)
        main_layout.addWidget(self.label_total_files)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)

        self.setCentralWidget(central_widget)

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

        self._update_states()

        return super().dropEvent(event)


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.resize(500, 350)
    mw.show()

    app.exec()