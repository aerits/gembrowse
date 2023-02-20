import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import browse, custWidgets
from abc import ABC, abstractmethod
import os

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

class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()

 # THIS IS GUI
    def UI(self):
        histor = "e"
        e = history(histor)
        reload = QPushButton('↻')
        searchbox = QLineEdit('gemini://gemini.circumlunar.space')
        searchbutton = QPushButton('→')
        displaypage = custWidgets.ScrollLabel(self)
        backbutton = QPushButton('←')

        tabs = custWidgets.MyTabWidget(self)

        def bruh():
            browse.downloadPage(searchbox.text())
            displaypage.setText(loadPage())
            e = history(searchbox.text())
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
        grid.addWidget(tabs, 0, 1)
        grid.addWidget(backbutton, 1,1)
        grid.addWidget(reload, 1, 2)
        grid.addWidget(searchbox, 1,3)
        grid.addWidget(searchbutton, 1,4)
        grid.addWidget(displaypage, 2, 1, 4, 4)
 
        self.setLayout(grid)
        self.setGeometry(500, 100, 500, 500)
        self.setWindowTitle('gembrowse')
        self.show()

def main():
    os.remove("history.txt")
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
