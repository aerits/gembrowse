#!/usr/bin/env python3
#i just tested some code to see if the idea would work

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

def window():
   page = open("page.txt", "r")
   app = QApplication(sys.argv)
   w = QWidget()
   b = QLabel(w)
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
   b.setText(text)
   w.setGeometry(500,500,500,500)
   b.move(50,20)
   w.setWindowTitle("gembrowse")
   w.setStyleSheet("background-color: white;")
   w.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
   window()
