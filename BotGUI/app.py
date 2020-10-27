# -*- coding: utf-8 -*-
from PyQt5.QtCore import QObject, pyqtSignal
from constants import *
from snippetWidget import QSnip
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *
from MyQtTree import MyQtTree
from ChangeMapBox import ChangeMapBox
import re


class Communicate(QObject):
    path_loaded = pyqtSignal()


class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.setGeometry(584, 171, 744, 671)
        self.setWindowTitle("Dofus Bot Path generator")
        self.setWindowIcon(QtGui.QIcon('icon.jpg'))
        widget = QWidget()
        self.setCentralWidget(widget)

        self.main_layout = QVBoxLayout()
        widget.setLayout(self.main_layout)
        self.vLayout = QVBoxLayout()
        self.main_layout.insertLayout(0, self.vLayout)

        self.infos_box = QGroupBox("Infos:")
        self.infos_box_layout = QVBoxLayout()
        self.infos_box.setLayout(self.infos_box_layout)
        self.main_layout.addWidget(self.infos_box)

        self.button_group_box = QGroupBox()
        self.button_map_box = QGroupBox()
        self.button_group_layout = QHBoxLayout()
        self.button_map_layout = QHBoxLayout()

        self.button_group_box.setLayout(self.button_group_layout)
        self.button_map_box.setLayout(self.button_map_layout)

        self.main_layout.addWidget(self.button_group_box)
        self.main_layout.addWidget(self.button_map_box)

        self.curr_map_idx = None
        self.path_file = None
        self.path_list = MyQtTree(self)
        self.initGui()
        if self.getFilePathFromCache():
            self.path_list.loadFromFile(self.path_file)
            self.curr_map_idx = len(self.path_list) - 1
        self.updatePathFileInfo()
        self.updateCurrentMapInfo()

    def initGui(self):
        # menu
        self.initMenu()

        # message label
        self.notification_text = QLabel()
        self.updateTopMessage("Press F5 to capture region.")
        self.vLayout.addWidget(self.notification_text)

        # save button button
        save_button = QPushButton("save path")
        save_button.clicked.connect(self.savePath)

        # capture region button
        capture_button = QPushButton("capture mode")
        capture_button.clicked.connect(self.startCaptureMode)

        # new map button
        create_map_button = QPushButton("new map")
        create_map_button.clicked.connect(self.createNewMap)

        # next map button
        next_map_button = QPushButton("next map")
        next_map_button.clicked.connect(self.askForDirection)
        self.button_group_layout.addWidget(save_button)
        self.button_group_layout.addWidget(capture_button)
        self.button_map_layout.addWidget(create_map_button)
        self.button_map_layout.addWidget(next_map_button)

        # init path list
        self.initPath()

        # populate infos box with labels stacked vertically
        self.current_map_info = QLabel()
        self.infos_box_layout.addWidget(self.current_map_info)
        self.current_path_file_info = QLabel()
        self.infos_box_layout.addWidget(self.current_path_file_info)

    def askForDirection(self):
        if self.curr_map_idx is None:
            QMessageBox.critical(self, "ERROR", "You didn't specify a current map.")
            return
        self.ch_map_box = ChangeMapBox(self)
        self.ch_map_box.directionClicked.connect(self.createNextMap)
        self.ch_map_box.show()

    def getCurrMapCoords(self):
        sx, sy = re.findall(MAP_REG, self.path_list[self.curr_map_idx].text(0))[0]
        return int(sx), int(sy)

    def createNextMap(self, direction):
        x, y = self.getCurrMapCoords()
        nx = x + direction[0]
        ny = y + direction[1]
        next_map_id = f"map[{nx},{ny}]"
        QTreeWidgetItem(self.path_list, [next_map_id])
        self.setCurrentMap(self.curr_map_idx + 1)

    def savePath(self):
        if not self.path_file:
            self.path_file = QFileDialog.getSaveFileName()[0]
        if self.path_file:
            self.path_list.saveToFile(self.path_file)
        else:
            QMessageBox.critical(self, "ERROR", "You didn't chose any file.")

    def initMenu(self):
        # Create new action
        newAction = QAction(text='&New', parent=self)
        newAction.setStatusTip('New path')
        newAction.triggered.connect(self.newPath)

        # Create new action
        openAction = QAction(text='&Open', parent=self)
        openAction.setStatusTip('Open path')
        openAction.triggered.connect(self.openPath)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)

    def newPath(self):
        self.path_file = QFileDialog.getSaveFileName()[0]
        if self.path_file:
            with open("cache", "w") as f:
                f.write(self.path_file)
            self.updatePathFileInfo()

    def initPath(self):
        self.path_list.deleteLater()
        self.path_list = MyQtTree(self)
        self.vLayout.addWidget(self.path_list)

    def openPath(self, event):
        self.path_file = QFileDialog.getOpenFileName()[0]
        self.initPath()
        if self.path_file:
            with open("cache", "w") as f:
                f.write(self.path_file)
            self.path_list.loadFromFile(self.path_file)
            self.updatePathFileInfo()

    def startCaptureMode(self):
        if self.curr_map_idx is None:
            QMessageBox.critical(self, "ERROR", "You didn't specify a current map.")
            return
        stypes = [
            "mapChange",
            "kralamoure",
            "poisskaille",
            "poissonPane",
            "sardineBrillante",
            "greuvette",
            "crabe",
            "espadon"
        ]
        self.hide()
        self.snip_win = QSnip(self, stypes)
        self.snip_win.snippetTaken.connect(self.appendMapRegions)
        self.snip_win.captureModeExited.connect(self.show)
        self.snip_win.show()

    def updateTopMessage(self, text):
        self.notification_text.setText(text)
        self.notification_text.adjustSize()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            self.startCaptureMode()
        event.accept()

    def appendMapRegions(self, snippet):
        curr_map = self.path_list[self.curr_map_idx]
        print(snippet)
        snippet = map(str, snippet)
        QTreeWidgetItem(curr_map, snippet)

    def getFilePathFromCache(self):
        with open("cache", "r") as f:
            self.path_file = f.read()
            if self.path_file:
                return True

    def createNewMap(self):
        map_id, ok_pressed = QInputDialog.getText(self, "Get map coordinates", "map coordinates :", QLineEdit.Normal, "")
        if re.match(COORD_REG, map_id):
            map_id.replace(" ", "")
            map_id = f"map[{map_id}]"
            QTreeWidgetItem(self.path_list, [map_id])
            self.setCurrentMap(self.curr_map_idx + 1)
        else:
            QMessageBox.critical(self, "ERROR", "valid map ID.")

    def askForCurrentMap(self):
        map_coord, ok_pressed = QInputDialog.getText(self, "Get map coordinates", "map coordinates :", QLineEdit.Normal, "")
        if re.match(COORD_REG, map_coord):
            map_coord.replace(" ", "").strip('\n')
            map_id = f"map[{map_coord}]"
            if map_id in self.path_list.maps():
                self.setCurrentMap(map_id)
            else:
                QMessageBox.critical(self, "ERROR", "Map ID you gave doesn't exist in path.")
        else:
            QMessageBox.critical(self, "ERROR", "You didn't give any valid map ID.")

    def updateCurrentMapInfo(self):
        self.current_map_info.setText(f"Current map is: {self.currentMap().text(0)}")
        self.current_map_info.adjustSize()

    def updatePathFileInfo(self):
        self.current_path_file_info.setText(f"Current path file is: {self.path_file}")
        self.current_map_info.adjustSize()

    def setCurrentMap(self, map_idx):
        self.curr_map_idx = map_idx
        self.updateCurrentMapInfo()

    def currentMap(self):
        return self.path_list[self.curr_map_idx]


def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    import sys
    sys.excepthook = except_hook
    window()
