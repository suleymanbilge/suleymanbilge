from PyQt5 import QtCore, QtGui, QtWidgets
from netmiko import ConnectHandler
from ping3 import ping
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(720, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cikti_listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.cikti_listWidget.setGeometry(QtCore.QRect(360, 10, 351, 331))
        self.cikti_listWidget.setObjectName("cikti_listWidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 180, 75, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clickme)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(20, 20, 251, 321))
        self.plainTextEdit.setObjectName("plainTextEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Ping"))

    def clickme(self):
            number: int = 0
            ipList = [self.plainTextEdit.toPlainText()]
            for i in ipList:
                list = i.split('\n')
                for j in list:
                    result = result = ping(j)
                    if result != None and result != False:
                        self.cikti_listWidget.insertItem(number,f"{j} ping result → OK")
                        number += 1
                    else:
                        self.cikti_listWidget.insertItem(number,f"{j} ping result → Not OK")
                    number += 1

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
