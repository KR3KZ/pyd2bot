from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QHeaderView, QGroupBox, QHBoxLayout, QPushButton


class PatternView(QWidget):
    def __init__(self, mw):
        super(PatternView, self).__init__(parent=mw)
        self.mw = mw

        # main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

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
        self.buttonsLyt = QHBoxLayout()
        self.buttonsGrpBx.setLayout(self.buttonsLyt)
        self.newCatButt = QPushButton("New category")
        self.captModeButt = QPushButton("Capture mode")
        self.newCatButt.clicked.connect(self.newCategory)
        self.captModeButt.clicked.connect(self.enterCaptMode)
        self.buttonsLyt.addWidget(self.newCatButt)
        self.buttonsLyt.addWidget(self.captModeButt)
        self.layout.addWidget(self.buttonsGrpBx)

    def newCategory(self, event):
        # TODO:
        # Create folder with name of category
        # Add category to table
        # Choice of type must be in enum "resource", "mob"
        pass

    def enterCaptMode(self, event):
        # TODO:
        # After capture drop menu to choose from defined categories
        # Save captured patterns to the category folder
        pass