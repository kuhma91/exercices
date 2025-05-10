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
import json
import csv
from datetime import datetime
import platform

# ==== third ==== #

# ==== local ===== #

# ==== global ==== #
DATE_FORMATS = ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d", "%Y.%m.%d"]


def exportDictToJSON(data, filePath):
    """
    Exports a dictionary to a JSON file.

    :param data: The dictionary to export.
    :type data: dict
    :param filePath: The path to the JSON file where data will be saved.
    :type filePath: str
    """
    folder = os.path.split(filePath)[0]
    os.makedirs(folder, exist_ok=True)

    try:
        with open(filePath, 'w') as jsonFile:
            json.dump(data, jsonFile, indent=4)

    except Exception as e:
        raise RuntimeError(f"An error occurred while exporting data: {e}")


def generateTxt(message, filePath, skipOpen=False):
    """
    Writes a message to a specified text file and optionally opens it.

    This function creates or overwrites the file at `filePath` with the provided `message`.
    If `skipOpen` is False, the file will be opened with the default program after writing.

    :param message: The string content to write to the file
    :type message: str
    :param filePath: The full path where the file should be written
    :type filePath: str
    :param skipOpen: If True, the file will not be opened after writing. Defaults to False
    :type skipOpen: bool
    """
    folder = os.path.split(filePath)[0]
    os.makedirs(folder, exist_ok=True)

    with open(filePath, "w") as file:
        file.write(message)

    if not skipOpen:
        openFile(filePath)


def getDataFromCsv(csvPath):
    """
    Reads a CSV file and returns its content as a dictionary where keys are column headers.

    :param csvPath: Path to the CSV file.
    :type csvPath: str
    :return: Dictionary with column headers as keys and lists of column values.
    :rtype: dict
    """
    csvData = {}
    with open(csvPath, newline='') as csvfile:
        reader = csv.reader(csvfile)

        titles = {}
        for i, row in enumerate(reader):
            if i == 0:
                titles = {x: name for x, name in enumerate(row)}
                continue

            if not titles:
                raise RuntimeError('no able to define titles')

            for x, info in enumerate(row):
                csvData.setdefault(titles[x], []).append(info)

    return csvData


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


def getJsonData(jsonFile):
    """
    Safely reads and parses a JSON file.

    This function attempts to open and parse the specified JSON file.
    If successful, it returns the parsed data as a Python object.
    If the file is not readable or the JSON is malformed, it raises a RuntimeError
    with a descriptive message.

    :param jsonFile: Path to the JSON file to be read
    :type jsonFile: str
    :return: Parsed JSON data as a dictionary or list (depending on file content)
    :rtype: dict or list
    """
    try:
        with open(jsonFile, 'r') as f:
            data = json.load(f)
            return data

    except json.JSONDecodeError as e:
        raise RuntimeError(f'JSON format error in {jsonFile} : {e}')

    except Exception as e:
        raise RuntimeError(f'Failed to read {jsonFile} : {e}')


def getRelatedFile(folder, wantedFile):
    """
    Searches recursively for a file matching the given name and optionally the extension.

    This function walks through all files in the given folder and its subdirectories,
    ignoring hidden and underscore-prefixed folders. It looks for a file whose name matches
    `wantedFile` (case-insensitive, without extension) and, if specified, whose extension matches `wantedExtension`.

    :param folder: The root directory to start the search from
    :type folder: str
    :param wantedFile: File name and extension to search for
    :type wantedFile: str

    :return: The full path to the matching file if found, otherwise None
    :rtype: str or None
    """
    data = getFileRecursively(folder)
    if not data:
        print(f'no data found if : {folder}')
        return

    searchedName, wantedExtension = os.path.splitext(wantedFile.lower())

    toReturn = None
    for filePath in data:
        shortName = os.path.split(filePath)[-1].lower()
        name, extension = os.path.splitext(shortName)
        if name != searchedName or extension != wantedExtension:
            continue

        toReturn = filePath
        break

    return toReturn


def getCSVData(folder=None, fileName=None, filePath=None):
    """
    Reads and parses the related CSV file into a dictionary format.

    This function looks for a CSV file matching the `RELATED_FILE` using `getRelatedCsv()`.
    If found, it reads its content and structures it as a dictionary where each key is a column title,
    and the corresponding value is a list of entries for that column.

    :param folder: The root directory to start the search from
    :type folder: str
    :param fileName: File name and extension to search for
    :type fileName: str
    :param filePath: csv file path to get data from
    :type filePath: str

    :return: CSV column names as keys and lists of column data as values
    :rtype: dict
    """
    if not filePath:
        if not fileName or not folder:
            raise RuntimeError('not enough value given: need fileName (with extension) or direct csv Path')

        filePath = getRelatedFile(folder, filePath)
        if not filePath:
            raise RuntimeError('no matching csv found')

    else:
        extension = os.path.splitext(filePath)[-1]
        if extension != '.csv':
            raise RuntimeError('need a csv file path')


    csvData = getDataFromCsv(filePath)

    return csvData


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


def xmlToDict(root):
    """
    Converts an ElementTree element and its children into a nested dictionary.

    :param root: An ElementTree element

    :return: XML data as a nested dict
    :rtype: dict
    """
    data = {}

    children = list(root)
    if children:
        for child in children:
            child_data = xmlToDict(child)
            tag = child.tag

            # Handle multiple children with the same tag
            if tag in data:
                if isinstance(data[tag], list):
                    data[tag].append(child_data)
                else:
                    data[tag] = [data[tag], child_data]
            else:
                data[tag] = child_data
    else:
        # Handle text content
        data = root.text.strip() if root.text and root.text.strip() else None

    return data
