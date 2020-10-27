from PyQt5.QtCore import QObject, pyqtSignal
from constants import *
from PyQt5.QtWidgets import *


class ChangeMapBox(QMainWindow):
    directionClicked = pyqtSignal(tuple)

    def __init__(self, parent=None):
        super(ChangeMapBox, self).__init__()
        self.horizontal_group_box = QGroupBox()
        self.setGeometry(756, 305, 374, 258)
        self.setWindowTitle("Chose next map direction")
        widget = QWidget()
        self.setCentralWidget(widget)
        self.createGridLayout()
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.horizontal_group_box)
        widget.setLayout(window_layout)

    def createGridLayout(self):
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        up_button = QPushButton('Up')
        left_button = QPushButton('Left')
        right_button = QPushButton('Right')
        down_button = QPushButton('Down')

        up_button.clicked.connect(self.upClicked)
        left_button.clicked.connect(self.leftClicked)
        right_button.clicked.connect(self.rightClicked)
        down_button.clicked.connect(self.downClicked)

        layout.addWidget(up_button, 0, 1)
        layout.addWidget(left_button, 1, 0)
        layout.addWidget(right_button, 1, 2)
        layout.addWidget(down_button, 2, 1)

        self.horizontal_group_box.setLayout(layout)

    def upClicked(self):
        self.directionClicked.emit((0, -1))
        self.close()

    def leftClicked(self):
        self.directionClicked.emit((-1, 0))
        self.close()

    def rightClicked(self):
        self.close()
        self.directionClicked.emit((1, 0))

    def downClicked(self):
        self.directionClicked.emit((0, 1))
        self.close()


def window():
    app = QApplication(sys.argv)
    win = ChangeMapBox()
    win.show()
    sys.exit(app.exec_())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys

    sys.excepthook = except_hook
    window()
