#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
CDTStudio V2

Author: Chen Guanzhou
Website: www.chenguanzhou.com 
Created in: March 2018
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

from view.shell import ShellWindow

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    w = ShellWindow()
    w.showMaximized()
    
    sys.exit(app.exec_())