# -*- coding: utf-8 -*-
import os

from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from gui import FarmerView, FighterView, PathGeneratorView, PatternView


class Communicate(QObject):
    path_loaded = pyqtSignal()


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(584, 171, 744, 671)
        self.setWindowTitle("Dofus Walker")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.currProjectDir = None
        self.patternsDir = None

        # Initialize tab screen
        self.pathGenerator = PathGeneratorView(self)
        self.fighter = FighterView(self)
        self.farmer = FarmerView(self)
        self.patternCreator = PatternView(self)

        # Add tabs
        self.tabs.addTab(self.pathGenerator, "path")
        self.tabs.addTab(self.fighter, "combat")
        self.tabs.addTab(self.farmer, "farm")
        self.tabs.addTab(self.patternCreator, "pattern")

        # menu
        self.initMenu()

    def initMenu(self):
        # Create new action
        newAction = QAction(text='&New project', parent=self)
        newAction.setStatusTip('New path')
        newAction.triggered.connect(self.newProject)

        # Create new action
        openAction = QAction(text='&Open', parent=self)
        openAction.setStatusTip('Open path')
        openAction.triggered.connect(self.openProject)

        # save action
        saveAction = QAction(text='&Save', parent=self)
        saveAction.setStatusTip('Save path')
        saveAction.triggered.connect(self.pathGenerator.savePath)

        # save as action
        saveAsAction = QAction(text='&Save as', parent=self)
        saveAsAction.setStatusTip('Open path')
        saveAsAction.triggered.connect(self.pathGenerator.savePathAs)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(saveAsAction)

    def newProject(self):
        self.currProjectDir = str(
            QFileDialog.getExistingDirectory(self, "Select Directory", options=QFileDialog.DontUseNativeDialog))
        if self.currProjectDir:
            self.patternsDir = os.path.join(self.currProjectDir, 'patterns')
            self.pathsDir = os.path.join(self.currProjectDir, 'paths')
            self.logsDir = os.path.join(self.currProjectDir, 'logs')
            os.mkdir(self.patternsDir)
            os.mkdir(self.pathsDir)
            os.mkdir(self.logsDir)

    def openProject(self):
        self.currProjectDir = str(
            QFileDialog.getExistingDirectory(self, "Select Directory", options=QFileDialog.DontUseNativeDialog))
        self.patternsDir = os.path.join(self.currProjectDir, 'patterns')



def window():
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
