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
from datetime import datetime

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getRelatedFile
from exercices.library.fileLib import isDate
from exercices.library.fileLib import generateTxt

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
RESUME_FILE_NAME = 'resume.txt'
RESUME_PATH = os.path.join(os.path.split(__file__)[0], RESUME_FILE_NAME)
RELATED_FILE = 'capteurs.csv'
DATE_FORMATS = ["%Y-%m-%d %H:%M:%S"]
BASE_RESUME = "Over a period of {lapsTime} from {minTime} to {maxTime}, the average values are:"



def getCSVData():
    """
    Reads and parses the related CSV file into a dictionary format.

    This function looks for a CSV file matching the `RELATED_FILE` using `getRelatedCsv()`.
    If found, it reads its content and structures it as a dictionary where each key is a column title,
    and the corresponding value is a list of entries for that column.

    :return: CSV column names as keys and lists of column data as values
    :rtype: dict
    """
    dataFile = getRelatedFile(folder=PACKAGE_REPO, wantedFile=RELATED_FILE)
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
    Processes CSV data to compute time range and averages, then writes a summary to a text file.

    This function loads CSV data via `getCSVData()`, identifies any date column to calculate
    the time span between the earliest and latest timestamps, and computes the average for all
    other numeric fields. It then formats this information and writes it into a text file
    using `generateTxt()`.
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
        resumeString += f'\n    - average {title} = {sum(values) / len(values)}'

    if not resumeString:
        resumeString = 'failed to compilate data'

    generateTxt(resumeString, RESUME_PATH)


if __name__ == '__main__':
    getResume()
