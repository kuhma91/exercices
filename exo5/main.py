"""
===============================================================================
fileName: exo5.main
scripter: angiu
creation date: 23/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import sys
from functools import partial

# ==== third ==== #
from PySide2 import QtWidgets
from PySide2.QtGui import QStandardItemModel
from PySide2.QtGui import QStandardItem

# ==== local ===== #
from library.general.uiLib import applyStyleSheet
from library.general.uiLib import loadUi
from exercices.exo5.core import getAvailableCsv
from exercices.exo5.core import getDataFromCSVPath

# ==== global ==== #


class CsvViewer:
    def __init__(self):
        self.ui = loadUi(__file__, __class__.__name__)

        self.csvs = getAvailableCsv()

        self.storeWidget()
        self.fillUi()
        self.connectWidgets()
        applyStyleSheet(self.ui)
        self.initializeUi()

    def storeWidget(self):
        self.CSVSelecter = self.ui.CSVSelecter
        self.treeView = self.ui.treeView

    def fillUi(self):
        self.CSVSelecter.addItems(sorted(list(self.csvs.keys())))
        self.updateTreeView()

    def updateTreeView(self):
        self.treeView.setModel(None)
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)

        csvName = self.CSVSelecter.currentText()
        chosenCSV =  self.csvs[csvName]

        data = getDataFromCSVPath(chosenCSV)

        # fill columns
        rows = zip(*data.values())
        for row in rows:
            items = [QStandardItem(str(cell)) for cell in row]
            self.model.appendRow(items)

        self.model.setHorizontalHeaderLabels(list(data.keys()))  # Add header

        header = self.treeView.header()  # create header to make it stretchable
        for i in enumerate(data):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)  # Stretchable

        self.treeView.setSortingEnabled(True)  # Enable sorting by column header

    def connectWidgets(self):
        self.CSVSelecter.currentIndexChanged.connect(self.updateTreeView)

    def initializeUi(self, *args):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()

        self.ui.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    CsvViewer()
