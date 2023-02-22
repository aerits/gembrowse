import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import browse, custWidgets, tabs
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
        e = tabs(self)

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
