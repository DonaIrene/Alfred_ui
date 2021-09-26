import sys
from PyQt5.QtCore import Qt, center
from PyQt5.QtWidgets import (QGridLayout, QLabel, QMainWindow, QTextEdit, QToolTip,QPushButton,
     QApplication, QWidget)
from PyQt5.QtGui import QFont, QIcon
from TrueBot import treiner




class Icon(QWidget):

     def __init__(self):
         super().__init__()
         self.initUI()
     
     def initUI(self):
          inserir = QTextEdit()
          chat = QTextEdit()
          sendBtn = QPushButton('confirm')
          
          self.setGeometry(300,300,300,220)
          self.setWindowTitle('Baby Alfred')
          self.setWindowIcon(QIcon('https://www.pngfind.com/mpng/wmioTi_coroa-icon-png-crown-icon-png-transparent-png/'))
          self.show()



          grid = QGridLayout()
          grid.setSpacing(3)
          grid.addWidget(inserir, 0, 0 , 1, 3)
          grid.addWidget(chat, 1, 0, 1, 1)
          grid.addWidget(sendBtn, 1, 2,)

          self.setLayout(grid)

def main ():
     app = QApplication(sys.argv)
     ex = Icon()
     sys.exit(app.exec_())



if __name__== '__main__':
     main()