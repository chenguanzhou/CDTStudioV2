#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Main Shell of CDTStudio V2

Author: Chen Guanzhou
Emails: cgz@whu.edu.cn 
Created in: March 2018
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox, qApp, QApplication, QStatusBar, QProgressBar, QLabel, QDockWidget, QTabWidget, QFrame
from .blocks.manager import BlockManager
from model.project.manager import ProjectManager

class ShellWindow(QMainWindow):
    

    def __init__(self):
        super().__init__()
        self.project_manager = ProjectManager(self)
        self.block_manager =  BlockManager(self)

        self.init_actions()
        self.init_statusbar()
        self.init_layout()

        self.project_manager.project_created.connect(self.on_project_created)
        self.project_manager.project_loaded.connect(self.on_project_loaded)
        self.project_manager.project_saved.connect(self.on_project_saved)
        self.project_manager.project_closed.connect(self.on_project_closed)

        self.block_manager.treeView.clicked.connect(self.on_block_clicked)

        self.update_project_infomation()
        
    """
    Initialize menus and toolbars in the main shell
    """
    def init_actions(self):        
        self.resize(800, 600)        

        # Actions
        action_new = QAction('Create', self)
        action_new.setShortcut('Ctrl+N')
        action_new.setStatusTip('Create a new project')
        action_new.triggered.connect(self.project_manager.create_project)

        action_open = QAction('Open', self)
        action_open.setShortcut('Ctrl+O')
        action_open.setStatusTip('Open an existing project')
        action_open.triggered.connect(self.project_manager.open_project)

        action_save = QAction('Save', self)
        action_save.setShortcut('Ctrl+S')
        action_save.setStatusTip('Save current project')
        action_save.triggered.connect(self.project_manager.save_project)

        action_close = QAction('Close', self)
        action_close.setShortcut('Ctrl+W')
        action_close.setStatusTip('Close current project')
        action_close.triggered.connect(self.project_manager.close_project)

        action_exit = QAction('Exit', self)
        action_exit.setStatusTip('Exit app')
        action_exit.triggered.connect(qApp.quit)

        action_about_qt = QAction('About Qt', self)
        action_about_qt.triggered.connect(qApp.aboutQt)

        # Menus
        menu_bar = self.menuBar()
        project_menu = menu_bar.addMenu('&Project')
        project_menu.addAction(action_new)
        project_menu.addAction(action_open)
        project_menu.addAction(action_save)
        project_menu.addAction(action_close)
        project_menu.addSeparator()
        project_menu.addAction(action_exit)

        help_menu = menu_bar.addMenu('&Help')
        help_menu.addAction(action_about_qt)

        # Toolbars
        toolbar = self.addToolBar('Project')
        toolbar.addAction(action_new)
        toolbar.addAction(action_open)
        toolbar.addAction(action_save)
        toolbar.addAction(action_close)

    """
    Initialize the statusBar in the main shell
    """
    def init_statusbar(self):
        #Progress Bar
        self.progressbar = QProgressBar(self)        
        self.progressbar.setEnabled(False)

        statusbar = self.statusBar()
        statusbar.showMessage('Ready!')
        statusbar.addPermanentWidget(self.progressbar)
        
        
    '''
    Initialize the layouts in the main shell
    '''
    def init_layout(self):   
        # layer manager
        self.addDockWidget(Qt.LeftDockWidgetArea, self.block_manager)

        # center widget
        self.main_widget = QTabWidget(self)
        self.setCentralWidget(self.main_widget)

    '''
    Update Project Information
    '''
    def update_project_infomation(self):
        self.__update_window_title()
        self.__update_blocks()
        self.__update_general()

    def __update_window_title(self):
        if self.project_manager.project:
            self.setWindowTitle('CDTStudio V2 -- {}'.format(self.project_manager.project.name))
        else:
            self.setWindowTitle('CDTStudio V2')

    def __update_blocks(self):
        if self.project_manager.project:
            self.block_manager.load_project(self.project_manager.project)
        else:
            self.block_manager.clear()

    def __update_general(self):
        pass

    '''
    '''
    def on_project_created(self):
        # if self.project_manager.project:
        #     print (self.project_manager.project.name)
        self.update_project_infomation()

    '''
    '''
    def on_project_loaded(self):
        self.update_project_infomation()

    '''
    '''
    def on_project_saved(self):
        self.update_project_infomation()

    '''
    '''
    def on_project_closed(self):
        self.update_project_infomation()

    '''
    '''
    def on_block_clicked(self, index):
        item = self.block_manager.model.itemFromIndex(index)

        self.main_widget.clear()
        for title, widget in item.get_central_widgets(self):
            self.main_widget.addTab(widget, title)