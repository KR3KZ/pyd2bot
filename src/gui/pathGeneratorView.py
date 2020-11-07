import os
import re

from PyQt5 import QtCore
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QPushButton, QTreeWidgetItem, \
    QFileDialog, QMessageBox, QAction, QInputDialog, QLineEdit, QListWidget, QWidget
from .constants import *
from gui.ChooseDirectionBox import ChooseDirectionBox
from gui.SnippetWidget import QSnip
import yaml


class MapCoordField(QLineEdit):
    def __init__(self, place_holder):
        super(MapCoordField, self).__init__()
        validator = QRegExpValidator(QRegExp("-?\d{2}"))
        self.setPlaceholderText(place_holder)
        self.setValidator(validator)


class PathList(QListWidget):
    def __init__(self):
        super(PathList, self).__init__()


class PathGeneratorView(QWidget):

    def __init__(self, parent):
        super(PathGeneratorView, self).__init__(parent)
        # Init path tab
        self.initGui()
        self.mw = parent
        self.path = []
        self.curr_map_idx = None
        self.pathFile = None
        self.patterns_dir = None
        self.start_map = None
        if self.getFilePathFromCache():
            self.pathList.loadFromFile(self.pathFile)
            self.start_map = self.path[0]
        else:
            self.pathFile = None

    def initGui(self):
        # main layout vbox
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.topBox = QGroupBox()
        self.topBoxLyt = QVBoxLayout()
        self.topBox.setLayout(self.topBoxLyt)
        self.layout.addWidget(self.topBox)

        # init path list
        self.pathList = QListWidget(self)
        self.topBoxLyt.addWidget(self.pathList)

        # message label
        self.chooseStartMapLyt = QHBoxLayout()
        self.startMapLbl = QLabel("Start Map: ")
        self.xcoords = MapCoordField("x coord")
        self.ycoords = MapCoordField("y coord")
        self.chooseStartMapLyt.addWidget(self.startMapLbl)
        self.chooseStartMapLyt.addWidget(self.xcoords)
        self.chooseStartMapLyt.addWidget(self.ycoords)
        self.topBoxLyt.insertLayout(1, self.chooseStartMapLyt)

        # Chose direction add to main widget
        self.chooseDirection = ChooseDirectionBox(self)
        self.layout.addWidget(self.chooseDirection)
        self.chooseDirection.directionClicked.connect(self.appendPath)

        # Save button at the bottom
        self.buttonsGrpBx = QGroupBox()
        self.buttonsLyt = QHBoxLayout()
        self.buttonsGrpBx.setLayout(self.buttonsLyt)
        self.saveButton = QPushButton("save path")
        self.saveButton.clicked.connect(self.savePath)
        self.buttonsLyt.addWidget(self.saveButton)
        self.layout.addWidget(self.buttonsGrpBx)

    def appendPath(self, direction):
        self.pathList.addItem(direction)

    def savePathAs(self):
        self.pathFile = QFileDialog.getSaveFileName()[0]
        self.savePath()
        self.updatePathFileInfo()

    def savePath(self):
        if not self.xcoords.text() or not self.ycoords.text():
            QMessageBox.critical(self.mw, "ERROR", "You didn't enter start map coords.")
            return

        if not self.pathFile:
            self.pathFile = QFileDialog.getSaveFileName(self.mw, 'Save Path', '',
                                                        "Bot Path File (*.path);;All Files (*)",
                                                        options=QFileDialog.DontUseNativeDialog)[0]
        if self.pathFile:
            with open(self.pathFile, 'w') as f:
                data = {"path": []}
                nbrItems = self.pathList.count()
                for i in range(nbrItems):
                    data["path"].append(self.pathList.item(i).text())
                data["start-map"] = (self.xcoords.text(), self.ycoords.text())
                yaml.dump(data, f)
        else:
            QMessageBox.critical(self.mw, "ERROR", "You didn't chose any file.")

    def newPath(self):
        self.pathFile = QFileDialog.getSaveFileName(self.mw, 'Select file to save path', '',
                                                    "Bot Path File (*.path);;All Files (*)",
                                                    options=QFileDialog.DontUseNativeDialog)[0]
        if self.pathFile:
            with open("cache", "w") as f:
                f.write(self.pathFile)

    def openPath(self):
        self.pathFile = QFileDialog.getOpenFileName()[0]
        self.pathList.clear()
        if os.path.exists(self.pathFile):
            with open(self.pathFile, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                for step in data["path"]:
                    self.pathList.addItem(step)
            x, y = data['start-map']
            self.xcoords.setText(x)
            self.Ycoords.setText(y)

    def openPatternsDir(self):
        self.patterns_dir = QFileDialog.getExistingDirectory(None, 'Select a folder:', 'C:\\', QFileDialog.ShowDirsOnly)

    def startCaptureMode(self):
        if self.curr_map_idx is None:
            QMessageBox.critical(self, "ERROR", "You didn't specify a current map.")
            return
        self.mw.hide()
        self.snip_win = QSnip(self, self.patterns_dir)
        self.snip_win.captureModeExited.connect(self.mw.show)
        self.snip_win.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            self.startCaptureMode()
        event.accept()

    def getFilePathFromCache(self):
        try:
            with open("cache", "r") as f:
                self.pathFile = f.read()
                if os.path.exists(self.pathFile):
                    return True
        except FileNotFoundError as e:
            pass
        return False

    def askFirstMap(self):
        map_coord, ok_pressed = QInputDialog.getText(self, "Get map coordinates", "map coordinates :", QLineEdit.Normal,
                                                     "")
        if re.match(COORD_REG, map_coord):
            map_coord.replace(" ", "").strip('\n')
            x, y = map(int, map_coord.split(","))
            self.path = [(x, y)] + self.path
        else:
            QMessageBox.critical(self, "ERROR", "You didn't enter valid coordinates!")
