"""
===============================================================================
fileName: exo6.main
scripter: angiu
creation date: 24/04/2025
description: 
===============================================================================
"""

# ==== native ==== #
import sys
import re
from functools import partial

# ==== third ==== #
from PySide2 import QtWidgets

# ==== local ===== #
from library.general.uiLib import applyStyleSheet
from library.general.uiLib import loadUi
from exercices.exo6.core import getAvailableJson
from exercices.exo6.core import getDataFromFile
from exercices.exo6.core import saveParam
from exercices.exo6.core import PARAM_NAME

# ==== global ==== #
DIGITS_PATTERN = '^\\d+$'
ERROR_COLOR = ('150, 0, 0', '212, 212, 212')
DEFAULT_COLOR = ('63, 63, 63', '212, 212, 212')
COLOR_TEMPLATE = 'background-color: rgb({0}); color: rgb({1}); border: 4px solid rgb({0});'


class JsonParamSetter:
    def __init__(self):
        self.ui = loadUi(__file__, __class__.__name__)

        self.availableJson = getAvailableJson()

        self.storeWidget()
        self.fillUi()
        self.connectWidgets()
        applyStyleSheet(self.ui)
        self.initializeUi()

    def storeWidget(self):
        self.fileSelecter = self.ui.fileSelecter
        self.textField = self.ui.textField
        self.slider = self.ui.slider
        self.endButton = self.ui.endButton

    def connectWidgets(self):
        self.fileSelecter.currentTextChanged.connect(partial(self.fillUi))
        self.slider.sliderMoved.connect(partial(self.updateTextField))
        self.slider.valueChanged.connect(partial(self.updateTextField))
        self.textField.textChanged.connect(partial(self.updateSlider))
        self.endButton.clicked.connect(partial(self.saveCommand))

    def fillUi(self, *args):
        self.fileSelecter.addItems(sorted(list(self.availableJson.keys())))

        fileName = self.getChosenFile()
        fileData = getDataFromFile(fileName)
        value = fileData.get(PARAM_NAME, 0)

        self.slider.setValue(value)
        self.textField.setText(str(value))

    def getChosenFile(self):
        fileName = self.fileSelecter.currentText()
        return self.availableJson[fileName]

    def updateTextField(self, *args):
        value = self.slider.value()
        self.textField.setText(str(value))

    def updateSlider(self, *args):
        stringValue = self.textField.text()

        if re.match(DIGITS_PATTERN, stringValue) or not stringValue:
            toApply = COLOR_TEMPLATE.format(DEFAULT_COLOR[0], DEFAULT_COLOR[1])
            issue = False
        else:
            toApply = COLOR_TEMPLATE.format(ERROR_COLOR[0], ERROR_COLOR[1])
            issue = True

        self.textField.setStyleSheet(toApply)
        if issue or not stringValue:
            return

        numValue = int(stringValue)
        if numValue > 100:
            self.textField.setText('100')
            numValue = 100

        self.slider.setValue(numValue)

    def saveCommand(self, *args):
        value = self.slider.value()
        fileName = self.getChosenFile()
        saveParam(fileName, value)


    def initializeUi(self, *args):
        if not QtWidgets.QApplication.instance():
            app = QtWidgets.QApplication(sys.argv)
        else:
            app = QtWidgets.QApplication.instance()

        self.ui.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    JsonParamSetter()