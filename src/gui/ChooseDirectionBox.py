from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5.QtWidgets import *


class ChooseDirectionBox(QWidget):
    directionClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super(ChooseDirectionBox, self).__init__()
        self.horizontal_group_box = QGroupBox()
        self.createGridLayout()
        window_layout = QVBoxLayout()
        window_layout.addWidget(self.horizontal_group_box)
        self.setLayout(window_layout)

    def createGridLayout(self):
        layout = QGridLayout()
        # layout.setColumnStretch(4, 0)

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
        self.directionClicked.emit('up')

    def leftClicked(self):
        self.directionClicked.emit('left')

    def rightClicked(self):
        self.directionClicked.emit('right')

    def downClicked(self):
        self.directionClicked.emit('down')


def window():
    app = QApplication(sys.argv)
    win = ChooseDirectionBox()
    win.show()
    sys.exit(app.exec_())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys

    sys.excepthook = except_hook
    window()
