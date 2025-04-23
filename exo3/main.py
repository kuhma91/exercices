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
import matplotlib.pyplot as plt

# ==== third ==== #

# ==== local ===== #
from exercices.library.fileLib import getCSVData

# ==== global ==== #
RELATED_REPO = os.path.split(__file__)[0]
PACKAGE_REPO = os.sep.join(__file__.split(os.sep)[:-2])
RELATED_FILE = 'capteurs.csv'
TIME_KEY = 'timestamp'
GRAPHIC_FILE_TEMPLATE = os.path.join(PACKAGE_REPO, '{name}.png')


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
    plt.plot(xAxis, yAxis, marker='o', linestyle='-', color='b')
    plt.title(name)
    plt.xlabel('time')
    plt.ylabel(name)
    plt.grid(True)

    plt.savefig(GRAPHIC_FILE_TEMPLATE.format(name=name), dpi=300)

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

        generateGraphic(name, timeStamps, yAxis, True)


if __name__ == '__main__':
    getGraphicInfo()
