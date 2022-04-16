from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

stuInfo = [{'name': 'farzad', 'family': 'adelfar', 'id': 99},
           {'name': 'ali', 'family': 'mamad', 'id': 90},
           {'name': 'ali', 'family': 'adelfar', 'id': 98}]


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Info app')
        self.setGeometry(450, 150, 600, 600)
        self.setLayout(QVBoxLayout())

        lab = QLabel('NAME: ')
        self.layout().addWidget(lab)
        lab.setFont(QFont('italic', 15))

        b1 = QPushButton('press', clicked=lambda: name())
        self.layout().addWidget(b1)

        lab_4 = QLabel('ID: ')
        self.layout().addWidget(lab_4)
        lab_4.setFont(QFont('italic', 15))

        b2 = QPushButton('press', clicked=lambda: stu_id())
        self.layout().addWidget(b2)

        def name():
            for num in stuInfo:
                print(num['name'])

        def stu_id():
            for i in stuInfo:
                print(i['id'])

        self.show()


app = QApplication([])
mw = MainWindow()

app.exec_()