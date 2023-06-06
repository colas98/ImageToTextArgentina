# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QPropertyAnimation

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(627, 383)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.SuperiorFrame = QtWidgets.QFrame(Form)
        self.SuperiorFrame.setMinimumSize(QtCore.QSize(0, 60))
        self.SuperiorFrame.setMaximumSize(QtCore.QSize(16777215, 60))
        self.SuperiorFrame.setStyleSheet("background-color:rgb(85, 255, 255)")
        self.SuperiorFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.SuperiorFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.SuperiorFrame.setObjectName("SuperiorFrame")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.SuperiorFrame)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.MenuButton = QtWidgets.QPushButton(self.SuperiorFrame)
        self.MenuButton.setMinimumSize(QtCore.QSize(140, 30))
        self.MenuButton.setStyleSheet("QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 8pt \"Arial Black\"\n"
"}\n"
"\n"
"QPushButton{\n"
"border:0px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/icons/icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.MenuButton.setIcon(icon)
        self.MenuButton.setObjectName("MenuButton")
        self.MenuButton.clicked.connect(self.mover_menu)

        self.horizontalLayout_4.addWidget(self.MenuButton)
        spacerItem = QtWidgets.QSpacerItem(225, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.SuperiorFrame)
        self.BottomFrame = QtWidgets.QFrame(Form)
        self.BottomFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.BottomFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.BottomFrame.setObjectName("BottomFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.BottomFrame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.LateralFrame = QtWidgets.QFrame(self.BottomFrame)
        self.LateralFrame.setMinimumSize(QtCore.QSize(0, 0))
        self.LateralFrame.setMaximumSize(QtCore.QSize(0, 16777215))
        self.LateralFrame.setStyleSheet("QFrame{\n"
"background: rgb(85, 170, 255)\n"
"}\n"
"\n"
"QPushButton{\n"
"border-top-left-radius: 20px; \n"
"border-bottom-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton-hover{\n"
"background-color: white; \n"
"border-top-left-radius: 20px; \n"
"border-bottom-left-radius: 20px; \n"
"}\n"
"")
        self.LateralFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.LateralFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.LateralFrame.setObjectName("LateralFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.LateralFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.PathButton = QtWidgets.QPushButton(self.LateralFrame)
        self.PathButton.setMinimumSize(QtCore.QSize(0, 40))
        self.PathButton.setStyleSheet("QPushButton:hover{\n"
"background-color:white;\n"
"}")
        self.PathButton.setObjectName("PathButton")
        self.verticalLayout_2.addWidget(self.PathButton)
        self.GeneralButton = QtWidgets.QPushButton(self.LateralFrame)
        self.GeneralButton.setMinimumSize(QtCore.QSize(0, 40))
        self.GeneralButton.setStyleSheet("QPushButton:hover{\n"
"background-color:white;\n"
"}\n"
"")
        self.GeneralButton.setObjectName("GeneralButton")
        self.verticalLayout_2.addWidget(self.GeneralButton)
        self.AdvancedButton = QtWidgets.QPushButton(self.LateralFrame)
        self.AdvancedButton.setMinimumSize(QtCore.QSize(0, 40))
        self.AdvancedButton.setStyleSheet("QPushButton:hover{\n"
"background-color:white;\n"
"}")
        self.AdvancedButton.setObjectName("AdvancedButton")
        self.verticalLayout_2.addWidget(self.AdvancedButton)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.PythonScanLabel = QtWidgets.QLabel(self.LateralFrame)
        font = QtGui.QFont()
        font.setItalic(True)
        self.PythonScanLabel.setFont(font)
        self.PythonScanLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PythonScanLabel.setObjectName("PythonScanLabel")
        self.verticalLayout_2.addWidget(self.PythonScanLabel)
        self.horizontalLayout.addWidget(self.LateralFrame)
        self.MainFrame = QtWidgets.QFrame(self.BottomFrame)
        self.MainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.MainFrame.setObjectName("MainFrame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.MainFrame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.stackedWidget = QtWidgets.QStackedWidget(self.MainFrame)
        self.stackedWidget.setObjectName("stackedWidget")
        self.WelcomePage = QtWidgets.QWidget()
        self.WelcomePage.setObjectName("WelcomePage")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.WelcomePage)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.WelcomeLabel = QtWidgets.QLabel(self.WelcomePage)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.WelcomeLabel.sizePolicy().hasHeightForWidth())
        self.WelcomeLabel.setSizePolicy(sizePolicy)
        self.WelcomeLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.WelcomeLabel.setObjectName("WelcomeLabel")
        self.verticalLayout_4.addWidget(self.WelcomeLabel)
        self.stackedWidget.addWidget(self.WelcomePage)
        self.PathsPage = QtWidgets.QWidget()
        self.PathsPage.setObjectName("PathsPage")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.PathsPage)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.PathsLabel = QtWidgets.QLabel(self.PathsPage)
        font = QtGui.QFont()
        font.setItalic(True)
        self.PathsLabel.setFont(font)
        self.PathsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.PathsLabel.setObjectName("PathsLabel")
        self.verticalLayout_6.addWidget(self.PathsLabel)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem2)
        self.BookFileButton = QtWidgets.QPushButton(self.PathsPage)
        self.BookFileButton.setObjectName("BookFileButton")
        self.BookFileButton.clicked.connect(self.getFileName)
        self.verticalLayout_6.addWidget(self.BookFileButton)
        self.BookLabel = QtWidgets.QLabel(self.PathsPage)
        self.BookLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.BookLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BookLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.BookLabel.setObjectName("BookLabel")
        self.verticalLayout_6.addWidget(self.BookLabel)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem3)
        self.SampleFileButton = QtWidgets.QPushButton(self.PathsPage)
        self.SampleFileButton.setObjectName("SampleFileButton")
        self.SampleFileButton.clicked.connect(self.getFileName2)

        self.verticalLayout_6.addWidget(self.SampleFileButton)
        self.SampleFileLabel = QtWidgets.QLabel(self.PathsPage)
        self.SampleFileLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        self.SampleFileLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.SampleFileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.SampleFileLabel.setObjectName("SampleFileLabel")
        self.verticalLayout_6.addWidget(self.SampleFileLabel)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem4)
        self.stackedWidget.addWidget(self.PathsPage)
        self.GeneralParametersPage = QtWidgets.QWidget()
        self.GeneralParametersPage.setObjectName("GeneralParametersPage")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.GeneralParametersPage)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.GeneralParametersLabel = QtWidgets.QLabel(self.GeneralParametersPage)
        font = QtGui.QFont()
        font.setItalic(True)
        self.GeneralParametersLabel.setFont(font)
        self.GeneralParametersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GeneralParametersLabel.setObjectName("GeneralParametersLabel")
        self.verticalLayout_5.addWidget(self.GeneralParametersLabel)
        self.FirstPageLabel = QtWidgets.QLabel(self.GeneralParametersPage)
        self.FirstPageLabel.setObjectName("FirstPageLabel")
        self.verticalLayout_5.addWidget(self.FirstPageLabel)
        self.FirstPageSpinBox = QtWidgets.QSpinBox(self.GeneralParametersPage)
        self.FirstPageSpinBox.setObjectName("FirstPageSpinBox")
        self.verticalLayout_5.addWidget(self.FirstPageSpinBox)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem6)
        self.LastPageLabel = QtWidgets.QLabel(self.GeneralParametersPage)
        self.LastPageLabel.setObjectName("LastPageLabel")
        self.verticalLayout_5.addWidget(self.LastPageLabel)
        self.SecondPageSpinBox = QtWidgets.QSpinBox(self.GeneralParametersPage)
        self.SecondPageSpinBox.setObjectName("SecondPageSpinBox")
        self.verticalLayout_5.addWidget(self.SecondPageSpinBox)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem7)
        self.SamplingPageLabel = QtWidgets.QLabel(self.GeneralParametersPage)
        self.SamplingPageLabel.setObjectName("SamplingPageLabel")
        self.verticalLayout_5.addWidget(self.SamplingPageLabel)
        self.SamplingcomboBox = QtWidgets.QComboBox(self.GeneralParametersPage)
        self.SamplingcomboBox.setObjectName("SamplingcomboBox")
        self.SamplingcomboBox.addItem("")
        self.SamplingcomboBox.addItem("")
        self.verticalLayout_5.addWidget(self.SamplingcomboBox)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.ThresholdingImageLabel = QtWidgets.QLabel(self.GeneralParametersPage)
        self.ThresholdingImageLabel.setObjectName("ThresholdingImageLabel")
        self.verticalLayout_5.addWidget(self.ThresholdingImageLabel)
        self.ThresholdingImageComboBox = QtWidgets.QComboBox(self.GeneralParametersPage)
        self.ThresholdingImageComboBox.setObjectName("ThresholdingImageComboBox")
        self.ThresholdingImageComboBox.addItem("")
        self.ThresholdingImageComboBox.addItem("")
        self.verticalLayout_5.addWidget(self.ThresholdingImageComboBox)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem9)
        self.ResizingImageLabel = QtWidgets.QLabel(self.GeneralParametersPage)
        self.ResizingImageLabel.setObjectName("ResizingImageLabel")
        self.verticalLayout_5.addWidget(self.ResizingImageLabel)
        self.ResizingImagecomboBox = QtWidgets.QComboBox(self.GeneralParametersPage)
        self.ResizingImagecomboBox.setObjectName("ResizingImagecomboBox")
        self.ResizingImagecomboBox.addItem("")
        self.ResizingImagecomboBox.addItem("")
        self.verticalLayout_5.addWidget(self.ResizingImagecomboBox)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.GeneralParametersPage)
        self.AdvancedParametersPage = QtWidgets.QWidget()
        self.AdvancedParametersPage.setObjectName("AdvancedParametersPage")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.AdvancedParametersPage)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AdvancedParametersLabel = QtWidgets.QLabel(self.AdvancedParametersPage)
        font = QtGui.QFont()
        font.setItalic(True)
        self.AdvancedParametersLabel.setFont(font)
        self.AdvancedParametersLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.AdvancedParametersLabel.setObjectName("AdvancedParametersLabel")
        self.verticalLayout_3.addWidget(self.AdvancedParametersLabel)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem11)
        self.ThresoldinMethodLabel = QtWidgets.QLabel(self.AdvancedParametersPage)
        self.ThresoldinMethodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ThresoldinMethodLabel.setObjectName("ThresoldinMethodLabel")
        self.verticalLayout_3.addWidget(self.ThresoldinMethodLabel)
        self.ThresholdingMethodComboBox = QtWidgets.QComboBox(self.AdvancedParametersPage)
        self.ThresholdingMethodComboBox.setObjectName("ThresholdingMethodComboBox")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.ThresholdingMethodComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.ThresholdingMethodComboBox)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem12)
        self.ResizingMethodLabel = QtWidgets.QLabel(self.AdvancedParametersPage)
        self.ResizingMethodLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ResizingMethodLabel.setObjectName("ResizingMethodLabel")
        self.verticalLayout_3.addWidget(self.ResizingMethodLabel)
        self.ResizingMethodComboBox = QtWidgets.QComboBox(self.AdvancedParametersPage)
        self.ResizingMethodComboBox.setObjectName("ResizingMethodComboBox")
        self.ResizingMethodComboBox.addItem("")
        self.ResizingMethodComboBox.addItem("")
        self.ResizingMethodComboBox.addItem("")
        self.ResizingMethodComboBox.addItem("")
        self.ResizingMethodComboBox.addItem("")
        self.verticalLayout_3.addWidget(self.ResizingMethodComboBox)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem13)
        self.stackedWidget.addWidget(self.AdvancedParametersPage)
        self.horizontalLayout_3.addWidget(self.stackedWidget)
        self.horizontalLayout.addWidget(self.MainFrame)
        self.verticalLayout.addWidget(self.BottomFrame)
        self.RunButton = QtWidgets.QPushButton(Form)
        self.RunButton.setStyleSheet("QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 8pt \"Arial Black\"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/icons/icons/118620_play_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.RunButton.setIcon(icon1)
        self.RunButton.setObjectName("RunButton")
        self.verticalLayout.addWidget(self.RunButton)
        self.ExitButton = QtWidgets.QPushButton(Form)
        self.ExitButton.setStyleSheet("QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 8pt \"Arial Black\"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/icons/icons/icons8-exit-50.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ExitButton.setIcon(icon2)
        self.ExitButton.setObjectName("ExitButton")
        self.verticalLayout.addWidget(self.ExitButton)

        self.PathButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.PathsPage))
        self.GeneralButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.GeneralParametersPage))
        self.AdvancedButton.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.AdvancedParametersPage))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.MenuButton.setText(_translate("Form", "  MENU"))
        self.PathButton.setText(_translate("Form", "Paths"))
        self.GeneralButton.setText(_translate("Form", "General Param"))
        self.AdvancedButton.setText(_translate("Form", "Advanced Param"))
        self.PythonScanLabel.setText(_translate("Form", "Python-Scan"))
        self.WelcomeLabel.setText(_translate("Form", "Welcome to SCAN module, click MENU to set the options "))
        self.PathsLabel.setText(_translate("Form", "PATHS"))
        self.BookFileButton.setText(_translate("Form", "Book file (.pdf)"))
        self.BookLabel.setText(_translate("Form", "None Selected"))
        self.SampleFileButton.setText(_translate("Form", "Sample File (.txt)"))
        self.SampleFileLabel.setText(_translate("Form", "None Selected"))
        self.GeneralParametersLabel.setText(_translate("Form", "GENERAL PARAMETERS"))
        self.FirstPageLabel.setText(_translate("Form", "First Page"))
        self.LastPageLabel.setText(_translate("Form", "Last Page"))
        self.SamplingPageLabel.setText(_translate("Form", "Sampling"))
        self.SamplingcomboBox.setItemText(0, _translate("Form", "True"))
        self.SamplingcomboBox.setItemText(1, _translate("Form", "False"))
        self.ThresholdingImageLabel.setText(_translate("Form", "Thresholding Image"))
        self.ThresholdingImageComboBox.setItemText(0, _translate("Form", "True"))
        self.ThresholdingImageComboBox.setItemText(1, _translate("Form", "False"))
        self.ResizingImageLabel.setText(_translate("Form", "Resizing Image"))
        self.ResizingImagecomboBox.setItemText(0, _translate("Form", "True"))
        self.ResizingImagecomboBox.setItemText(1, _translate("Form", "False"))
        self.AdvancedParametersLabel.setText(_translate("Form", "ADVANCED PARAMETERS"))
        self.ThresoldinMethodLabel.setText(_translate("Form", "Thresholding Method"))
        self.ThresholdingMethodComboBox.setItemText(0, _translate("Form", "None"))
        self.ThresholdingMethodComboBox.setItemText(1, _translate("Form", "All"))
        self.ThresholdingMethodComboBox.setItemText(2, _translate("Form", "1"))
        self.ThresholdingMethodComboBox.setItemText(3, _translate("Form", "2"))
        self.ThresholdingMethodComboBox.setItemText(4, _translate("Form", "3"))
        self.ThresholdingMethodComboBox.setItemText(5, _translate("Form", "4"))
        self.ThresholdingMethodComboBox.setItemText(6, _translate("Form", "5"))
        self.ThresholdingMethodComboBox.setItemText(7, _translate("Form", "6"))
        self.ThresholdingMethodComboBox.setItemText(8, _translate("Form", "7"))
        self.ResizingMethodLabel.setText(_translate("Form", "Resizing Method"))
        self.ResizingMethodComboBox.setItemText(0, _translate("Form", "None"))
        self.ResizingMethodComboBox.setItemText(1, _translate("Form", "All"))
        self.ResizingMethodComboBox.setItemText(2, _translate("Form", "1"))
        self.ResizingMethodComboBox.setItemText(3, _translate("Form", "2"))
        self.ResizingMethodComboBox.setItemText(4, _translate("Form", "3"))
        self.RunButton.setText(_translate("Form", "Run"))
        self.ExitButton.setText(_translate("Form", "Exit"))
        self.ExitButton.clicked.connect(lambda: self.closescr(Form))

    def mover_menu(self):
        if True:
            width = self.LateralFrame.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal
            self.animacion = QPropertyAnimation(self.LateralFrame, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animacion.start()

    def closescr(self, Form):
        Form.hide()

    def getFileName(self):
        response = QFileDialog.getOpenFileName(
        )
        self.BookLabel.setText(response[0])
        return response[0]

    def getFileName2(self):
        response = QFileDialog.getOpenFileName(
        )
        self.SampleFileLabel.setText(response[0])
        return response[0]

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
