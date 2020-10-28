import os
import re

from PyQt5 import QtCore
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QPushButton, QTreeWidgetItem, \
    QFileDialog, QMessageBox, QAction, QInputDialog, QLineEdit, QWidget
from .constants import *
from gui.ChangeMapBox import ChangeMapBox
from gui.MyQtTree import MyQtTree
from gui.SnippetWidget import QSnip


class PathGeneratorView(QWidget):

    def __init__(self):
        super(PathGeneratorView, self).__init__()

        # Init path tab
        self.initLayout()
        self.initWidgets()

        self.curr_map_idx = None
        self.path_file = None
        if self.getFilePathFromCache():
            self.path_list.loadFromFile(self.path_file)
            self.curr_map_idx = len(self.path_list) - 1
        else:
            self.path_file = None
        self.updatePathFileInfo()
        self.updateCurrentMapInfo()

    def initLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.vLayout = QVBoxLayout()
        self.layout.insertLayout(0, self.vLayout)

        self.infos_box = QGroupBox("Infos:")
        self.infos_box_layout = QVBoxLayout()
        self.infos_box.setLayout(self.infos_box_layout)
        self.layout.addWidget(self.infos_box)

        self.button_group_box = QGroupBox()
        self.button_map_box = QGroupBox()
        self.button_group_layout = QHBoxLayout()
        self.button_map_layout = QHBoxLayout()

        self.button_group_box.setLayout(self.button_group_layout)
        self.button_map_box.setLayout(self.button_map_layout)

    def initWidgets(self):
        self.layout.addWidget(self.button_group_box)
        self.layout.addWidget(self.button_map_box)

        # message label
        self.notification_text = QLabel()
        self.updateTopMessage("Press F5 to capture region.")
        self.vLayout.addWidget(self.notification_text)

        # save button button
        self.save_button = QPushButton("save path")
        self.save_button.clicked.connect(self.savePath)

        # capture region button
        self.capture_button = QPushButton("capture mode")
        self.capture_button.clicked.connect(self.startCaptureMode)

        # new map button
        self.create_map_button = QPushButton("new map")
        self.create_map_button.clicked.connect(self.createNewMap)

        # next map button
        self.next_map_button = QPushButton("next map")
        self.next_map_button.clicked.connect(self.askForDirection)

        # Populate path tab layout with widgets
        self.button_group_layout.addWidget(self.save_button)
        self.button_group_layout.addWidget(self.capture_button)
        self.button_map_layout.addWidget(self.create_map_button)
        self.button_map_layout.addWidget(self.next_map_button)

        # init path list
        self.path_list = MyQtTree(self)
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

    def savePathAs(self):
        self.path_file = QFileDialog.getSaveFileName()[0]
        self.savePath()
        self.updatePathFileInfo()

    def savePath(self):
        if not self.path_file:
            self.path_file = QFileDialog.getSaveFileName()[0]
        if self.path_file:
            self.path_list.saveToFile(self.path_file)
        else:
            QMessageBox.critical(self, "ERROR", "You didn't chose any file.")

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

    def openPath(self):
        self.path_file = QFileDialog.getOpenFileName()[0]
        self.initPath()
        if os.path.exists(self.path_file):
            with open("cache", "w") as f:
                f.write(self.path_file)
            self.path_list.loadFromFile(self.path_file)
            self.updatePathFileInfo()
            self.curr_map_idx = len(self.path_list) - 1
            self.updateCurrentMapInfo()

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
        try:
            with open("cache", "rect") as f:
                self.path_file = f.read()
                if os.path.exists(self.path_file):
                    return True
        except FileNotFoundError as e:
            pass
        return False

    def createNewMap(self):
        map_id, ok_pressed = QInputDialog.getText(self, "Get map coordinates", "map coordinates :", QLineEdit.Normal,
                                                  "")
        if re.match(COORD_REG, map_id):
            map_id.replace(" ", "")
            map_id = f"map[{map_id}]"
            QTreeWidgetItem(self.path_list, [map_id])
            self.setCurrentMap(self.curr_map_idx + 1)
        else:
            QMessageBox.critical(self, "ERROR", "valid map ID.")

    def askForCurrentMap(self):
        map_coord, ok_pressed = QInputDialog.getText(self, "Get map coordinates", "map coordinates :", QLineEdit.Normal,
                                                     "")
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
        if self.curr_map_idx:
            self.current_map_info.setText(f"Current map is: {self.currentMap().text(0)}")
        else:
            self.current_map_info.setText(f"Current map is: None")
        self.current_map_info.adjustSize()

    def updatePathFileInfo(self):
        self.current_path_file_info.setText(f"Current path file is: {self.path_file}")
        self.current_map_info.adjustSize()

    def setCurrentMap(self, map_idx):
        self.curr_map_idx = map_idx
        self.updateCurrentMapInfo()

    def currentMap(self):
        if self.curr_map_idx:
            return self.path_list[self.curr_map_idx]
        else:
            return None
