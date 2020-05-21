from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
from trie import *
T = Trie()
output ="False"
# -----------------------------------initialize a window-----------------------
class Example(QWidget):

    def __init__(self):
        super().__init__()

        # -----------------------input text area for enter the searching word -----------------------------
        self.b = QPlainTextEdit(self)
        self.b.move(50, 50)
        self.b.resize(300, 40)
        self.b.textChanged.connect(self.getText)
        self.b.setPlaceholderText("search")

        # ---------------------output text area --------------------------------
        self.out = QPlainTextEdit(self)
        self.out.resize(800, 250)
        self.out.move(100, 200)
        self.out.textChanged.connect(self.getText)
        self.out.setReadOnly(True)
        self.out.setStyleSheet("""QPlainTextEdit {background-color: #333;color: #fff;}""")

        self.initUI()

    def initUI(self):
        # ----------------main window-----------------
        self.setGeometry(200, 200, 1000, 500)
        self.setWindowTitle('Searching_Engine')

        # -----------------run button-----------------
        self.runB = QPushButton('Search', self)
        self.runB.move(50, 110)
        self.runB.resize(300, 40)
        # when run it
        self.runB.clicked.connect(self.run)

        # ----------------info "Run one step" button-----------------
        self.info = QPushButton('Browse', self)
        self.info.move(500, 60)
        self.info.resize(300, 90)
        self.info.clicked.connect(self.getInfo)

        self.show()

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
        fileName = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        readallfiles(fileName, T)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    w = Example()
    sys.exit(app.exec_())