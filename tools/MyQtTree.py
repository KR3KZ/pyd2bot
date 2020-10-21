from PyQt5.QtWidgets import *


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
                if line and not line.startswith('#'):
                    step = line.split(',')
                    QTreeWidgetItem(current, step)
                else:
                    current = QTreeWidgetItem(self, [line[1:]])

    def saveToFile(self, file_path):
        with open(file_path, 'w') as f:
            lines = []
            for mapId, entries in self.items():
                print(mapId, entries)
                lines.append('#' + mapId)
                lines += [','.join(entry) for entry in entries]
            f.writelines(lines)

    def __getitem__(self, mapId):
        if mapId.startsWith("map["):
            for id, item in self.items():
                if id == mapId:
                    return item
        else:
            raise KeyError('Map Id not found.')

    def __iter__(self):
        n = self.topLevelItemCount()
        for i in range(n):
            yield self.topLevelItem(i)

    def items(self):
        for item in self:
            yield item.text(0), _mapList(item)

    def maps(self):
        for item in self:
            yield item.text(0)

    def delMap(self, mapId):
        for idx, name in enumerate(self.maps()):
            if mapId == name:
                self.takeTopLevelItem(idx)

    def onChoice(self, choice):
        if choice == 'delete map':
            self.delMap(self.selected.text(0))

        elif choice == 'delete entry':
            p = self.selected.parent()
            p.removeChild(self.selected)

        elif choice == 'set current':
            self.parent.current_map = self.selected

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

        combo_box.addItem("highlight")
        combo_box.activated[str].connect(self.onChoice)
        combo_box.showPopup()



