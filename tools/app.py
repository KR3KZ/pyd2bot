# -*- coding: utf-8 -*-
"""
Created on Wed May 27 15:08:49 2020
A Snipping Tool for Programmers - Thsi program enables the user to snip portions of the screen, performas text recognition on the snipped image and then either performs an automatic google search in the chosen browser or copies the text to clip board. 
@author: Stephen Worsley
"""

from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton, QAction
import tkinter as tk
import sys



class MyWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__()
        self.win_width = 340
        self.win_height = 200
        self.setGeometry(50, 50, self.win_width, self.win_height)
        self.setWindowTitle("Path generator powered by KhalidINC")

        # Menu
        # Create new action
        newAction = QAction(text='&New', parent=self)
        newAction.setStatusTip('New path')
        newAction.triggered.connect(self.newCall)

        # Create new action
        openAction = QAction(text='&Open', parent=self)
        openAction.setStatusTip('Open path')
        openAction.triggered.connect(self.openCall)

        # Create menu bar and add action
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)

        listWidget = myListWidget()

        # Resize width and height
        listWidget.resize(300, 120)

        listWidget.addItem("Item 1");
        listWidget.addItem("Item 2");
        listWidget.addItem("Item 3");
        listWidget.addItem("Item 4");

        listWidget.setWindowTitle('PyQT QListwidget Demo')
        listWidget.itemClicked.connect(listWidget.Clicked)

        listWidget.show()
        # Define buttons
        # self.searchOpen = QPushButton(self)
        # self.searchOpen.setText("new path")
        # self.searchOpen.move(10, 75)
        # self.searchOpen.setFixedSize(150, 40)
        # self.searchOpen.clicked.connect(self.newCall)

    def newCall(self):
        pass

    def openCall(self):
        pass

    def snipClicked(self):
        self.snip_win = SnipWidget(self)
        self.snip_win.show()






def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())


window()
