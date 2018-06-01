#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Layer Manager of CDTStudio V2

Author: Chen Guanzhou
Emails: cgz@whu.edu.cn 
Created in: March 2018
"""


import sys
from PyQt5.QtCore import Qt, QModelIndex
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView
from model.project.project import Project

from .project_block import ProjectBlock
from .dataset_block import DatasetBlock
from .task_block import TaskBlock

class BlockManager(QDockWidget):
    
    def __init__(self, parent):
        super().__init__('Layer Manager', parent)
        
        self.treeView = QTreeView(self)
        self.model = QStandardItemModel(self)
        self.treeView.setModel(self.model)
        self.setWidget(self.treeView)                
        self.treeView.setEditTriggers(QTreeView.NoEditTriggers)
        self.treeView.setHeaderHidden(True)

        self.root_block = None
        self.root_dataset = None
        self.root_task = None

        

    def load_project(self, project: Project):
        self.clear()

        self.root_block = ProjectBlock(project.name)
        self.root_dataset = DatasetBlock()
        self.root_task = TaskBlock()

        self.root_block.appendRow(self.root_dataset)
        self.root_block.appendRow(self.root_task)
        self.model.appendRow(self.root_block)
        self.treeView.expandAll()

    def clear(self):
        self.root_block = None
        self.root_dataset = None
        self.root_task = None

        self.model = QStandardItemModel(self)
        self.treeView.setModel(self.model)





