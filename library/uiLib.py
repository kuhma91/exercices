# ==== native ==== #
import sys
import os
import importlib.util

# ==== third ==== #
from PySide2 import QtWidgets

# ==== global ==== #


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
