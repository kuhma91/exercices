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
from datetime import datetime

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getFileRecursively, DATE_FORMATS
from exercices.library.fileLib import isDate

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
RELATED_FILE = 'capteurs.csv'
DATE_FORMATS = ["%Y-%m-%d %H:%M:%S"]
BASE_RESUME = "Over a period of {lapsTime} from {minTime} to {maxTime}, the average values are:"
RESUME_FILE_NAME = 'resume.txt'


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

        titles = {}
        for i, row in enumerate(reader):
            if i == 0:
                titles = {x: name for x, name in enumerate(row)}
                continue

            if not titles:
                print('no able to define titles')
                return

            for x, info in enumerate(row):
                csvData.setdefault(titles[x], []).append(info)

    return csvData


def getResume():
    """
    Retrieves and processes CSV data, computing averages and time ranges.

    This function reads the CSV data, identifies date columns, and computes the
    time range (min and max dates) for each date field. For non-date fields, it calculates
    the average value. It returns a formatted summary string.

    :return: A summary string with time laps and average values or an error message if no data is found
    :rtype: str
    """
    csvData = getCSVData()
    if not csvData:
        print('no csv data found')
        return

    resumeString = ''
    for title, data in csvData.items():
        if isDate(data[0], DATE_FORMATS):
            timeObjects = [datetime.strptime(x, "%Y-%m-%d %H:%M:%S") for x in data]
            minTime, maxTime = min(timeObjects), max(timeObjects)
            lapsTime = maxTime - minTime
            resumeString = BASE_RESUME.format(lapsTime=str(lapsTime), maxTime=str(maxTime), minTime=str(minTime))
            continue

        values = [float(x) for x in data]
        resumeString += f'\n- average {title} = {sum(values) / len(values)}'

    if not resumeString:
        return 'failed to compilate data'

    return resumeString


def getResume():
    """
    Generates a resume string and writes it to a text file.

    This function calls `getResume()` to generate a formatted summary, then opens a file
    specified by `RESUME_FILE_NAME` in write mode and saves the resume string into it.
    """
    toPrint = getResume()
    with open(RESUME_FILE_NAME, "w") as file:
        file.write(toPrint)


if __name__ == '__main__':
    getResume()
