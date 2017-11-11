
import sys

from PyQt5.QtCore import (
    QCoreApplication,
    QBasicTimer,
)
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
    Strategy,
    generate_ocean
)


TIMER = 100
CELL_SIZE = 10
MAP_COLOR = {
    Shark: lambda obj: QColor(0, 0, 128, 255 * obj.percent_life()),
    Guppies: lambda obj: QColor(255, 164, 0, 255 * obj.percent_life()),
    Land: lambda obj: QColor(51, 102, 0, 255),
    Water: lambda obj: QColor(255, 255, 255, 255)
}


class OceanGUI(QWidget):
    def __init__(self, ocean, num_it=None):
        super().__init__()

        self.num_it = num_it
        self.cur_it = 0
        self.ocean = ocean
        self.initUI()

    def initUI(self):
        self.timer = QBasicTimer()
        self.timer.start(TIMER, self)

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
            qp.setBrush(MAP_COLOR[cell.__class__](cell))
            qp.drawRect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)

        qp.end()

    def timerEvent(self, e):
        Strategy.run_ocean(self.ocean)
        self.update()
        self.cur_it += 1

        if self.num_it is not None and self.cur_it == self.num_it:
            self.timer.stop()


def gui(ocean, num_it=None):
    app = QApplication(sys.argv)
    ocean_gui = OceanGUI(ocean, num_it)
    app.exec_()
