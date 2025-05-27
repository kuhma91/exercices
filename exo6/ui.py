"""
===============================================================================
fileName: exo6.ui
scripter: angiu
creation date: 24/04/2025
description: 
===============================================================================
"""
# ==== native ==== #

# ==== third ==== #
from PySide2 import QtWidgets
from PySide2 import QtCore
from PySide2.QtCore import Qt

# ==== local ===== #

# ==== global ==== #


class JsonParamSetterUi(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(JsonParamSetterUi, self).__init__(parent)
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
        csvSelectLabel.setMinimumWidth(self.uiWidth / 6)
        csvSelectLabel.setMinimumHeight(30)
        csvSelectLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        csvSelectLayout.addWidget(csvSelectLabel)
        self.fileSelecter = QtWidgets.QComboBox()
        self.fileSelecter.setMinimumWidth((self.uiWidth / 6) * 5)
        self.fileSelecter.setMinimumHeight(30)
        self.fileSelecter.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        csvSelectLayout.addWidget(self.fileSelecter)
        self.mainLayout.addLayout(csvSelectLayout)

        spacer1 = QtWidgets.QLabel('')
        spacer1.setMinimumWidth(self.uiWidth)
        spacer1.setMinimumHeight(15)
        spacer1.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addWidget(spacer1)

        menuLayout = QtWidgets.QHBoxLayout()
        paramLabel = QtWidgets.QLabel('new param : ')
        paramLabel.setMinimumWidth(self.uiWidth / 6)
        paramLabel.setMinimumHeight(30)
        paramLabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        menuLayout.addWidget(paramLabel)
        self.textField = QtWidgets.QLineEdit()
        self.textField.setMinimumWidth(self.uiWidth / 6)
        self.textField.setMinimumHeight(30)
        self.textField.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        menuLayout.addWidget(self.textField)
        self.slider = QtWidgets.QSlider(Qt.Horizontal)
        self.slider.setMinimumWidth((self.uiWidth / 6) * 4)
        self.slider.setMinimumHeight(30)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.setSingleStep(1)
        self.slider.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        menuLayout.addWidget(self.slider)
        menuLayout.setStretch(1, 1)  # QLineEdit
        menuLayout.setStretch(2, 4)  # QSlider

        self.mainLayout.addLayout(menuLayout)

        spacer2 = QtWidgets.QLabel('')
        spacer2.setMinimumWidth(self.uiWidth)
        spacer2.setMinimumHeight(15)
        spacer2.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.mainLayout.addWidget(spacer2)

        endLayout = QtWidgets.QHBoxLayout()
        spacer3 = QtWidgets.QLabel('')
        spacer3.setMinimumWidth((self.uiWidth / 4) * 3)
        spacer3.setMinimumHeight(30)
        spacer3.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        endLayout.addWidget(spacer3)
        self.endButton = QtWidgets.QPushButton('save')
        self.endButton.setMinimumWidth(self.uiWidth / 4)
        self.endButton.setMinimumHeight(30)
        self.endButton.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        endLayout.addWidget(self.endButton)

        self.mainLayout.addLayout(endLayout)