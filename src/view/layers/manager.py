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
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView
from ..project.project import Project

class LayerManager(QDockWidget):
    
    def __init__(self, parent):
        super().__init__('Layer Manager', parent)
        
        self.treeView = QTreeView(self)
        self.setWidget(self.treeView)
        self.model = QStandardItemModel(self)
        self.treeView.setModel(self.model)

    def load_project(self, project: Project):
        self.clear()
        self.model.appendRow(QStandardItem(project.name))

    def clear(self):
        self.model = QStandardItemModel(self)
        self.treeView.setModel(self.model)




