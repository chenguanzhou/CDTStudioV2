#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Layer Manager of CDTStudio V2

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""


import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView

class LayerManager(QDockWidget):
    
    def __init__(self):
        super().__init__('Layer Manager')
        
        self.treeView = QTreeView(self)
        self.setWidget(self.treeView)
