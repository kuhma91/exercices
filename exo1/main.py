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
from exercices.library.fileLib import isDate
from exercices.library.fileLib import generateTxt
from exercices.library.fileLib import getCSVData

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
RESUME_FILE_NAME = 'resume.txt'
OUTPUT_FOLDER = os.path.join(os.path.split(__file__)[0], 'resumes')
RESUME_PATH = os.path.join(OUTPUT_FOLDER, RESUME_FILE_NAME)
RELATED_FILE = 'capteurs.csv'
DATE_FORMATS = ["%Y-%m-%d %H:%M:%S"]
BASE_RESUME = "Over a period of {lapsTime} from {minTime} to {maxTime}, the average values are:"


def getResume():
    """
    Processes CSV data to compute time range and averages, then writes a summary to a text file.

    This function loads CSV data via `getCSVData()`, identifies any date column to calculate
    the time span between the earliest and latest timestamps, and computes the average for all
    other numeric fields. It then formats this information and writes it into a text file
    using `generateTxt()`.
    """
    csvData = getCSVData(PACKAGE_REPO, RELATED_FILE)
    if not csvData:
        raise RuntimeError('no csv data found')

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
