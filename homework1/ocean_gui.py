
import sys

from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QDesktopWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton
)
from PyQt5.QtGui import (
    QPainter,
    QColor,
    QBrush
)

from model import (
    Ocean,
    Shark,
    Guppies,
    Land,
    Water,
    generate_ocean
)


CELL_SIZE = 10
MAP_COLOR = {
    Shark: QColor(0, 0, 128, 128),
    Guppies: QColor(255, 164, 0, 128),
    Land: QColor(128, 128, 128, 128),
    Water: QColor(255, 255, 255, 128)
}


class OceanUI(QWidget):
    def __init__(self, ocean):
        super().__init__()

        self.ocean = ocean
        self.initUI()

    def initUI(self):
        window_size = self.ocean.size * CELL_SIZE
        self.resize(window_size, window_size)
        self.center()
        self.setWindowTitle('Ocean')
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        for idx, cell in enumerate(self.ocean):
            x, y = divmod(idx, self.ocean.size)
            qp.setBrush(MAP_COLOR[type(cell)])
            qp.drawRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

        qp.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    ocean = generate_ocean()

    ocean_ui = OceanUI(ocean)
    sys.exit(app.exec_())
