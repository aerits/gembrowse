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

# old signal code remove later replaced with worker and qthreads and stuff
class MySignal(QtCore.QObject):
    sig_no_args = QtCore.pyqtSignal()
    sig_with_str = QtCore.pyqtSignal(str)

def loadPage():
     page = open("page.txt", "r")

     text=""
     # enhanced for loop
     # this goes through the page.txt and formats it with html
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
    #initialize multithreading variables
     threads = []
     t = threading.Thread(target=loadPage)
     threads.append(t)
     signal = MySignal

     def __init__(self):
        super().__init__()
        self.UI()

     # THIS IS GUI
     def UI(self):
          #create variables for the collections for tabs
          self.dictionary_of_tabs = {0:tabs.tab(0)}
          self.tab_list_dictionary = {0:"New Tab"}
          self.tab_list = tablist.tablist(self.tab_list_dictionary)
          # https://stackoverflow.com/questions/36453462/pyqt5-qobject-cannot-create-children-for-a-parent-that-is-in-a-different-thread
          # use this
          # nevermind, actually create qtimers
          # nevermind, create qthreads instead of pythons built in things to use
          # qtimers in another thread
          # im not sure if i will be able to actually implement all of this today so ehh
          def makeANewTab():
            #dictionary_of_tabs[len(dictionary_of_tabs)] = tabs.tab(len(dictionary_of_tabs))
            # temp code that should just add the tab to the same container
            # and show both the tab you were on and the tab you just made
            vbox.addWidget(self.dictionary_of_tabs[len(self.dictionary_of_tabs)-1])
            print("MAKE A NEW TAB BRO")
          
          #multi threading things
          self.thread = QThread()

          self.worker = self.Worker()

          self.worker.moveToThread(self.thread)

          self.thread.started.connect(self.worker.run)
          self.thread.finished.connect(self.worker.finished)

          self.thread.start()


          # [[old threading code]]
          #self.timer=QTimer(self)
          #self.timer.timeout.connect(makeANewTab)

          #self.t = threading.Thread(target=input)
          #self.t.daemon = True
          #self.t.start()

          #test code that iteratively adds stuff
          #to dictionary for reference
          #for i in range(1, 10):
                #dictionary_of_tabs[i] = tabs.tab(i)

          #e = QPushButton('bruh why won\'t this work')

          #tab_list = tablist.tablist(tab_list_dictionary)

          # create a vertical layout
          vbox = QVBoxLayout()
          vbox.setContentsMargins(0,0,0,0)
          #vbox.setAlignment(QtCore.Qt.AlignTop)
          
          # put the tab list and the page into the layout
          vbox.addWidget(self.tab_list)
          vbox.addWidget(self.dictionary_of_tabs[0])
          self.setLayout(vbox)

          self.setGeometry(500, 100, 500, 500)
          self.setWindowTitle('gembrowse')
          self.show()

     class Worker(QObject):
        finished = pyqtSignal()

        # tell the main thread that there needs to be a new tab
        def sendTabSignal(self):
            self.finished.emit()

        # check if a new tab needs to be created or deleted
        def run(self):
            while(running):
        
              # close tabs
              item = self.self.tab_list.checkIfYouNeedToCloseIt(len(self.tab_list_dictionary))

              if(item > -1):
                #print(item)
                #tab_list_dictionary.pop(item)
                # move back all items in tab_list_dictionary by 1 to replace the space ethat was lost
                for i in range(item, len(self.tab_list_dictionary)-1):
                  self.tab_list_dictionary[i] = self.tab_list_dictionary[i+1]
                  if(len(self.tab_list_dictionary) < 1):
                    os._exit(0)
                  self.tab_list_dictionary.pop(len(self.tab_list_dictionary)-1)

                # open tabs
                item = self.tab_list.checkIfYouNeedToOpenIt(len(self.tab_list_dictionary))
                     
                if(item > -1):
                  self.tab_list_dictionary[item] = "New Tab"
                  self.dictionary_of_tabs[item] = tabs.tab(item)
                  sendTabSignal()

                  # [[old threading code]]
                  #self.timer.start(0)
                  #signal.sig_no_args.emit()
                  #vbox.addWidget(dictionary_of_tabs[item])
                        
                  #print(tab_list_dictionary)

def main():
     app = QApplication(sys.argv)
     ex = PyQtLayout()
     #sys.exit(app.exec_())
     app.exec_()
     #PyQtLayout.t.terminate()

if __name__ == '__main__':
    main()
