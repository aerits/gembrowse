#!/usr/bin/env python3
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tabs
import sip

class tab(QWidget):
    def buttonIsPressed(self):
        self.pressed="pressed"

    def __init__(self, name, parent=None):
        QWidget.__init__(self, parent=parent)
        self.pressed = 'notPressed'
        tabButton = QPushButton(name)
        close = QPushButton('x')
        hbox = QHBoxLayout()
        hbox.addWidget(tabButton)
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
        #self.tabClose(self.tabs[0])

    def tabCreate(self):
        self.tabs[2] = tab('bruh3')
        self.hbox.addWidget(self.tabs[2])

    def tabClose(self, i):
        #self.tabs[i].deleteLater()
        self.hbox.removeWidget(self.tabs[i])
        sip.delete(self.tabs[i])
        self.tabs[i] = None

    def checkIfYouNeedToCloseIt(self, numOfTabs):
        for i in range(numOfTabs):
            if(self.tabs[i].pressed=="pressed"):
                self.tabClose(i)
