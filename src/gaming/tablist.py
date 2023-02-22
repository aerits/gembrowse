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
        if(self.pressed==True):
            return True
        else:
            return False
    def __init__(self, name, parent=None):
        QWidget.__init__(self, parent=parent)
        tab = QPushButton(name)
        close = QPushButton('x')
        hbox = QHBoxLayout()
        hbox.addWidget(tab)
        hbox.addWidget(close)
        self.setLayout(hbox)
        close.pressed.connect(self.buttonIsPressed)

class tablist(QWidget):
    hbox = QHBoxLayout()
    tabs={}
    #numberOfTabs = 1

    #tabs[numberOfTabs-1] = tab(numberOfTabs-1)

    def __init__(self, tablistdictionary, parent=None):
        QWidget.__init__(self, parent=parent)
        #tabs = {}
        newtab = QPushButton('+')

        hbox1 = QHBoxLayout()
        hbox1.addLayout(self.hbox)
        hbox1.addWidget(newtab)

        # add tabs
        for i in range(len(tablistdictionary)):
            self.tabs[i] = tab(tablistdictionary[i])
            self.hbox.addWidget(self.tabs[i])
        self.setLayout(hbox1)

    def tabCreate(self):
        bruh3 = tab('bruh3')
        self.hbox.addWidget(bruh3)

    def tabClose(self, tab):
        self.hbox.removeWidget(tab)

    def checkIfYouNeedToCloseIt(self, tab):
        if(tab.isButtonPressed()==True):
            self.tabClose(tab)
