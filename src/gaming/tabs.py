#!/usr/bin/env python3

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import custWidgets, browse
import history

def loadPage():
     page = open("page.txt", "r")

     text=""
     # enhanced for loop
     for i in page.readlines():
         if i.startswith('###'):
             text=text+"<p><h3>"+i+"</h3></p>"
         elif i.startswith('##'):
             text=text+"<p><h2>"+i+"</h2></p>"
         elif i.startswith('#'):
             text=text+"<p><h1><u>"+i+"</u></h1></p>"
         elif i.startswith("*"):
             text=text+"<p><ul style=\"list-style-type:circle;\">"+i+"</ul></p>"
         else:
             text=text+"<p>"+i+"</p>"
     page.seek(0)
     text = text.replace('#', '')

     return text

class tab(QWidget):
     def __init__(self, id, parent=None):
          QWidget.__init__(self, parent=parent)
          self.id = id

          histor = "e"
          e = history.history(histor)
          reload = QPushButton('↻')
          searchbox = QLineEdit('gemini://gemini.circumlunar.space')
          searchbutton = QPushButton('→')
          displaypage = custWidgets.ScrollLabel(self)
          backbutton = QPushButton('←')


          def bruh():
               browse.downloadPage(searchbox.text())
               displaypage.setText(loadPage())
               e = history.history(searchbox.text())
               e.writeHistory()

          def goBackInTime():
               browse.downloadPage(e.readHistory())
               displaypage.setText(loadPage())


          searchbutton.clicked.connect(bruh)
          reload.clicked.connect(bruh)
          backbutton.clicked.connect(goBackInTime)

          bruh()

          # THIS IS A MULTIDIMENTIONAL ARRAY IN A WAY ALRIGHT
          grid = QGridLayout()
          grid.addWidget(backbutton, 1,1)
          grid.addWidget(reload, 1, 2)
          grid.addWidget(searchbox, 1,3)
          grid.addWidget(searchbutton, 1,4)
          grid.addWidget(displaypage, 2, 1, 4, 4)

          self.setLayout(grid)
