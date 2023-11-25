import sys
from PyQt5 import uic
import random
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class WordTrick(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi('untitled.ui', self)
        self.k = False
        self.pushButton.clicked.connect(self.g)


    def g(self):
        self.k = True
        self.update()

    def paintEvent(self, event):
        #super().painEvent(event)
        if self.k:
            self.w = QPainter(self)
            self.w.begin(self)
            self.w.setBrush(QColor(255, 255, 0))
            self.ran = random.randint(1, 40)
            for i in range(13):
                self.w.drawEllipse(random.randint(0, 400), random.randint(0, 400), self.ran * i - self.ran, self.ran * i - self.ran)
            self.w.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WordTrick()
    ex.show()
    sys.exit(app.exec())