from time import sleep

from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox, QHBoxLayout
from core.grid import Grid
from gui.Overlay import GridOverlay
import core.env as env


class FighterView(QWidget):

    def __init__(self, parent):
        super(FighterView, self).__init__(parent)
        self.initButton()
        self.initLayout()
        self.mainWindow = parent

    def initButton(self):
        # next map button
        self.highlight_grid_button = QPushButton("highlight grid")
        self.highlight_grid_button.clicked.connect(self.highlightGrid)

    def initLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.button_combat_box = QGroupBox()
        self.button_combat_layout = QHBoxLayout()
        self.button_combat_box.setLayout(self.button_combat_layout)

        self.button_combat_layout.addWidget(self.highlight_grid_button)

        self.layout.addWidget(self.button_combat_box)
        self.layout.insertLayout(0, self.button_combat_layout)

    def highlightGrid(self, event):
        self.mainWindow.hide()
        combat_grid = Grid(env.COMBAT_R, env.VCELLS, env.HCELLS)
        combat_grid.parse()
        self.overlay = GridOverlay(combat_grid)
        self.overlay.highlightEnded.connect(self.mainWindow.show)
        self.overlay.highlight(2)

