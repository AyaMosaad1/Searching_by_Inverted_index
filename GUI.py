import sys
import time
import os.path

from PyQt5.QtCore import QRegExp

from trie import *
from pathlib import Path
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *

T = Trie()

# -----------------------------------initialize a window-----------------------
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # ----------------main window-----------------
        self.setGeometry(140, 120, 1040, 490)
        self.setStyleSheet('background-color: rgb(255,255,255)')
        self.setWindowTitle('Searching_Engine')
        self.setWindowIcon(QtGui.QIcon('search.png'))

        # ----------------------- "image"-select folder  -----------------------------
        self.label = QLabel(self)
        self.label.setGeometry(70, 90, 170, 170)
        pixmap = QPixmap('fin.png')
        self.label.setPixmap(pixmap)

        # -----------------------input text area for enter the searching word -----------------------------
        self.b = QPlainTextEdit(self)
        self.b.setGeometry(320, 210, 200, 36)
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
        self.info.setGeometry(40, 270, 220, 38)
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
        self.runB.setGeometry(310, 270, 220, 38)
        self.runB.setFont(QFont('Arial', 10))
        self.runB.setStyleSheet("background-color:rgb(33,36,45);\n"
                                "color: white;\n"
                                "border-style: outset;\n"
                                "border-width:0px;\n"
                                "border-radius:5px;\n"
                                "padding :6px;\n"
                                "min-width:10px;\n")
        self.runB.clicked.connect(self.run)

        # -----------------  display output files -----------------
        self.listWidget = QListWidget(self)
        self.listWidget.setGeometry(QtCore.QRect(580, 20, 410, 430))
        self.listWidget.setStyleSheet("background-color:rgb(255,255,255);\n"
                                      "border-style: outset;\n"
                                      "border-radius:5px;\n"
                                      "border-width:1px;\n"
                                      "border-color:rgb(33,36,45);\n")
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

        # -----------------choose output display widget-----------------
        self.chooseStyleWidget = QtWidgets.QWidget(self)
        self.chooseStyleWidget.setGeometry(QtCore.QRect(300, 135, 400, 180))
        self.chooseStyleWidget.setObjectName("progressWidget")
        self.chooseStyleWidget.setStyleSheet("background-color: white;\n"
                                             "border-radius:5px;\n"
                                             "border: 1px solid ;\n"
                                             "border-color:rgb(33,36,45);\n")

        self.choose = QLabel('Please choose one .......',self.chooseStyleWidget)
        self.choose.setFont(QFont('Arial', 13))
        self.choose.setGeometry(120, 30, 200, 70)
        self.choose.setStyleSheet("border: 0px solid ;\n")


        self.btnFile = QPushButton('Open file',self.chooseStyleWidget)
        self.btnFile.setFont(QFont('Arial', 10))
        self.btnFile.setGeometry(30, 100, 140, 35)
        self.btnFile.setStyleSheet('background-color: white;\n'
                                   "border-radius:5px;\n"
                                   "border: 1px solid ;\n"
                                   "border-color:rgb(33,36,45);\n")
        self.btnFile.clicked.connect(self.DisplayFile)


        self.btnSent = QPushButton('Show sentence',self.chooseStyleWidget)
        self.btnSent.setGeometry(210, 100, 140, 35)
        self.btnSent.setFont(QFont('Arial', 10))
        self.btnSent.setStyleSheet("background-color: white;\n"
                                   "border: 1px solid ;\n"
                                   "border-radius:5px;\n"
                                   "border-color:rgb(33,36,45);\n")
        self.btnSent.clicked.connect(self.showSentence)

        self.chooseStyleWidget.hide()

        # ---------------------display file content--------------------------------
        self.fileWidget = QtWidgets.QWidget(self)
        self.fileWidget.setGeometry(QtCore.QRect(300, 120, 450, 240))
        self.fileWidget.setObjectName("fileWidget")
        self.fileWidget.setStyleSheet('background-color: white;\n'
                                          "border-radius:5px;\n"
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


        self.fileWidget.hide()

        self.show()

    def ClickedClose(self):
        self.out.clear()
        self.fileWidget.hide()

    def showProgress(self):
        # show progress widget
        self.progressWidget.show()
        self.prog.appendPlainText(str(0))
        QApplication.processEvents()

        # loading data in files
        i = 0
        for path in pathlib.Path(fileName).iterdir():
            if path.is_file():
                i += 1
                current_file = open(path, "r", encoding='UTF-8')
                s = current_file.read()
                import re
                # D, file, anotherfile, name = path.split('/')
                keys = list(map(str, re.split('[@. ]', s)))[:len(s)]
                enteredwords = list()
                for key in keys:
                    if key.find("’") != -1:
                        x = key.find("’")  # ’ mo5tlfa 3an '
                        key = key[:x]
                    else:
                        key = ''.join([i for i in key if i.isalpha()])

                    if not key in enteredwords:
                        T.insert(key, path.name)
                        enteredwords.append(key)
                current_file.close()
                keys.clear()
                self.prog.appendPlainText(str(i))
                if not i % 20:
                    QApplication.processEvents(QtCore.QEventLoop.AllEvents, 50)

        self.progressWidget.close()


    # return file name
    def Clicked(self, item):
        file_subPath = (item.text())
        global filePath
        filePath=pathlib.Path(fileName, file_subPath)
        self.chooseStyleWidget.show()

    def DisplayFile(self):
        self.chooseStyleWidget.hide()
        self.out = MyHighlighter(filePath, word, self.fileWidget)
        # self.out = QPlainTextEdit(self.fileWidget)
        self.out.setGeometry(QtCore.QRect(4, 24, 440, 200))
        self.out.textChanged.connect(self.getText)
        self.out.setReadOnly(True)
        self.out.setStyleSheet("background-color:rgb(255,255,255);"
                               "border: 0px solid ;\n")
        self.out.show()

        self.fileWidget.show()

    def showSentence(self):
        self.chooseStyleWidget.hide()
        self.out = QPlainTextEdit(self.fileWidget)
        self.out.setGeometry(QtCore.QRect(4, 24, 440, 200))
        self.out.textChanged.connect(self.getText)
        self.out.setReadOnly(True)
        self.out.setStyleSheet("background-color:rgb(255,255,255);"
                                 "border: 0px solid ;\n" )
        with open(filePath, "r") as file:

            d = file.readlines()
            for line in d:
                if word.lower() in line.lower():
                    self.out.setPlainText(line)
                    break
        file.close()
        self.fileWidget.show()

    # -------------------write txt from gui"we input the word throw input.txt to code" --------------------
    def getText(self):
        global output
        global word
        word=self.b.document().toPlainText()
        output = T.search(word)

    # -------------------------------write the output into gui------------------------------------------



    def write(self):
        if output == "Not Found":
            self.listWidget.clear()
            self.listWidget.addItem(output)
        else:
            # filesList = list(output)
            # filesList = output
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



class MyHighlighter(QPlainTextEdit):
    def __init__(self,path,word, parent):
        super(MyHighlighter, self).__init__(parent)
        # Setup the text editor
        file = open(path, 'r')
        with file:
            text = file.read()
        text = text.casefold()
        self.setPlainText(text)
        cursor = self.textCursor()
        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("red")))
        # Setup the regex engine
        pattern = word

        regex = QtCore.QRegExp(pattern)

        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.toPlainText(), pos)
        while (index != -1):
            # Select the matched text and apply the desired format
            cursor.setPosition(index)
            cursor.movePosition(QtGui.QTextCursor.EndOfWord, 1)
            cursor.mergeCharFormat(format)
            # Move to the next match
            pos = index + regex.matchedLength()
            index = regex.indexIn(self.toPlainText(), pos)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Example()
    sys.exit(app.exec_())