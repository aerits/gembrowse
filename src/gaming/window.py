import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class ScrollLabel(QScrollArea):

    # constructor
    def __init__(self, *args, **kwargs):
        QScrollArea.__init__(self, *args, **kwargs)

        # making widget resizable
        self.setWidgetResizable(True)

        # making qwidget object
        content = QWidget(self)
        self.setWidget(content)

        # vertical box layout
        lay = QVBoxLayout(content)

        # creating label
        self.label = QLabel(content)

        # setting alignment to the text
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        # making label multi-line
        self.label.setWordWrap(True)

        # adding label to the layout
        lay.addWidget(self.label)

    # the setText method
    def setText(self, text):
        # setting text to the label
        self.label.setText(text)
 
class PyQtLayout(QWidget):
 
    def __init__(self):
        super().__init__()
        self.UI()
 
    def UI(self):
        reload = QPushButton('↻')
        searchbox = QLineEdit('gemini://gemini.circumlunar.space')
        searchbutton = QPushButton('→')
        displaypage = ScrollLabel(self)
        
        page = open("page.txt", "r")

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

        displaypage.setText(text)

        grid = QGridLayout()
        grid.addWidget(reload, 0,1)
        grid.addWidget(searchbox, 0,2)
        grid.addWidget(searchbutton, 0,3)
        grid.addWidget(displaypage, 1, 1, 3, 3)
 
        self.setLayout(grid)
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('gembrowse')
        self.show()

def main():
    app = QApplication(sys.argv)
    ex = PyQtLayout()
    sys.exit(app.exec_())
 
if __name__ == '__main__':
    main()
