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

    def updateTreeView(self):
        self.treeView.setModel(None)
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)

        csvName = self.CSVSelecter.currentText()
        chosenCSV =  self.csvs[csvName]

        data = getDataFromCSVPath(chosenCSV)
        headers = list(data.keys())

        self.model.setHorizontalHeaderLabels(headers)  # Add header
        for i, _ in enumerate(headers):






    def connectWidgets(self):
        self.endButton.clicked.connect(partial(self.createCommand))

    def createCommand(self, *args):
        assetType = self.typeMenu.currentText()
        givenName = self.nameMenu.text()
        if not givenName.strip():
            print('no name given')
            return

        assetName = formatString(givenName, 'PascalCase')
        generateAsset(assetName, assetType)


    def initializeUi(self, *args):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()

        self.ui.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    CsvViewer()
