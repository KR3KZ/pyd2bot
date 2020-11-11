from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QHeaderView, QGroupBox, QHBoxLayout, QPushButton, \
    QLineEdit, QComboBox, QTableWidgetItem, QMessageBox
from gui.custWidgets import QSnip
import os


class PatternView(QWidget):
    def __init__(self, mw):
        super(PatternView, self).__init__(parent=mw)
        self.mw = mw
        # main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.currCatDir = None

        # patterns table
        self.patternsTable = QTableWidget()
        self.patternsTable.setShowGrid(True)
        self.patternsTable.setColumnCount(2)
        self.patternsTable.resizeColumnsToContents()
        self.patternsTable.setHorizontalHeaderLabels(['name', 'type'])
        self.patternsTable.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.patternsTable.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.layout.addWidget(self.patternsTable)

        # Save button at the bottom
        self.buttonsGrpBx = QGroupBox()
        self.buttonsLyt = QVBoxLayout()
        self.buttonsGrpBx.setLayout(self.buttonsLyt)

        # Create category
        self.newCatLyt = QHBoxLayout()
        self.newCatButt = QPushButton("New category")
        self.catName = QLineEdit()
        self.catName.setPlaceholderText("Choose a name for your pattern category.")
        self.catTypeCB = QComboBox(self)
        self.catTypeCB.addItem("Resource")
        self.catTypeCB.addItem("Mob")
        self.newCatLyt.addWidget(self.newCatButt)
        self.newCatLyt.addWidget(self.catName)
        self.newCatLyt.addWidget(self.catTypeCB)
        self.layout.insertLayout(1, self.newCatLyt)

        self.captModeButt = QPushButton("Capture mode")
        self.newCatButt.clicked.connect(self.newCategory)
        self.captModeButt.clicked.connect(self.startCaptureMode)
        self.buttonsLyt.addWidget(self.captModeButt)
        self.layout.addWidget(self.buttonsGrpBx)

    def newCategory(self, event):
        if not self.catName.text():
            QMessageBox.critical(self.mw, "ERROR", "You didn't enter a name.")
        self.currCatDir = os.path.join(self.mw.patternsDir, self.catName.text())
        if not os.path.exists(self.currCatDir):
            os.mkdir(self.currCatDir)
        rowPosition = self.patternsTable.rowCount()
        self.patternsTable.insertRow(rowPosition)
        self.patternsTable.setItem(rowPosition, 0, QTableWidgetItem(self.catName.text()))
        self.patternsTable.setItem(rowPosition, 1, QTableWidgetItem(self.catTypeCB.currentText()))

    def startCaptureMode(self):
        self.mw.hide()
        self.snip_win = QSnip(self, self.currCatDir)
        self.snip_win.captureModeExited.connect(self.mw.show)
        self.snip_win.show()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F5:
            self.startCaptureMode()
        event.accept()