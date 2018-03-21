#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Layer Manager of CDTStudio V2

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""


import sys, glob
from pathlib import Path
from PyQt5.QtCore import Qt, QObject, pyqtSignal
from PyQt5.QtWidgets import QMessageBox, qApp, QApplication, QDockWidget, QTreeView, QFileDialog
from .project import Project

class ProjectManager(QObject):
    
    project_created = pyqtSignal()
    project_loaded = pyqtSignal()
    project_saved = pyqtSignal()
    project_closed = pyqtSignal()

    def __init__(self, parent):
        super(QObject, self).__init__(parent)
        self.project = None
        
    def create_project(self):
        if self.project:
            ret = QMessageBox.information(self.parent(), self.tr("Create"), self.tr("Close current project and create a new one?"), QMessageBox.Yes, QMessageBox.No)
            if ret == QMessageBox.Yes:
                self.close_project()
            else:
                return

        dir_path = QFileDialog.getExistingDirectory(
            self.parent(), self.tr('Select an empty directory as the new project repository'))

        if dir_path and len(glob.glob('{}/*'.format(dir_path))) > 0:
            # create failed
            self.project = None
            QMessageBox.critical(
                self.parent(), self.tr('Error'), self.tr('Current directory is not empty!'))
            return

        root_path = Path(dir_path)
        self.project = Project(root_path.name, root_path)

        self.project_created.emit()

    def open_project(self):
        if self.project:
            ret = QMessageBox.information(self.parent(), self.tr("Open"), self.tr("Close current project and open a new one?"), QMessageBox.Yes, QMessageBox.No)
            if ret == QMessageBox.Yes:
                self.close_project()
            else:
                return

        dir_path = QFileDialog.getExistingDirectory(self.parent(), self.tr("Open an existing project"))        
        if dir_path:
            root_path = Path(dir_path)
            try:
                if not (root_path/'project.json').exists():
                    raise FileNotFoundError((root_path/'project.json').absolute())
                self.project = Project(root_path.name, root_path)        
                self.project.load()
                self.project_loaded.emit()
                
            except Exception as msg:
                QMessageBox.critical(self.parent(), self.tr("Error"), 
                    self.tr('Current directory is not valid!\n{}'.format(msg)))

    def save_project(self):
        if self.project:            
            self.project.save()
            self.project_saved.emit()


    def close_project(self):
        if self.project:       
            self.project = None
            self.project_closed.emit()
