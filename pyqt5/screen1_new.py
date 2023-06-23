# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from screen2_new import Ui_Screen2


class Ui_Screen1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(310, 150)
        MainWindow.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowMinimizeButtonHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(400, 150))
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 9, 16, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 10, 251, 110))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ScanPushButton = QtWidgets.QPushButton(self.widget)
        self.ScanPushButton.setStyleSheet("background: rgb(85, 170, 255)")
        self.ScanPushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/icons/qr-code-scan.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ScanPushButton.setIcon(icon)
        self.ScanPushButton.setIconSize(QtCore.QSize(100, 100))
        self.ScanPushButton.setObjectName("ScanPushButton")
        self.horizontalLayout.addWidget(self.ScanPushButton)
        spacerItem = QtWidgets.QSpacerItem(13, 105, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.SummaryPushButton = QtWidgets.QPushButton(self.widget)
        self.SummaryPushButton.setStyleSheet("background: #55aaff")
        self.SummaryPushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/icons/summary_pyqt5.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.SummaryPushButton.setIcon(icon1)
        self.SummaryPushButton.setIconSize(QtCore.QSize(100, 100))
        self.SummaryPushButton.setObjectName("SummaryPushButton")
        self.horizontalLayout.addWidget(self.SummaryPushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 418, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.ScanPushButton.clicked.connect(self.secondscr)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def secondscr(self):
        # Code the 2nd screen here
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Screen2()
        self.ui.setupUi(self.Form)
        self.Form.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Screen1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
