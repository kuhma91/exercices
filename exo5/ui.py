"""
===============================================================================
fileName: exo5.ui
scripter: angiu
creation date: 23/04/2025
description: 
===============================================================================
"""
# ==== native ==== #

# ==== third ==== #
from PySide2 import QtWidgets
from PySide2 import QtCore

# ==== local ===== #

# ==== global ==== #


class CsvViewerUi(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(CsvViewerUi, self).__init__(parent)
        self.uiName = __class__.__name__.split('Ui')[0]

        self.uiWidth = 500
        self.uiMenus = {}
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle(self.uiName)
        self.setMinimumWidth(self.uiWidth + 45)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowCloseButtonHint)

        self.mainLayout = QtWidgets.QVBoxLayout(self)

        csvSelectLayout = QtWidgets.QHBoxLayout()
        csvSelectLabel = QtWidgets.QLabel('available files :')
        csvSelectLabel.setMinimumWidth(self.uiWidth / 3)
        csvSelectLabel.setMinimumHeight(30)
        csvSelectLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        csvSelectLayout.addWidget(csvSelectLabel)
        self.CSVSelecter = QtWidgets.QComboBox()
        self.CSVSelecter.setMinimumWidth((self.uiWidth / 3) * 2)
        self.CSVSelecter.setMinimumHeight(30)
        self.CSVSelecter.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        csvSelectLayout.addWidget(self.CSVSelecter)
        self.mainLayout.addLayout(csvSelectLayout)

        spacer1 = QtWidgets.QLabel('')
        spacer1.setMinimumWidth(self.uiWidth)
        spacer1.setMinimumHeight(15)
        spacer1.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addWidget(spacer1)

        self.treeView = QtWidgets.QTreeView()
        self.mainLayout.addWidget(self.treeView)

        self.statsLabel = QtWidgets.QLabel()
        self.statsLabel.setWordWrap(True)
        self.mainLayout.addWidget(self.statsLabel)