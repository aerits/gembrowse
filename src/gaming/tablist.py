#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tabs

class tablist(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)
        firsttab = QPushButton('bruh')
        hbox = QHBoxLayout()
        hbox.addWidget(firsttab)
        self.setLayout(hbox)
