# ==== native ==== #
import sys
import os
import importlib.util

# ==== third ==== #
from PySide2 import QtWidgets

# ==== global ==== #
STYLE_SHEET = {
    'QPushButton': "background-color: rgb(85, 85, 85); color: rgb(212, 212, 212); border: 4px solid rgb(85, 85, 85)",
    'QLabel': "color: rgb(212, 212, 212);",
    'QCheckBox': "color: rgb(212, 212, 212);",
    'QLineEdit': "background-color: rgb(63, 63, 63); color: rgb(212, 212, 212); border: 4px solid rgb(63, 63, 63)",
    'QLineEditSpe': "background-color: rgb(45, 45, 45); color: rgb(212, 212, 212); border: 4px solid rgb(45, 45, 45)"
}
OTHER_WIDGETS = "background-color: rgb(63, 63, 63); color: rgb(212, 212, 212); border: 4px solid rgb(63, 63, 63)"


def applyStyleSheet(ui=None, widgets=None, special=False):
    """
    Apply default color on ui

    :param ui: qMainWidow to apply styleSheet on
    :type ui: widget
    """
    if not ui and not widgets:
        return

    if ui:
        ui.setStyleSheet(f"background-color: rgb(45, 45, 45);")

    if not widgets:
        if not ui:
            print('no given UI or widgets')
            return

        buttons = [x for x in ui.findChildren(QtWidgets.QPushButton)]
        texts = [x for style in [ui.findChildren(QtWidgets.QLabel), ui.findChildren(QtWidgets.QCheckBox)] for x in style]
        other = [widget for widget in ui.findChildren(QtWidgets.QWidget)
                 if widget not in texts and widget not in buttons]
        widgets = [widget for widgets in [buttons, texts, other] for widget in widgets]

    for widget in widgets:
        widgetType = widget.__class__.__name__
        if widgetType.endswith('Layout'):
            continue

        if special:
            toApply = STYLE_SHEET.get(f'{widgetType}Spe', None) or STYLE_SHEET.get(widgetType, None) or OTHER_WIDGETS
        else:
            toApply = STYLE_SHEET.get(widgetType, None) or OTHER_WIDGETS

        widget.setStyleSheet(toApply)


def loadUi(mainModule, className):
    """load ui module related to given mainModule file path

    :param mainModule: package main module file path
    :type mainModule: str
    :param className: name of class to launch
    :type className: str

    :return: ui
    :rtype: module
    """
    baseFolder = os.path.split(mainModule)[0]
    uiFile = os.path.join(baseFolder, 'ui.py')

    spec = importlib.util.spec_from_file_location(f'{className}Ui', uiFile)
    uiModule = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(uiModule)

    toLaunch = getattr(uiModule, f'{className}Ui', None)
    if toLaunch is None:
        print(f'not found : {className}Ui')
        return

    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)

    try:
        uiInstance = toLaunch()
    except Exception as e:
        print(f"Error while instancing : {e}")
        raise

    return uiInstance
