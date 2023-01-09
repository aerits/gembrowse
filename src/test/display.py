#!/usr/bin/env python3
#i just tested some code to see if the idea would work
#scuffed code i will probably replace most of later

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   # open up the page
   page = open("page.txt", "r")

   # create qt stuff
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)

   # format the text to go into the qlabel
   text=""
   for i in page.readlines():
      if i.startswith('###'):
         text=text+"<p>"+"<h3>"+i+"</h3>"+"</p>"
      elif i.startswith('##'):
         text=text+"<p>"+"<h2>"+i+"</h2>"+"</p>"
      elif i.startswith('#'):
         text=text+"<p>"+"<h1>"+"<u>"+i+"</u>"+"</h1>"+"</p>"
      else:
         text=text+"<p>"+i+"</p>"
      page.seek(0)
   text = text.replace('#', '')

   # put the text into the qlabel
   b.setText(text)

   # set size of window
   w.setGeometry(500,500,500,500)

   # move the text to the right slightly
   b.move(50,20)

   # self explanatory
   w.setWindowTitle("gembrowse")
   w.setStyleSheet("background-color: white;")

   # show window
   w.show()

   # close app when you hit the x
   sys.exit(app.exec_())


window()
