"""
===============================================================================
fileName: exo4.main
scripter: angiu
creation date: 23/04/2025
description: 
===============================================================================
"""
# ==== native ==== #
import xml.etree.ElementTree as ET
import os

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import exportDictToJSON
from exercices.library.fileLib import getRelatedFile
from exercices.library.fileLib import xmlToDict

# ==== global ==== #
PACKAGE_FOLDER = os.sep.join(__file__.split(os.sep)[:-2])
RELATED_FILE = 'config_machine.xml'
RELATED_REPO = os.path.split(__file__)[0]
OUTPUT_FOLDER = os.path.join(RELATED_REPO, 'report')
REPORT_FILE_PATH = os.path.join(OUTPUT_FOLDER, 'report.json')


def getDataFromXML():
    """
    Reads and parses an XML file, converting its contents into a nested dictionary.

    This function locates the XML file based on the `RELATED_FILE` name in the given folder (`PACKAGE_FOLDER`).
    It then parses the XML using `ElementTree`, extracting the root element and recursively converting
    the XML structure into a dictionary format using `xmlToDict()`.

    :return: A dictionary representing the XML structure, where the root element tag is the key
             and the parsed data is the value.
    :rtype: dict
    """
    xmlPath = getRelatedFile(PACKAGE_FOLDER, RELATED_FILE)
    if not xmlPath:
        raise RuntimeError(f'no {RELATED_FILE} found in {PACKAGE_FOLDER}')

    tree = ET.parse(xmlPath)
    root = tree.getroot()
    data = {root.tag: xmlToDict(root)}
    exportDictToJSON(data, REPORT_FILE_PATH)


if __name__ == "__main__":
    getDataFromXML()
