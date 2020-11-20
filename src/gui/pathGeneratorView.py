import os
import re

from PyQt5 import QtCore
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QPushButton, QTreeWidgetItem, \
    QFileDialog, QMessageBox, QAction, QInputDialog, QLineEdit, QWidget

from core import env
from .constants import *
from gui.ChooseDirectionBox import ChooseDirectionBox
from gui.MyQtTree import MyQtTree
from gui.SnippetWidget import QSnip


class MapCoordField(QLineEdit):
    def __init__(self, place_holder):
        super(MapCoordField, self).__init__()
        validator = QRegExpValidator(QtCore.QRegExp("-?\d{2}"))
        self.setPlaceholderText(place_holder)
        self.setValidator(validator)


class GetMapField(QWidget):

    def __init__(self, label_text):
        super(GetMapField, self).__init__()
        self.chooseStartMapLyt = QHBoxLayout()
        self.startMapLbl = QLabel(label_text)
        self.xcoords = MapCoordField("x coord")
        self.ycoords = MapCoordField("y coord")
        self.chooseStartMapLyt.addWidget(self.startMapLbl)
        self.chooseStartMapLyt.addWidget(self.xcoords)
        self.chooseStartMapLyt.addWidget(self.ycoords)
        self.set_button = QPushButton("set")
        self.chooseStartMapLyt.addWidget(self.set_button)
        window_layout = QVBoxLayout()
        window_layout.insertLayout(0, self.chooseStartMapLyt)
        self.setLayout(window_layout)

    def x(self):
        return self.xcoords.text()

    def y(self):
        return self.ycoords.text()


class PathGeneratorView(QWidget):

    def __init__(self, main_window):
        super(PathGeneratorView, self).__init__()

        self.mw = main_window

        # Init path tab
        self.initLayout()
        self.initWidgets()

        self.curr_map_idx = None
        self.path_name = None

        if self.getFilePathFromCache():
            self.path_list.loadFromFile(self.path_name)
            self.curr_map_idx = len(self.path_list) - 1
        else:
            self.path_name = None

        self.updatePathFileInfo()
        self.updateCurrentMapInfo()
        #
        # self.categories = [
        #     "crabe",
        #     "espadon",
        #     "goujon",
        #     "greuvette",
        #     "kralamoure",
        #     "mapChange",
        #     "poisskaille",
        #     "poissonPane",
        #     "sardineBrillante",
        #     "raie",
        #     "requin_marteau_faucille"
        # ]
        self.categories = [
            "frene",
            "ortie",
            "sauge",
            "mapChange"
        ]

    def patternDir(self, ptype):
        return os.path.join(self.mw.patternsDir, ptype)

    def initLayout(self):
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # top box (list + choose start map)
        self.topBox = QGroupBox()
        self.topBoxLyt = QVBoxLayout()
        self.topBox.setLayout(self.topBoxLyt)
        self.layout.addWidget(self.topBox)

        # show infos about path and current map
        self.infos_box = QGroupBox("Infos:")
        self.infos_box_layout = QVBoxLayout()
        self.infos_box.setLayout(self.infos_box_layout)
        self.layout.addWidget(self.infos_box)

        # buttons group box
        self.button_group_box = QGroupBox()
        self.button_group_layout = QHBoxLayout()
        self.button_group_box.setLayout(self.button_group_layout)

    def initWidgets(self):
        self.layout.addWidget(self.button_group_box)

        # save button button
        self.save_button = QPushButton("save path")
        self.save_button.clicked.connect(self.savePath)

        # Capture region button
        self.capture_button = QPushButton("capture mode")
        self.capture_button.clicked.connect(self.startCaptureMode)

        # load path button
        self.load_button = QPushButton("load path")
        self.load_button.clicked.connect(self.openPath)

        self.button_group_layout.addWidget(self.capture_button)
        self.button_group_layout.addWidget(self.save_button)
        self.button_group_layout.addWidget(self.load_button)

        # message label
        self.notification_text = QLabel()
        self.updateTopMessage("Press F5 to capture region.")
        self.topBoxLyt.addWidget(self.notification_text)

        # Chose direction add to main widget
        self.chooseDirection = ChooseDirectionBox(self)
        self.layout.addWidget(self.chooseDirection)
        self.chooseDirection.directionClicked.connect(self.createNextMap)

        # init path list
        self.path_list = MyQtTree(self)
        self.initPath()

        # Set start map
        self.startMap = GetMapField("Start map: ")
        self.topBoxLyt.addWidget(self.startMap)
        self.startMap.set_button.clicked.connect(self.setStartMap)

        # populate infos box with labels stacked vertically
        self.current_map_info = QLabel()
        self.infos_box_layout.addWidget(self.current_map_info)
        self.current_path_file_info = QLabel()
        self.infos_box_layout.addWidget(self.current_path_file_info)

    def setStartMap(self):
        nx = self.startMap.x()
        ny = self.startMap.y()
        map_id = f"map[{nx},{ny}]"
        QTreeWidgetItem(self.path_list, [map_id])
        self.setCurrentMap(0)

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

    def openPath(self):
        self.path_name = QFileDialog.getOpenFileName(self, "Select path",
                                             options=QFileDialog.DontUseNativeDialog,
                                             directory=self.mw.pathsDir)[0]
        self.path_list.loadFromFile(self.path_name)
        self.curr_map_idx = len(self.path_list) - 1
        self.updateCurrentMapInfo()

    def savePathAs(self):
        self.savePath()
        self.updatePathFileInfo()

    def initPath(self):
        self.path_list.deleteLater()
        self.path_list = MyQtTree(self)
        self.topBoxLyt.addWidget(self.path_list)

    def savePath(self):
        if not self.path_name:
            self.path_name = QInputDialog.getText(self, "Get path name", "Name for the path :",
                                                  QLineEdit.Normal, "")[0]
        if self.path_name:
            path_file = os.path.join(self.mw.pathsDir, self.path_name)
            self.path_list.saveToFile(path_file)
        else:
            QMessageBox.critical(self, "ERROR", "You didn't chose any name.")

    def startCaptureMode(self):
        if self.curr_map_idx is None:
            QMessageBox.critical(self, "ERROR", "You didn't specify a current map.")
            return
        self.mw.hide()
        self.snip_win = QSnip(self, self.categories)
        self.snip_win.snippetTaken.connect(self.appendMapRegions)
        self.snip_win.captureModeExited.connect(self.mw.show)
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
        snippet = map(str, snippet)
        QTreeWidgetItem(curr_map, snippet)

    def getFilePathFromCache(self):
        try:
            with open("cache", "r") as f:
                self.path_name = f.read()
                if os.path.exists(self.path_name):
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
        if self.curr_map_idx is not None:
            self.current_map_info.setText(f"Current map is: {self.currentMap().text(0)}")
        else:
            self.current_map_info.setText(f"Current map is: None")
        self.current_map_info.adjustSize()

    def updatePathFileInfo(self):
        self.current_path_file_info.setText(f"Current path file is: {self.path_name}")
        self.current_map_info.adjustSize()

    def setCurrentMap(self, map_idx):
        self.curr_map_idx = map_idx
        self.updateCurrentMapInfo()

    def currentMap(self):
        if self.curr_map_idx is not None:
            return self.path_list[self.curr_map_idx]
        else:
            return None
