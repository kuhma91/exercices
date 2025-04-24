"""
===============================================================================
fileName: exo6.core
scripter: angiu
creation date: 24/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import os
import re
import pprint

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getFileRecursively
from exercices.library.fileLib import getJsonData
from exercices.library.fileLib import exportDictToJSON

# ==== global ==== #
PACKAGE_FOLDER = os.sep.join(__file__.split(os.sep)[:-2])
EXTENSION = '.json'
EXO_PATTERN = '(?P<exoName>(exo\\d*))'
PARAM_NAME = 'newParam'


def getAvailableJson():
    """
    Recursively scans the package root directory to find all available `.json` files
    that are not located within directories matching the pattern 'exoX' (e.g., 'exo1', 'exo2').

    :return: base name of each `.json` file and related filePath.
    :rtype: dict
    """
    files = getFileRecursively(PACKAGE_FOLDER)

    data = {}
    for filePath in files:
        extension = os.path.splitext(filePath)[-1]
        if extension != EXTENSION:
            continue

        exo = [part for part in filePath.split(os.sep) if re.match(EXO_PATTERN, part)]
        if exo:
            continue

        shortName = os.path.splitext(os.path.split(filePath)[-1])[0]
        data[shortName] = filePath

    return data


def getDataFromFile(chosenFile):
    """
    Loads and returns data from a given JSON file.

    :param chosenFile: Path to the JSON file to read.
    :type chosenFile: str

    :return: Parsed data from the JSON file.
    :rtype: dict
    """
    return getJsonData(chosenFile)


def saveParam(fileName, value):
    data = getJsonData(fileName)
    data[PARAM_NAME] = value
    exportDictToJSON(data, fileName)


if __name__ == "__main__":
    pprint.pprint(getAvailableJson())
