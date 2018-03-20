#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Main Shell of CDTStudio V2

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QAction, QMessageBox, qApp, QApplication, QStatusBar, QProgressBar, QLabel, QDockWidget, QTabWidget
from layers.manager import LayerManager

class ShellWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.init_actions()
        self.init_statusbar()
        self.init_layout()
        
    """
    Initialize menus and toolbars in the main shell
    """
    def init_actions(self):        
        self.resize(800, 600)
        self.setWindowTitle('CDTStudio V2')

        # Actions
        action_new = QAction('Create', self)
        action_new.setShortcut('Ctrl+N')
        action_new.setStatusTip('Create a new project')
        action_new.triggered.connect(lambda _:QMessageBox.information(self, 'Title', 'Create project'))

        action_open = QAction('Open', self)
        action_open.setShortcut('Ctrl+O')
        action_open.setStatusTip('Open an existing project')
        action_open.triggered.connect(lambda _:QMessageBox.information(self, 'Title', 'Open project'))

        action_close = QAction('Close', self)
        action_close.setShortcut('Ctrl+W')
        action_close.setStatusTip('Close current project')
        action_close.triggered.connect(lambda _:QMessageBox.information(self, 'Title', 'Close project'))

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
        project_menu.addAction(action_close)
        project_menu.addSeparator()
        project_menu.addAction(action_exit)

        help_menu = menu_bar.addMenu('&Help')
        help_menu.addAction(action_about_qt)

        # Toolbars
        toolbar = self.addToolBar('Project')
        toolbar.addAction(action_new)
        toolbar.addAction(action_open)
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
        # center widget
        main_widget = QTabWidget(self)
        main_widget.addTab(QLabel('haha', self), "General")
        main_widget.addTab(QLabel('haha2', self), "Map2D")

        self.setCentralWidget(main_widget)

        # layer manager
        self.addDockWidget(Qt.LeftDockWidgetArea, LayerManager())


if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    ex = ShellWindow()
    ex.showMaximized()
    sys.exit(app.exec_())