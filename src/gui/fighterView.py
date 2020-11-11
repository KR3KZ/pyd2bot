from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox, QHBoxLayout



class FighterView(QWidget):

    def __init__(self, mw):
        super(FighterView, self).__init__(mw)
        self.mw = mw

