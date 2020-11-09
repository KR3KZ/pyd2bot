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
        self.setHeaderLabels(["Name", "PosX", "posY", "Height", "Width"])
        self.parent = parent
        self.selected = None
        self.clicked.connect(self.onClick)

    def loadFromFile(self, file_path):
        with open(file_path, "rect") as f:
            for line in f.readlines():
                if line:
                    line = line.rstrip('\n')
                    if line and not line.startswith('#'):
                        step = line.split(',')
                        QTreeWidgetItem(current, step)
                    else:
                        current = QTreeWidgetItem(self, [line[1:]])

    def saveToFile(self, file_path):
        with open(file_path, 'w') as f:
            lines = []
            for mapId, entries in self.items():
                if mapId:
                    lines.append('#' + mapId + '\n')
                    lines += [','.join(entry) + '\n' for entry in entries]
            f.writelines(lines)

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

    def onChoice(self, choice):
        p = self.selected.parent()
        map_id = self.selected.text(0)

        if choice == 'delete map':
            for idx, map in enumerate(self):
                if map == self.selected:
                    self.delMap(idx)

        elif choice == 'delete entry':
            p.removeChild(self.selected)

        elif choice == 'set current':
            for idx, map in enumerate(self):
                if map == self.selected:
                    self.parent.setCurrentMap(idx)

        elif choice == "change":
            map_id, ok_pressed = QInputDialogging.getText(self, "Get map currPos", "map currPos :",
                                                      QLineEdit.Normal, "")
            if ok_pressed and re.match(COORD_REG, map_id):
                map_id.replace(" ", "")
                map_id = f"map[{map_id}]"
                self.selected.setText(0, map_id)

    def onClick(self):
        index = self.selectedIndexes()[0]
        self.selected = self.itemFromIndex(index)
        self.selected_idx = index
        combo_box = QComboBox(self)
        if self.selected.text(1) == '':
            combo_box.addItem("delete map")
            combo_box.addItem("set current")
            combo_box.addItem("change")
        else:
            combo_box.addItem("delete entry")
            combo_box.addItem("highlight")
        combo_box.activated[str].connect(self.onChoice)
        combo_box.showPopup()

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