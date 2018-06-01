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
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView, QLabel, QAction
from .baseblock import BaseBlock

class TaskBlock(BaseBlock):
    def __init__(self):
        super().__init__('Tasks')

    def get_central_widgets(self, parent):
        return [
            ('General', QLabel('test task', parent))
        ]

    def get_actions(self):
        return [
            
        ]