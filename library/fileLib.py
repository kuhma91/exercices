"""
===============================================================================
fileName: exercises.library.fileLib
scripter: angiu
creation date: 22/04/2025
description: library related to file info and management
===============================================================================
"""
# ==== native ==== #
import os
from datetime import datetime
import platform

# ==== third ==== #

# ==== local ===== #

# ==== global ==== #
DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y.%m.%d"]

def getFileRecursively(folder):
    """
    Recursively retrieves all files from a given folder, excluding hidden and underscore-prefixed directories.

    :param folder: The root folder path to start the recursive file search from
    :type folder: str

    :return: file paths found within the folder and its eligible subdirectories
    :rtype: list
    """
    files = []
    for item in os.listdir(folder):
        itemPath = os.path.join(folder, item)
        if os.path.isfile(itemPath):
            files.append(itemPath)
            continue

        if os.path.isdir(itemPath):
            if item.startswith('.') or item.startswith('_'):
                continue

            data = getFileRecursively(itemPath)
            files.extend(data)
            continue

    return files


def isDate(data, dateFormats=None):
    """
    Checks if a given string can be interpreted as a date using known formats.

    Tries to parse the input string against a list of common date formats.
    Returns True if any format matches, otherwise returns False.

    :param data: info to check is it's a date
    :type data: str
    :param dateFormats: Optional list of date format strings (default includes common formats)
    :type dateFormats: list[str] or None

    :return: True if the string matches a known date format, False otherwise
    :rtype: bool
    """
    if not dateFormats:
        dateFormats = DATE_FORMATS

    for fmt in dateFormats:
        try:
            datetime.strptime(data, fmt)
            return True
        except ValueError:
            continue

    return False


def openFile(fileToOpen):
    """
    Opens a file with the default program based on the operating system.

    This function checks the operating system and opens the specified file
    with the associated default program (e.g., text editor for text files).

    :param fileToOpen: The path to the file to be opened
    :type fileToOpen: str
    """
    if platform.system() == "Windows":
        os.startfile(fileToOpen)  # Windows
    elif platform.system() == "Darwin":
        os.system(f"open {fileToOpen}")  # macOS
    else:
        os.system(f"xdg-open {fileToOpen}")
