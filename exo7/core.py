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
import csv

# ==== third ==== #
# ==== local ===== #
from exercices.library.fileLib import getFileRecursively
from exercices.library.fileLib import getDataFromCsv

# ==== global ==== #
DATA_REPO = os.path.join(os.sep.join(__file__.split(os.sep)[:-2]), 'data')


def getCsvs():
    files = getFileRecursively(DATA_REPO)
    csvs = [x for x in files if x.endswith('.csv')]

    data = {}
    for csvFile in csvs:
        csvInfo = getDataFromCsv(csvFile)
        shortName = os.path.splitext(os.path.split(csvFile)[-1])[0]
        data[shortName] = csvInfo | {'filePath': csvFile}

    return data



