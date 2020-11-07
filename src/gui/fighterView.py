from time import sleep
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox, QHBoxLayout
from core.grid import Grid
from gui.Overlay import GridOverlay
import core.env as env


class FighterView(QWidget):

    def __init__(self, mw):
        super(FighterView, self).__init__(mw)
        self.mw = mw

