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
from exercices.library.fileLib import generateTxt
from exercices.library.fileLib import getJsonData

# ==== global ==== #
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
LOG_FILE_NAME = 'log.txt'
OUTPUT_FOLDER = os.path.join(PACKAGE_REPO, 'logs')
RESUME_PATH = os.path.join(OUTPUT_FOLDER, LOG_FILE_NAME)
RELATED_FILE = 'machine_status.json'
KEY = 'status'
VALIDATION = 'running'
RESUME = 'ID - {machine_id} [{last_check}] : {status}'


def getLog():
    """
    Reads a related JSON file and checks the value of a specific key.

    This function locates a JSON file using `getRelatedFile()`, opens and parses it,
    then retrieves the value associated with a predefined `KEY`. If the key does not exist
    or its value does not match the expected `VALIDATION` string, a formatted alert message
    is written to `RESUME_PATH`. The script stops with an error if the file or key is missing.
    """
    jsonFile = getRelatedFile(PACKAGE_REPO, RELATED_FILE)
    if not jsonFile:
        raise RuntimeError('no related json found')

    data = getJsonData(jsonFile)
    value = data.get(KEY)
    if not value:
        raise RuntimeError(f'no : {KEY} found in {jsonFile}')

    if value == VALIDATION:
        return

    generateTxt(RESUME.format(**data), RESUME_PATH)


if __name__ == "__main__":
    getLog()

