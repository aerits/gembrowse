import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import browse, custWidgets, tabs, tablist
from abc import ABC, abstractmethod
import os
import threading

running=True;

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
     threads = []
     t = threading.Thread(target=loadPage)
     threads.append(t)

     def __init__(self):
        super().__init__()
        self.UI()

     # THIS IS GUI
     def UI(self):
          dictionary_of_tabs = {0:tabs.tab(0)}
          tab_list_dictionary = {0:"gaming", 1:"bruh2"}
          tab_list = tablist.tablist(tab_list_dictionary)

          def input():
                while(running):
                     item = tab_list.checkIfYouNeedToCloseIt(len(tab_list_dictionary))
                     if(item > -1):
                          tab_list_dictionary.pop(item)

          t = threading.Thread(target=input)

          t.start()

          #test code that iteratively adds stuff
          #to dictionary for reference
          #for i in range(1, 10):
                #dictionary_of_tabs[i] = tabs.tab(i)

          #e = QPushButton('bruh why won\'t this work')

          #tab_list = tablist.tablist(tab_list_dictionary)
          tab_list.tabCreate()

          vbox = QVBoxLayout()
          vbox.setContentsMargins(0,0,0,0)
          #vbox.setAlignment(QtCore.Qt.AlignTop)
          vbox.addWidget(tab_list)
          vbox.addWidget(dictionary_of_tabs[0])
          self.setLayout(vbox)

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
