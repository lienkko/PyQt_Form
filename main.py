import sys
import random
from PyQt5 import uic
from PyQt5.QtCore import QRect
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from PIL import Image, ImageDraw


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.setStyleSheet("background: white")
        self.box = [self.label, self.label_2, self.label_3]
        for i in self.box:
            i.hide()
        self.pushButton.clicked.connect(self.run)
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.pushButton.hide()
        for i in self.box:
            wh = random.randint(20, 100)
            image = Image.new('RGB', (wh + 1, wh + 1), "white")
            draw = ImageDraw.Draw(image)

            draw.ellipse((0, 0, wh, wh), 'yellow', 'blue')
            image.save('el.png')
            i.setGeometry(QRect(random.randint(20, 380), random.randint(20, 250), wh + 1, wh + 1))
            i.setPixmap(QPixmap("el.png"))
            i.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
