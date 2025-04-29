"""
===============================================================================
fileName: main
scripter: angiu
creation date: 27/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import os
import pprint

# ==== third ==== #
from exercices.library.fileLib import getFileRecursively
from exercices.library.fileLib import getCSVData

# ==== local ===== #

# ==== global ==== #
PACKAGE_FOLDER = os.sep.join(__file__.split(os.sep)[:-2])
EXTENSION = '.csv'


def getCSVs():
    files = getFileRecursively(PACKAGE_FOLDER)

    csvs = []
    for item in files:
        extension = os.path.splitext(item)[-1]
        if extension != EXTENSION:
            continue

        csvs.append(item)

    return csvs


def readCsv():
    csvs = getCSVs()

    data = {}
    for i, filePath in enumerate(csvs):
        containedIn = getCSVData(filePath=filePath)
        for k, v in containedIn.items():
            data.setdefault(k, {}).setdefault(filePath, []).append(v)

    return data


if __name__ == "__main__":
    readCsv()
