import sys
from PyQt5.QtWidgets import *


class WordTrick(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(400, 400, 400, 400)
        self.setWindowTitle('bye')

        self.p = QPushButton('aло', self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())