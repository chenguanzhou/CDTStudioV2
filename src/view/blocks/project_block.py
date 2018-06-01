#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Layer Manager of CDTStudio V2

Author: Chen Guanzhou
Emails: cgz@whu.edu.cn 
Created in: March 2018
"""


import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView, QLabel
from .baseblock import BaseBlock

class ProjectBlock(BaseBlock):
    def __init__(self, project_name):
        super().__init__(project_name)

    def get_central_widgets(self, parent):
        return [
            ('General', QLabel('test project', parent))
        ]