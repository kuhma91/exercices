"""
===============================================================================
fileName: exercise_1.main
scripter: angiu
creation date: 22/04/2025
description: read a csv file to calculate min and max values then save it in resume.txt
===============================================================================
"""
# ==== native ==== #
import csv
import os
import pprint

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getFileRecursively

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
RELATED_FILE = 'capteurs.csv'


def getRelatedCsv():
    """
    Searches for a related CSV file in the package repository.

    This function extracts the base name and extension from the global `RELATED_FILE`, then
    recursively searches through the `PACKAGE_REPO` directory for a file that matches both the
    name and extension (case-insensitive). If a match is found, the corresponding file path is returned.

    Return: The full path to the matching file if found
    :rtype: str
    """
    data = getFileRecursively(PACKAGE_REPO)
    if not data:
        print(f'no data found if : {PACKAGE_REPO}')
        return

    searchedName, wantedExtension = os.path.splitext(RELATED_FILE.lower())

    toReturn = None
    for filePath in data:
        shortName = os.path.split(filePath)[-1].lower()
        name, extension = os.path.splitext(shortName)
        if name != searchedName or extension != wantedExtension:
            continue

        toReturn = filePath
        break

    return toReturn


def getCSVData():
    """
    Reads and parses the related CSV file into a dictionary format.

    This function looks for a CSV file matching the `RELATED_FILE` using `getRelatedCsv()`.
    If found, it reads its content and structures it as a dictionary where each key is a column title,
    and the corresponding value is a list of entries for that column.

    :return: CSV column names as keys and lists of column data as values
    :rtype: dict
    """
    dataFile = getRelatedCsv()
    if not dataFile:
        print('no matching csv found')
        return

    csvData = {}
    with open(dataFile, newline='') as csvfile:
        reader = csv.reader(csvfile)

        titles = None
        for i, row in enumerate(reader):
            if i == 0:
                titles = {x: name for x, name in enumerate(row)}
                continue

            for x, info in enumerate(row):
                csvData.setdefault(titles[x], []).append(info)

    return csvData

