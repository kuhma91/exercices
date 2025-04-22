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

# ==== third ==== #

# ==== local ===== #

# ==== global ==== #


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
