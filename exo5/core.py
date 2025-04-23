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
from datetime import datetime

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getCSVData
from exercices.library.fileLib import isDate
from exercices.library.fileLib import getFileRecursively

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
FILE_NAME = 'capteurs.csv'
EXTENSION = '.csv'
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"
DATE_FORMATS = [DATE_FORMAT]


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


def calculAverage(csvData):
    """
    Computes the average, minimum, and maximum of each list of numeric values
    in the input dictionary, and returns a formatted summary as a string.

    :param csvData: data to get info from
    :type csvData: dict[str, list[str]]

    :return: A formatted string summarizing the average, minimum, and maximum for each numeric key.
             Non-numeric entries are skipped.
    :rtype: str
    """
    statText = ''
    for title, data in csvData.items():
        if isDate(data[0], DATE_FORMATS):
            timeObjects = [datetime.strptime(x, DATE_FORMAT) for x in data]
            minTime, maxTime = min(timeObjects), max(timeObjects)
            statText += f'{title} : {maxTime - minTime} [{minTime} -> {maxTime}]\n'
            continue

        values = [float(x) for x in data]
        statText += f'{title} = {sum(values) / len(values)} [{min(values)} -> {max(values)}]\n'

    return statText.strip()
