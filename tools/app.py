# -*- coding: utf-8 -*-
from snippetWidget import QSnip
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


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
        self.button_group_box = QGroupBox()
        self.button_layout = QHBoxLayout()
        self.button_group_box.setLayout(self.button_layout)
        self.main_layout.addWidget(self.button_group_box)

        self.path_file = None
        self.initGui()

    def initGui(self):
        # menu
        self.initMenu()

        # message label
        self.notification_text = QLabel()
        self.setMessage("Press F5 to capture region.")

        self.vLayout.addWidget(self.notification_text)

        # save button
        save_button = QPushButton("save path")
        save_button.clicked.connect(self.savePath)

        # delete last
        delete_last_button = QPushButton("delete last")
        delete_last_button.clicked.connect(self.deleteLast)

        # capture region
        capture_button = QPushButton("capture mode")
        capture_button.clicked.connect(self.startCaptureMode)
        capture_button.clicked.connect(self.startCaptureMode)

        self.button_layout.addWidget(save_button)
        self.button_layout.addWidget(delete_last_button)
        self.button_layout.addWidget(capture_button)

        # path show in a list
        self.path_list = None
        self.initPath()
        # path_list.itemClicked.connect(path_list.Clicked)

    def savePath(self):
        if not self.path_file:
            self.path_file = QFileDialog.getSaveFileName()[0]
        with open(self.path_file, 'w') as f:
            path_list = self.getPathAsList()
            lines = [', '.join(r) for r in path_list]
            f.writelines(lines)

    def getPathAsList(self):
        result = []
        n = self.path_list.topLevelItemCount()
        for i in range(n):
            step = self.path_list.topLevelItem(i)
            m = step.columnCount()
            row = [step.text(k) for k in range(m)]
            result.append(row)
        return result

    def deleteLast(self):
        n = self.path_list.topLevelItemCount()
        self.path_list.takeTopLevelItem(n - 1)

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
        self.setMessage(f"Press F5 to capture region.\n"
                        f"You are working on file : {self.path_file}")

    def initPath(self):
        if self.path_list:
            self.path_list.deleteLater()
        self.path_list = QTreeWidget(self)
        self.path_list.setColumnCount(5)
        self.path_list.setHeaderLabels(["Type", "PosX", "posY", "Height", "Width"])
        self.vLayout.addWidget(self.path_list)

    def openPath(self, event):
        self.path_file = QFileDialog.getOpenFileName()[0]
        self.initPath()
        if self.path_file:
            with open(self.path_file, "r") as f:
                for l in f.readlines():
                    if l and not l.startswith('#'):
                        step = l.split(',')
                        QTreeWidgetItem(self.path_list, step)
            self.setMessage(f"Press F5 to capture region.\n"
                            f"You are working on file : {self.path_file}")

    def startCaptureMode(self):
        stypes = ["mapChange",
                  "kralamoure",
                  "poisskaille",
                  "poissonPane",
                  "sardineBrillante"]
        self.hide()
        self.snip_win = QSnip(self, stypes)
        self.snip_win.snippetTaken.connect(self.appendPath)
        self.snip_win.captureModeExited.connect(self.show)
        self.snip_win.show()

    def setMessage(self, text):
        self.notification_text.setText(text)
        self.notification_text.adjustSize()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            self.startCaptureMode()
        event.accept()

    def appendPath(self, snippet):
        print(snippet)
        snippet = map(str, snippet)
        if self.path_file:
            QTreeWidgetItem(self.path_list, snippet)
        else:
            QMessageBox.critical(self, "ERROR", "You didn't load any path file.")



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
