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
LOG_FILE_NAME = 'log.txt'
RESUME_PATH = os.path.join(os.path.split(__file__)[0], LOG_FILE_NAME)
RELATED_FILE = 'machine_status.json'
KEY = 'status'


def getJsonData():
    jsonFile = getRelatedFile(PACKAGE_REPO, RELATED_FILE)
    if not jsonFile:
        raise RuntimeError('no related json found')

    data = json.load(open(jsonFile, 'r'))
    value = data.get()
