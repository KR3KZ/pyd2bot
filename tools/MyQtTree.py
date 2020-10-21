from PyQt5.QtWidgets import *
import re
from constants import *


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
        self.setHeaderLabels(["Type", "PosX", "posY", "Height", "Width"])
        self.parent = parent
        self.selected = None
        self.clicked.connect(self.onClick)

    def loadFromFile(self, file_path):
        with open(file_path, "r") as f:
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

    def delMap(self, map_id):
        for idx, name in enumerate(self.maps()):
            if map_id == name:
                self.takeTopLevelItem(idx)
                if map_id == self.parent.current_map:
                    self.parent.current_map = None
                    self.parent.updateCurrentMapInfo()

    def onChoice(self, choice):
        p = self.selected.parent()
        map_id = self.selected.text(0)
        if choice == 'delete map':
            self.delMap(map_id)
        elif choice == 'delete entry':
            p.removeChild(self.selected)
        elif choice == 'set current':
            self.parent.setCurrentMap(map_id)

    def onClick(self):
        index = self.selectedIndexes()[0]
        self.selected = self.itemFromIndex(index)
        combo_box = QComboBox(self)
        if self.selected.text(1) == '':
            combo_box.addItem("delete map")
            combo_box.addItem("set current")
        else:
            combo_box.addItem("delete entry")
            combo_box.addItem("highlight")
        combo_box.activated[str].connect(self.onChoice)
        combo_box.showPopup()

    def __getitem__(self, map_id):
        res = None
        if re.findall(MAP_REG, map_id):
            for map in self:
                if map.text(0) == map_id:
                    res = map
        if not res:
            raise KeyError('Map ID not found.')
        return res

    def getMapList(self, map_id):
        return _mapList(self[map_id])

    def __iter__(self):
        n = self.topLevelItemCount()
        for i in range(n):
            yield self.topLevelItem(i)

    def __contains__(self, map_id):
        return map_id in self.maps()