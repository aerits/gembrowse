#!/usr/bin/env python3
import sys
import os
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
    tabOpen=False
    numberOfTabs = 2

    #tabs[numberOfTabs-1] = tab(numberOfTabs-1)

    def __init__(self, tablistdictionary, parent=None):
        QWidget.__init__(self, parent=parent)
        #tabs = {}
        self.newtab = QPushButton('+')

        hbox1 = QHBoxLayout()
        hbox1.addLayout(self.hbox)
        hbox1.addWidget(self.newtab)

        # add tabs
        for i in range(len(tablistdictionary)):
            self.tabs[i] = tab(tablistdictionary[i])
            self.hbox.addWidget(self.tabs[i])
        self.setLayout(hbox1)
        #self.tabClose(self.tabs[0])

        self.newtab.pressed.connect(self.tabCreate)

    def tabCreate(self):
        self.numberOfTabs+=1
        self.tabs[self.numberOfTabs-1] = tab('New Tab')
        self.hbox.addWidget(self.tabs[self.numberOfTabs-1])

    def tabClose(self, i):
        #self.tabs[i].deleteLater()
        self.numberOfTabs-=1
        self.hbox.removeWidget(self.tabs[i])
        sip.delete(self.tabs[i])
        self.tabs[i] = None

    def checkIfYouNeedToCloseIt(self, numOfTabs):
        isATabClosed = [False, -1]
        for tabNumber in range(0, numOfTabs):
            #print(self.tabs)
            try:
                if(self.tabs[tabNumber].pressed=="pressed"):
                    self.tabClose(tabNumber)
                    #print(tabNumber)
                    self.tabs.pop(tabNumber)
                    for secondTabNumber in range(tabNumber, numOfTabs-1):
                        self.tabs[secondTabNumber] = self.tabs[secondTabNumber+1]
                    if(numOfTabs < 2):
                        os._exit(0)
                    #self.tabs.pop(tabNumber)
                    isATabClosed = [True, tabNumber]

            except:
                #print("error? key error probably")
                pass

        if(isATabClosed[0]==True):
            return isATabClosed[1]
        else:
            return -1

    def checkIfYouNeedToOpenIt(self, numOfTabs):
        if(numOfTabs < self.numberOfTabs):
            #print(self.tabs)
            return self.numberOfTabs-1
        else:
            return -1
