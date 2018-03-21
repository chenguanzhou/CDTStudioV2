#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CDTStudio V2

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""

PYQGIS_PATH = "c:/osgeo4w64/apps/qgis-dev/python"
QGIS_PLUGIN_PATH = "c:/osgeo4w64/apps/qgis-dev/plugins"

import sys, os
sys.path.append(PYQGIS_PATH)

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from qgis.core import QgsApplication, QgsProviderRegistry

from view.shell import ShellWindow

def start_app():
    QgsApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QgsApplication([], True)
    QgsProviderRegistry.instance(QGIS_PLUGIN_PATH)
    
    w = ShellWindow()
    w.showMaximized()
    
    app.exec_()
    app.exitQgis()

if __name__ == '__main__':

    start_app()