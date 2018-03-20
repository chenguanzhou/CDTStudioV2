#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Layer Manager of CDTStudio V2

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""


import sys
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView

class ProjectManager(QObject):
    
    def __init__(self):
        super().__init__()
        
    def create_project_request()
