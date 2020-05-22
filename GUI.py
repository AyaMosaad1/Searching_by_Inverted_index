from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os.path
from PyQt5 import QtCore, QtGui ,QtWidgets
from pathlib import Path
import sys
import time
from trie import *
T = Trie()
fileName ="hello"
output ="False"

# -----------------------------------initialize a window-----------------------
class Example(QWidget):

    def __init__(self):
        super().__init__()

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

        # ---------------------output text area --------------------------------
        self.out = QPlainTextEdit(self)
        self.out.setGeometry(QtCore.QRect(560, 20, 400, 400))
        self.out.textChanged.connect(self.getText)
        self.out.setReadOnly(True)
        self.out.setStyleSheet("QPlainTextEdit {background-color:rgb(255,255,255);}")
        self.initUI()

    def initUI(self):
        # ----------------main window-----------------
        self.setGeometry(200, 100, 1000, 470)
        self.setStyleSheet('background-color: rgb(255,255,255)')
        self.setWindowTitle('Searching_Engine')
        self.setWindowIcon(QtGui.QIcon('search.png'))


        # -----------------run button-----------------
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

        # ----------------info "Run one step" button-----------------
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
        self.show()

    def showProgress(self):
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

        #self.b.textChanged.connect(self.getnumber)

        # label
        self.progresslabel = QLabel(self.progressWidget)
        self.progresslabel.setGeometry(140, 100, 200, 40)
        self.progresslabel.setFont(QFont('Arial', 12))
        self.progresslabel.setText("Loading files ....")
        self.progresslabel.setStyleSheet("background-color:rgb(33,36,45);\n"
                                       "border: 0px solid ;\n")

        self.prog.appendPlainText(str(0))
        self.progressWidget.show()
        QApplication.processEvents()

        i=0
        os.chdir(fileName)
        for path in pathlib.Path(fileName).iterdir():
            num_files=len(list(Path('.').glob('*')))
            if path.is_file():
                i+=1
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

                self.prog.appendPlainText(str(i))
                QApplication.processEvents()


        self.progressWidget.close()


    # --------------------------------write txt from gui"we input the word throw input.txt to code" -------------------------------------

    def getText(self):
        global output
        output = T.search(self.b.document().toPlainText())


    # -------------------------------write the output into gui------------------------------------------
    def write(self):
        data = repr(output)
        self.out.setPlainText(data)


    # --------------------------------run function----------------------------------------
    def run(self):
        # write code to execute when pressing on "run" button
        self.write()

    # -------------------------------info function-----------------------------------------------------
    def getInfo(self):
        # write code to execute when pressing on "info" button
        global fileName
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.showProgress()



if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Example()
    sys.exit(app.exec_())