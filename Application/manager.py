import webbrowser
import sys

from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit,
                             QApplication, QFileDialog, QProgressBar,
                             QMessageBox)

import Final, Check


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    gate = ""
    end = ""
    model = ""
    ans = ""

    def initUI(self):

        # gate folder button
        self.btn = QPushButton('Выберите папку со сканами', self)
        self.btn.resize(200, 25)
        self.btn.move(20, 20)
        self.btn.clicked.connect(self.showgateDialog)

        # End folder button
        self.btn = QPushButton('Выберите конечную папку со сканами', self)
        self.btn.resize(270, 25)
        self.btn.move(20, 60)
        self.btn.clicked.connect(self.showEndDialog)

        # Model file button
        self.btn = QPushButton('Выберите файл модели', self)
        self.btn.resize(200, 25)
        self.btn.move(20, 100)
        self.btn.clicked.connect(self.showModelDialog)

        # Run button
        self.btn = QPushButton('Запуск', self)
        self.btn.resize(80, 25)
        self.btn.move(20, 170)
        self.btn.clicked.connect(self.start)

        #Check button
        self.btn = QPushButton('Проверить', self)
        self.btn.resize(100, 25)
        self.btn.move(550, 170)
        self.btn.clicked.connect(self.check)

        #Exit button
        self.btn = QPushButton('Выход', self)
        self.btn.resize(80, 25)
        self.btn.move(560, 250)
        self.btn.clicked.connect(QApplication.quit)

        # gate editable line
        self.gate = QLineEdit(self)
        self.gate.resize(300, 25)
        self.gate.move(240, 22)

        # End editable line
        self.end = QLineEdit(self)
        self.end.resize(300, 25)
        self.end.move(310, 62)

        # Model editable line
        self.model = QLineEdit(self)
        self.model.resize(300, 25)
        self.model.move(240, 102)

        # Progress bar
        self.bar = QProgressBar(self)
        self.bar.resize(300, 25)
        self.bar.move(26, 140)
        # Set value
#        self.bar.setValue(50)

        self.setGeometry(300, 300, 700, 300)
        self.setWindowTitle('Выберите папку')
        self.show()

    def showgateDialog(self):
        global gate
        gate = str(QFileDialog.getExistingDirectory(self))+"/"
        self.gate.setText(str(gate))

    def showEndDialog(self):
        global end
        end = str(QFileDialog.getExistingDirectory(self))+"/"
        self.end.setText(str(end))

    def showModelDialog(self):
        global model
        model = str(QFileDialog.getOpenFileName(self)[0])
        self.model.setText(str(model))

    def start(self):
        global gate, end, model
        Final.Final.start(gate, end, model, self.bar)
        self.bar.setValue(100)
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        msg.setText("Открыть конечную папку?")
        msg.buttonClicked.connect(self.windbtn)

        retval = msg.exec_()
        print(retval)

    def windbtn(mes):
        print(mes)
 #       webbrowser.open('file:///' + end)

    def check(self):
        global end, ans
        Check.Check.check(Check, end, )

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
