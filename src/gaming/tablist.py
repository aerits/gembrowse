#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tabs

class tab(QWidget):
    pressed = False
    def buttonIsPressed(self):
        pressed=True
        print("bruh")
    def isButtonPressed(self):
        if(pressed==True):
            print("true")
            return True
        else:
            print("false")
            return False
    def __init__(self, name, parent=None):
        QWidget.__init__(self, parent=parent)
        tab = QPushButton(name)
        close = QPushButton('x')
        hbox = QHBoxLayout()
        hbox.addWidget(tab)
        hbox.addWidget(close)
        self.setLayout(hbox)
        e = close.pressed.connect(self.buttonIsPressed)

class tablist(QWidget):
    hbox = QHBoxLayout()
    #tabs={}
    #numberOfTabs = 1

    #tabs[numberOfTabs-1] = tab(numberOfTabs-1)

    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        newtab = QPushButton('+')
        bruh = tab('bruh')
        self.hbox.addWidget(newtab)
        self.hbox.addWidget(bruh)
        self.setLayout(self.hbox)

        #bruh.close.pressed.connect(tabClose(bruh))

    def tabCreate(self):
        bruh2 = tab('bruh2')
        self.hbox.addWidget(bruh2)

    def tabClose(self, tab):
        self.hbox.removeWidget(tab)
