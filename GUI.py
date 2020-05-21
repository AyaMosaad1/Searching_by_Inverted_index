from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui ,QtWidgets


import sys
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
        #self.out = QPlainTextEdit(self)
        #self.out.resize(800, 250)
        #self.out.move(100, 200)
        #self.out.textChanged.connect(self.getText)
        #self.out.setReadOnly(True)
        #self.out.setStyleSheet("""QPlainTextEdit {background-color: #333;color: #fff;}""")

        self.initUI()

    def initUI(self):
        # ----------------main window-----------------
        self.setGeometry(200, 100, 1000, 470)
        self.setStyleSheet('background-color: rgb(255,255,255)')
        self.setWindowTitle('Searching_Engine')
        self.setWindowIcon(QtGui.QIcon('search.png'))

        # ----------------add widget to left"show data"----------------
        self.leftWidget = QtWidgets.QTabWidget(self)
        self.leftWidget.setGeometry(QtCore.QRect(560, 20, 400, 400))
        self.leftWidget.setObjectName("leftWidget")
        # table
        self.tableWidget = QTableWidget(self.leftWidget)
        data = {'Kitty': ['1', '2', '3', '3'],
                'Cat': ['4', '5', '6', '2'],
                'Meow': ['7', '8', '9', '5'],
                'Purr': ['4', '3', '4', '8'], }

        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)
        # Enter data onto Table
        horHeaders = []
        for n, key in enumerate(sorted(data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(data[key]):
                newitem = QTableWidgetItem(item)
                self.tableWidget.setItem(m, n, newitem)
        # Add Header
        self.tableWidget.setHorizontalHeaderLabels(horHeaders)

        # Adjust size of Table
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()

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
        # progrees bar
        self.progress  = QProgressBar(self.progressWidget)
        self.progress .setGeometry(20, 100, 355, 20)
        self.progress .setStyleSheet('color: rgb(255,255,255);\n' )

        # label
        self.progressBar = QLabel(self.progressWidget)
        self.progressBar.setGeometry(140, 50, 200, 40)
        self.progressBar.setFont(QFont('Arial', 12))
        self.progressBar.setText("Loading files ....")
        self.progressBar.setStyleSheet("background-color:rgb(33,36,45);\n"
                                       "border: 0px solid ;\n"
                                       )
        self.progressWidget.show()
        print(fileName)#hna l moshkla
        for path in pathlib.Path(fileName).iterdir():
            if path.is_file():
                print('yarab')
                current_file = open(path, "r", encoding='UTF-8')
                print('yarab')
                s = current_file.read()
                print('yarab')
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
        #readallfiles(fileName, T)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Example()
    sys.exit(app.exec_())