"""
===============================================================================
fileName: exo2.main
scripter: angiu
creation date: 23/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import os
import json
import pprint

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getRelatedFile

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
FILE_NAME = 'machine_status.json'


def getJsonData():
    jsonFile = getRelatedFile(PACKAGE_REPO, FILE_NAME)
    return json.load(open(jsonFile, 'r'))


pprint.pprint(getJsonData())
