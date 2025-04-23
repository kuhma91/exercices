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
import matplotlib.pyplot as plt
from datetime import datetime

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getCSVData

# ==== global ==== #
RELATED_REPO = os.path.split(__file__)[0]
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
OUTPUT_FOLDER = os.path.join(RELATED_REPO, 'graphics')
RELATED_FILE = 'capteurs.csv'
TIME_KEY = 'timestamp'
GRAPHIC_FILE_TEMPLATE = os.path.join(OUTPUT_FOLDER, '{name}.png')


def generateGraphic(name, xAxis, yAxis, show=False):
    """
    Generates and saves a line chart using the provided X and Y axis data.

    :param name: The name of the curve; used for the chart title and filename.
    :type name: str
    :param xAxis: The list of X-axis values (e.g., timestamps).
    :type xAxis: list
    :param yAxis: The list of Y-axis values corresponding to the X-axis.
    :type yAxis: list
    :param show: If True, displays the chart after saving. Default is False.
    :type show: bool
    """
    filePath = GRAPHIC_FILE_TEMPLATE.format(name=name)
    folder = os.path.split(filePath)[0]
    os.makedirs(folder, exist_ok=True)

    plt.figure()  # force new figure creation - avoid issues

    plt.plot(xAxis, yAxis, marker='o', linestyle='-', color='b')
    plt.title(f'{name} graphic')
    plt.xlabel('time')
    plt.ylabel(name)
    plt.grid(True)

    plt.xticks(rotation=45)  # Rotate the X-axis labels by 45 degrees for better readability
    plt.tight_layout()  # Automatically adjust subplot parameters to give a nice fit and prevent label cutoff

    plt.savefig(filePath, dpi=300)

    if show:
        plt.show()

def getGraphicInfo():
    """
    Reads CSV data and generates a line chart for each data series except the time key.
    """
    csvData = getCSVData(PACKAGE_REPO, RELATED_FILE)
    timeStamps = csvData.get(TIME_KEY, [])
    if not timeStamps:
        raise RuntimeError(f'"{TIME_KEY}" not in csvData')

    for name, yAxis in csvData.items():
        if name == TIME_KEY:
            continue

        if len(yAxis) != len(timeStamps):
            print(f'{name} count does not match timestamps')
            continue

        generateGraphic(name=name, xAxis=timeStamps, yAxis=[float(value) for value in yAxis])

        import pprint

        print(f'\nname={name}')
        pprint.pprint(timeStamps)
        pprint.pprint([float(value) for value in yAxis])


if __name__ == '__main__':
    getGraphicInfo()
