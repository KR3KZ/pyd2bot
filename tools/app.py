# -*- coding: utf-8 -*-
from snippetWidget import QSnip
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction, QFileDialog


class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.setWindowTitle("Dofus Bot Path generator")
        self.setGeometry(100, 100, 200, 100)
        self.path_file = None
        self.notification_text = QLabel(self)
        self.notification_text.move(20, 50)
        self.set_notification("Press F5 to capture.")
        self.initMenu()

    def initMenu(self):
        # Create new action
        newAction = QAction(text='&New', parent=self)
        newAction.setStatusTip('New path')
        newAction.triggered.connect(self.newPathCall)

        # Create new action
        openAction = QAction(text='&Open', parent=self)
        openAction.setStatusTip('Open path')
        openAction.triggered.connect(self.openPathCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)

    def newPathCall(self):
        path_file = QFileDialog.getOpenFileName()[0]
        self.path_file = open(path_file, "w+")

    def openPathCall(self, event):
        path_file = QFileDialog.getOpenFileName()[0]
        self.path_file = open(path_file, "a+")

    def callSnippetTool(self):
        self.snip_win = QSnip(self)
        self.snip_win.snippetTaken.connect(self.appendPath)
        self.snip_win.show()

    def set_notification(self, text):
        self.notification_text.setText(text)
        self.notification_text.adjustSize()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            self.callSnippetTool()
        event.accept()

    def appendPath(self, snippet):
        print(snippet)


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
