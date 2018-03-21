#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Project

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""


import sys
import json
from pathlib import Path
from PyQt5.QtCore import Qt, QObject
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView

PROJECT_JSON_FILE_NAME = 'project.json'

class Project(QObject):
    

    name = ''
    path = ''
    description = ''
    
    def __init__(self, name: str = None, path: Path= None, description: str = None):
        super().__init__()
        self.name = name
        self.path = path
        self.description = description

    def load(self):
        with open(self.path/PROJECT_JSON_FILE_NAME, 'r') as pro_file:
            data = json.loads(pro_file.read())
            self.name = data['property']['name']
            self.description = data['property']['description']


    def save(self):
        with open(self.path/PROJECT_JSON_FILE_NAME, 'w') as pro_file:

            data = {
                'property':{
                    'name': self.name,
                    'description': self.description,
                },
                'metadata': {},
                'rasters': [],
                'vectors': []
            }

            pro_file.write(json.dumps(data))
    

    
        
    
