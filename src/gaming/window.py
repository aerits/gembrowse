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

class MySignal(QtCore.QObject):
    sig_no_args = QtCore.pyqtSignal()
    sig_with_str = QtCore.pyqtSignal(str)

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
t = threading.Thread()
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
          tab_list_dictionary = {0:"New Tab"}
          tab_list = tablist.tablist(tab_list_dictionary)

          def input():
                while(running):
                    
                     # close tabs
                     item = tab_list.checkIfYouNeedToCloseIt(len(tab_list_dictionary))

                     if(item > -1):
                        #print(item)
                        #tab_list_dictionary.pop(item)
                        # move back all items in tab_list_dictionary by 1 to replace the space ethat was lost
                        for i in range(item, len(tab_list_dictionary)-1):
                          tab_list_dictionary[i] = tab_list_dictionary[i+1]
                        if(len(tab_list_dictionary) < 1):
                            os._exit(0)
                        tab_list_dictionary.pop(len(tab_list_dictionary)-1)

                     # open tabs
                     item = tab_list.checkIfYouNeedToOpenIt(len(tab_list_dictionary))
                     
                     if(item > -1):
                        tab_list_dictionary[item] = "New Tab"
                        dictionary_of_tabs[item] = tabs.tab(item)
                        signal.sig_no_args.emit()
                        #vbox.addWidget(dictionary_of_tabs[item])
                        
                     #print(tab_list_dictionary)
          # https://stackoverflow.com/questions/36453462/pyqt5-qobject-cannot-create-children-for-a-parent-that-is-in-a-different-thread
          # use this
          def makeANewTab():
            #dictionary_of_tabs[len(dictionary_of_tabs)] = tabs.tab(len(dictionary_of_tabs))
            vbox.addWidget(dictionary_of_tabs[len(dictionary_of_tabs)-1])
            print("MAKE A NEW TAB BRO")
          signal = MySignal

          signal.sig_no_args.connect(makeANewTab)
          


          t = threading.Thread(target=input)

          t.start()

          #test code that iteratively adds stuff
          #to dictionary for reference
          #for i in range(1, 10):
                #dictionary_of_tabs[i] = tabs.tab(i)

          #e = QPushButton('bruh why won\'t this work')

          #tab_list = tablist.tablist(tab_list_dictionary)

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
     app = QApplication(sys.argv)
     ex = PyQtLayout()
     #sys.exit(app.exec_())
     app.exec_()

if __name__ == '__main__':
    main()
