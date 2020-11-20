import os

import yaml
from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *
import re
from .constants import *

from gui.constants import COORD_REG


def _mapList(map):
    m = map.childCount()
    return [_itemList(map.child(k)) for k in range(m)]


def _itemList(item):
    m = item.columnCount()
    return [item.text(k) for k in range(m)]


def _iterQTreeItem(item):
    n = item.topLevelItemCount()
    for i in range(n):
        yield item.topLevelItem(i)


class MyQtTree(QTreeWidget):
    def __init__(self, parent):
        super(MyQtTree, self).__init__()
        self.setColumnCount(5)
        self.headerLabels = ["Type", "PosX", "PosY", "Height", "Width", "PatternId"]
        self.setHeaderLabels(self.headerLabels)
        self.parent = parent
        self.selected = None
        self.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.customContextMenuRequested[QtCore.QPoint].connect(self.rightMenuShow)

    def loadFromFile(self, file_path):
        if os.path.exists(file_path):
            with open(file_path, 'r') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
                for mapPos, mapData in data.items():
                    x, y = mapPos
                    current = QTreeWidgetItem(self, [f"map[{x}, {y}]"])
                    for spot in mapData:
                        items = [spot[key] for key in self.headerLabels]
                        QTreeWidgetItem(current, items)

    def saveToFile(self, file_path):
        """
        {
        (0, 1): [
                    {
                        'type':
                        'rect':
                        'patternId':
                    },
                    ...
                ]
        (1, 1) : ...,

        }
        :param file_path:
        :return:
        """
        with open(file_path, 'w') as f:
            data = {}
            for mapId, entries in self.items():
                mx, my = re.findall(MAP_REG, mapId)[0]
                mapCoord = (int(mx), int(my))
                data[mapCoord] = []
                for entry in entries:
                    spotDict = {key: val for key, val in zip(self.headerLabels, entry)}
                    data[mapCoord].append(spotDict)
            yaml.dump(data, f, sort_keys=False)

    def items(self):
        for item in self:
            yield item.text(0).strip(), _mapList(item)

    def maps(self):
        for item in self:
            yield item.text(0)

    def delMap(self, map_idx):
        self.takeTopLevelItem(map_idx)
        if map_idx == self.parent.curr_map_idx:
            if self.parent.curr_map_idx > 0:
                self.parent.curr_map_idx -= 1
                self.parent.updateCurrentMapInfo()
            else:
                self.parent.curr_map_idx = None

    def rightMenuShow(self):
        index = self.selectedIndexes()[0]
        self.selected = self.itemFromIndex(index)
        self.rightMenu = QMenu(self)

        if self.selected.text(1) == '':
            removeAction = QAction(text="Delete", parent=self)
            removeAction.triggered.connect(self.removeMap)
            setCurrMapAction = QAction(text="Set current", parent=self)
            setCurrMapAction.triggered.connect(self.setCurrMap)
            editMapAction = QAction(text="Edit", parent=self)
            editMapAction.triggered.connect(self.editMap)
            self.rightMenu.addAction(removeAction)
            self.rightMenu.addAction(setCurrMapAction)
            self.rightMenu.addAction(editMapAction)
        else:
            removeAction = QAction(text="Delete", parent=self)
            removeAction.triggered.connect(self.removeSpot)
            self.rightMenu.addAction(removeAction)
        self.rightMenu.exec_(QCursor.pos())

    def removeSpot(self):
        p = self.selected.parent()
        p.removeChild(self.selected)

    def removeMap(self):
        for idx, map in enumerate(self):
            if map == self.selected:
                self.delMap(idx)

    def setCurrMap(self):
        for idx, map in enumerate(self):
            if map == self.selected:
                self.parent.setCurrentMap(idx)

    def editMap(self):
        map_id, ok_pressed = QInputDialog.getText(self, "Get map coordinates", "map coordinates :",
                                                  QLineEdit.Normal, "")
        if ok_pressed and re.match(COORD_REG, map_id):
            map_id.replace(" ", "")
            map_id = f"map[{map_id}]"
            self.selected.setText(0, map_id)

    def __len__(self):
        return self.topLevelItemCount()

    def __getitem__(self, map_idx):
        return self.topLevelItem(map_idx)

    def getMapList(self, map_idx):
        return _mapList(self[map_idx])

    def __iter__(self):
        n = self.topLevelItemCount()
        for i in range(n):
            yield self.topLevelItem(i)
