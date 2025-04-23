"""
===============================================================================
fileName: exo3.main
scripter: angiu
creation date: 23/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import os
import csv
import pprint

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getRelatedFile

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
RELATED_FILE = 'capteurs.csv'


def getGraphicInfo():
    csvData = getRelatedFile(PACKAGE_REPO, RELATED_FILE)




