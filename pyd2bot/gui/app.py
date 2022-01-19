# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *

from core import env
from gui.farmerView import FarmerView
from gui.fighterView import FighterView
from gui.pathGeneratorView import PathGeneratorView


class Communicate(QObject):
    path_loaded = pyqtSignal()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(1585, 29, 333, 997)
        self.setWindowTitle("Dofus Bot")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Initialize tab screen
        self.pathGenerator = PathGeneratorView(self)
        self.fighter = FighterView(self)
        self.farmer = FarmerView()

        # Add tabs
        self.tabs.addTab(self.pathGenerator, "path")
        self.tabs.addTab(self.fighter, "combat")
        self.tabs.addTab(self.farmer, "farm")

        # menu
        self.initMenu()
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)

    def initMenu(self):
        # Create new action
        newAction = QAction(text='&New', parent=self)
        newAction.setStatusTip('New project')
        newAction.triggered.connect(self.newProject)

        # Create new action
        openAction = QAction(text='&Open', parent=self)
        openAction.setStatusTip('Open project')
        openAction.triggered.connect(self.openProject)

        # save action
        saveAction = QAction(text='&Save', parent=self)
        saveAction.setStatusTip('Save')
        saveAction.triggered.connect(self.saveProject)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)

    def saveProject(self):
        self.pathGenerator.savePath()

    def newProject(self):
        self.currProjectDir = str(
            QFileDialog.getExistingDirectory(self, "Select directory",
                                             options=QFileDialog.DontUseNativeDialog,
                                             directory=r"C:\Users\khalid.majdoub\PycharmProjects\bot2pix"))
        if self.currProjectDir:
            self.patternsDir = os.path.join(self.currProjectDir, 'patterns')
            self.pathsDir = os.path.join(self.currProjectDir, 'paths')
            self.logsDir = os.path.join(self.currProjectDir, 'logs')
            os.mkdir(self.patternsDir)
            os.mkdir(self.pathsDir)
            os.mkdir(self.logsDir)
            for cat in self.pathGenerator.categories:
                cat_dir = os.path.join(self.patternsDir, cat)
                if not os.path.exists(cat_dir):
                    os.mkdir(cat_dir)

    def openProject(self):
        self.currProjectDir = str(
            QFileDialog.getExistingDirectory(self,
                                             "Select directory",
                                             options=QFileDialog.DontUseNativeDialog,
                                             directory=r"C:\Users\khalid.majdoub\PycharmProjects\bot2pix\examples"))
        self.patternsDir = os.path.join(self.currProjectDir, 'patterns')
        self.pathsDir = os.path.join(self.currProjectDir, 'paths')
        self.logsDir = os.path.join(self.currProjectDir, 'logs')


def window():
    env.focusDofusWindow()
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys

    sys.excepthook = except_hook
    window()
