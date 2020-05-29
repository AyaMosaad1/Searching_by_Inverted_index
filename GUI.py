import sys
import time
import os.path
from trie import *
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *


T = Trie()
output = list()
fileName = " "
# -----------------------------------initialize a window-----------------------
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # ----------------main window-----------------
        self.setGeometry(200, 100, 1000, 470)
        self.setStyleSheet('background-color: rgb(255,255,255)')
        self.setWindowTitle('Searching_Engine')
        self.setWindowIcon(QtGui.QIcon('search.png'))

        # ----------------------- "image"-select folder  -----------------------------
        self.label = QLabel(self)
        self.label.setGeometry(60, 80, 170, 170)
        pixmap = QPixmap('fin.png')
        self.label.setPixmap(pixmap)

        # -----------------------input text area for enter the searching word -----------------------------
        self.b = QPlainTextEdit(self)
        self.b.setGeometry(305, 200, 210, 36)
        self.b.setStyleSheet("background-color:rgb(255,255,255);\n"
                             "color: rgb(33,36,45);\n"
                             "border-style: outset;\n"
                             "border-width:1px;\n"
                             "border-radius:5px;\n"
                             "border-color:rgb(33,36,45);\n"
                             "padding :6px;\n"
                             "min-width:10px;\n")
        self.b.textChanged.connect(self.getText)
        self.b.setPlaceholderText("Enter the word")



        # ----------------info "Browse one step" button-----------------
        self.info = QPushButton('Browse folder', self)
        self.info.setGeometry(30, 260, 220, 38)
        self.info.setFont(QFont('Arial', 10))
        self.info.setStyleSheet("background-color:rgb(33,36,45);\n"
                                "color: white;\n"
                                "border-style: outset;\n"
                                "border-width:0px;\n"
                                "border-radius:5px;\n"
                                "padding :6px;\n"
                                "min-width:10px;\n")
        self.info.clicked.connect(self.getInfo)

        # -----------------Search button-----------------
        self.runB = QPushButton('Search', self)
        self.runB.setGeometry(300, 260, 220, 38)
        self.runB.setFont(QFont('Arial', 10))
        self.runB.setStyleSheet("background-color:rgb(33,36,45);\n"
                                "color: white;\n"
                                "border-style: outset;\n"
                                "border-width:0px;\n"
                                "border-radius:5px;\n"
                                "padding :6px;\n"
                                "min-width:10px;\n")
        # when run it
        self.runB.clicked.connect(self.run)



        #display output files
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(560, 20, 400, 400))
        self.listWidget.setStyleSheet("background-color:rgb(255,255,255);\n")
        self.listWidget.itemClicked.connect(self.Clicked)
        # -----------------Progress widget-----------------
        # main widget
        self.progressWidget = QtWidgets.QWidget(self)
        self.progressWidget.setGeometry(QtCore.QRect(300, 135, 400, 170))
        self.progressWidget.setObjectName("progressWidget")
        self.progressWidget.setStyleSheet('background-color: rgb(33,36,45);\n'
                                          'color: rgb(255,255,255);\n'
                                          "border: 2px solid ;\n"
                                          "border-color:rgb(249,219,210);\n")
        # progrees text
        self.prog = QPlainTextEdit(self.progressWidget)
        self.prog.setGeometry(180, 70, 200, 36)
        self.prog.setFont(QFont('Arial', 14))
        self.prog.setStyleSheet("background-color:rgb(33,36,45);\n"
                                "border: 0px solid ;\n"
                                "color: rgb(255,255,255);\n")
        self.prog.setReadOnly(True)

        # label
        self.progresslabel = QLabel(self.progressWidget)
        self.progresslabel.setGeometry(140, 100, 200, 40)
        self.progresslabel.setFont(QFont('Arial', 12))
        self.progresslabel.setText("Loading files ....")
        self.progresslabel.setStyleSheet("background-color:rgb(33,36,45);\n"
                                         "border: 0px solid ;\n")
        self.progressWidget.hide()

        # ---------------------display file content--------------------------------

        self.fileWidget = QtWidgets.QWidget(self)
        self.fileWidget.setGeometry(QtCore.QRect(300, 120, 450, 240))
        self.fileWidget.setObjectName("fileWidget")
        self.fileWidget.setStyleSheet('background-color: white;\n'
                                          "border: 1px solid ;\n"
                                          "border-color:rgb(33,36,45);\n")
        self.btnclose = QPushButton(self.fileWidget)
        self.btnclose.setGeometry(427, 1, 20, 20)
        self.closepic = QLabel( self.btnclose)
        self.closepic.setGeometry(0, 0, 20, 20)
        self.closepic.setStyleSheet('background-color: white;\n'
                                      "border: 0px solid ;\n"
                                      "border-color:rgb(33,36,45);\n")
        pixmap = QPixmap('close.png')
        self.closepic.setPixmap(pixmap)
        self.btnclose.clicked.connect(self.ClickedClose)

        self.out = QPlainTextEdit(self.fileWidget)
        self.out.setGeometry(QtCore.QRect(4, 24, 440, 200))
        self.out.textChanged.connect(self.getText)
        self.out.setReadOnly(True)
        self.out.setStyleSheet("background-color:rgb(255,255,255);"
                               "border: 0px solid ;\n" )
        self.fileWidget.hide()

        self.show()

    def ClickedClose(self):
        self.out.clear()
        self.fileWidget.hide()

    def showProgress(self):
        #show progress widget
        self.progressWidget.show()
        self.prog.appendPlainText(str(0))
        QApplication.processEvents()

        #loading data in files
        i = 0
        for path in pathlib.Path(fileName).iterdir():
            if path.is_file():
                i += 1
                current_file = open(path, "r", encoding='UTF-8')
                s = current_file.read()
                import re
                # D, file, anotherfile, name = path.split('/')
                keys = list(map(str, re.split('[@. ]', s)))[:len(s)]
                for key in keys:
                    if key.find("’") != -1:
                        x = key.find("’")  # ’ mo5tlfa 3an '
                        key = key[:x]
                    else:
                        key = ''.join([i for i in key if i.isalpha()])

                    T.insert(key, path.name)

                current_file.close()
                keys.clear()
                self.prog.appendPlainText(str(i))
                if not i % 20:
                    QApplication.processEvents(QtCore.QEventLoop.AllEvents, 50)

        self.progressWidget.close()

    # return file name
    def Clicked(self, item):
        file_subPath = (item.text())
        name=pathlib.Path(fileName, file_subPath)

        file = open(name, 'r')

        with file:
            text = file.read()
            self.out.setPlainText(text)
        file.close()
        self.fileWidget.show()

    # -------------------write txt from gui"we input the word throw input.txt to code" --------------------
    def getText(self):
        word = self.b.document().toPlainText()
        global output
        output = T.search(word)

    # -------------------------------write the output into gui------------------------------------------

    def write(self):
        if output == "Not Found":
            self.listWidget.clear()
            self.listWidget.addItem(output)
        else:
            #filesList = list(output)
            #filesList = output
            self.listWidget.clear()
            for file in output:
                listWidgetItem = QListWidgetItem(file)
                self.listWidget.addItem(listWidgetItem)

            # --------------------------------run function----------------------------------------
    def run(self):
        self.write()

    # -------------------------------info function-----------------------------------------------------
    def getInfo(self):
        global fileName
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.showProgress()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())