"""
===============================================================================
fileName: exo5.core
scripter: angiu
creation date: 23/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import os

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getCSVData
from exercices.library.fileLib import getFileRecursively

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
FILE_NAME = 'capteurs.csv'
EXTENSION = '.csv'


def getAvailableCsv():
    """
    Recursively traverses a directory to return a dictionary of available CSV files.

    This function uses the `getFileRecursively` function to gather all files from the directory
    specified by `PACKAGE_REPO`. It then filters the files based on their extension, keeping only
    those that match the extension defined in `EXTENSION`. The returned dictionary maps the short
    name of each file (without its extension) to its full path.

    :return: names of the CSV and related fullPath
    :rtype: dict
    """
    files = getFileRecursively(PACKAGE_REPO)

    data = {}
    for item in files:
        extension = os.path.splitext(item)[-1]
        if extension != EXTENSION:
            continue

        shortName = os.path.splitext(os.path.split(item)[-1])[0]
        data[shortName] = item

    return data


def getDataFromCSVPath(chosenCSV):
    """
    get data from given csv filePath

    :param chosenCSV: file path of csv file to get info from
    :type chosenCSV: str

    :return: data from chosen CSV
    :rtype: dict
    """
    return getCSVData(filePath=chosenCSV)