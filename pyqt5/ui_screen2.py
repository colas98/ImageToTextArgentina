# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'screen2FIqOlW.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(435, 235)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_superior = QFrame(Form)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setMinimumSize(QSize(0, 40))
        self.frame_superior.setMaximumSize(QSize(16777215, 40))
        self.frame_superior.setStyleSheet(u"background-color:rgb(85, 255, 255)")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_superior)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.bt_menu = QPushButton(self.frame_superior)
        self.bt_menu.setObjectName(u"bt_menu")
        self.bt_menu.setStyleSheet(u"QPushButton:hover{\n"
"background-color: white;\n"
"font: 87 8pt \"Arial Black\"\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"images/icons/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_menu.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.bt_menu)

        self.horizontalSpacer = QSpacerItem(225, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.bt_minimize = QPushButton(self.frame_superior)
        self.bt_minimize.setObjectName(u"bt_minimize")
        self.bt_minimize.setMinimumSize(QSize(16, 16))
        self.bt_minimize.setMaximumSize(QSize(16777215, 35))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bt_minimize.setFont(font)
        self.bt_minimize.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #a00ff;\n"
"background-color: rgb(85, 170, 255); \n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"images/icons/icons/icons8-minimize-26.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minimize.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.bt_minimize)

        self.bt_minsize = QPushButton(self.frame_superior)
        self.bt_minsize.setObjectName(u"bt_minsize")
        self.bt_minsize.setMinimumSize(QSize(16, 16))
        self.bt_minsize.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #a00ff;\n"
"background-color: rgb(85, 170, 255); \n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"images/icons/icons/icons8-minimize-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_minsize.setIcon(icon2)

        self.horizontalLayout_2.addWidget(self.bt_minsize)

        self.bt_maxsize = QPushButton(self.frame_superior)
        self.bt_maxsize.setObjectName(u"bt_maxsize")
        self.bt_maxsize.setMinimumSize(QSize(16, 16))
        self.bt_maxsize.setMaximumSize(QSize(16777215, 35))
        font1 = QFont()
        font1.setPointSize(8)
        font1.setBold(True)
        font1.setWeight(75)
        self.bt_maxsize.setFont(font1)
        self.bt_maxsize.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #a00ff;\n"
"background-color: rgb(85, 170, 255); \n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"images/icons/icons/icons8-maximize-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_maxsize.setIcon(icon3)

        self.horizontalLayout_2.addWidget(self.bt_maxsize)

        self.bt_close = QPushButton(self.frame_superior)
        self.bt_close.setObjectName(u"bt_close")
        self.bt_close.setMinimumSize(QSize(16, 16))
        self.bt_close.setMaximumSize(QSize(16777215, 35))
        self.bt_close.setFont(font1)
        self.bt_close.setStyleSheet(u"QPushButton{\n"
"border:0px;\n"
"}\n"
"QPushButton:hover{\n"
"border: 5px solid #a00ff;\n"
"background-color: rgb(85, 170, 255); \n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"images/icons/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bt_close.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.bt_close)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addWidget(self.frame_superior)

        self.frame_inferior = QFrame(Form)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_inferior)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_lateral = QFrame(self.frame_inferior)
        self.frame_lateral.setObjectName(u"frame_lateral")
        self.frame_lateral.setMaximumSize(QSize(0, 16777215))
        self.frame_lateral.setStyleSheet(u"QFrame{\n"
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
        self.frame_lateral.setFrameShape(QFrame.StyledPanel)
        self.frame_lateral.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_lateral)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.bt_path = QPushButton(self.frame_lateral)
        self.bt_path.setObjectName(u"bt_path")
        self.bt_path.setMinimumSize(QSize(0, 40))
        self.bt_path.setStyleSheet(u"QPushButton:hover{\n"
"background-color:white;\n"
"}")

        self.verticalLayout_2.addWidget(self.bt_path)

        self.bt_general = QPushButton(self.frame_lateral)
        self.bt_general.setObjectName(u"bt_general")
        self.bt_general.setMinimumSize(QSize(0, 40))
        self.bt_general.setStyleSheet(u"QPushButton:hover{\n"
"background-color:white;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.bt_general)

        self.bt_advanced = QPushButton(self.frame_lateral)
        self.bt_advanced.setObjectName(u"bt_advanced")
        self.bt_advanced.setMinimumSize(QSize(0, 40))
        self.bt_advanced.setStyleSheet(u"QPushButton:hover{\n"
"background-color:white;\n"
"}")

        self.verticalLayout_2.addWidget(self.bt_advanced)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.label = QLabel(self.frame_lateral)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame_lateral)

        self.frame = QFrame(self.frame_inferior)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_4.addWidget(self.pushButton_3)

        self.stackedWidget.addWidget(self.page)
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.verticalLayout_6 = QVBoxLayout(self.page_1)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.path = QPushButton(self.page_1)
        self.path.setObjectName(u"path")

        self.verticalLayout_6.addWidget(self.path)

        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.general = QPushButton(self.page_2)
        self.general.setObjectName(u"general")

        self.verticalLayout_5.addWidget(self.general)

        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_3 = QVBoxLayout(self.page_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.advance = QPushButton(self.page_3)
        self.advance.setObjectName(u"advance")

        self.verticalLayout_3.addWidget(self.advance)

        self.stackedWidget.addWidget(self.page_3)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.horizontalLayout.addWidget(self.frame)


        self.verticalLayout.addWidget(self.frame_inferior)

        self.exit = QPushButton(Form)
        self.exit.setObjectName(u"exit")

        self.verticalLayout.addWidget(self.exit)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.bt_menu.setText(QCoreApplication.translate("Form", u"MENU", None))
        self.bt_minimize.setText("")
        self.bt_minsize.setText("")
        self.bt_maxsize.setText("")
        self.bt_close.setText("")
        self.bt_path.setText(QCoreApplication.translate("Form", u"Path", None))
        self.bt_general.setText(QCoreApplication.translate("Form", u"General", None))
        self.bt_advanced.setText(QCoreApplication.translate("Form", u"Advance", None))
        self.label.setText(QCoreApplication.translate("Form", u"Python-Scan", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.path.setText(QCoreApplication.translate("Form", u"Path", None))
        self.general.setText(QCoreApplication.translate("Form", u"General", None))
        self.advance.setText(QCoreApplication.translate("Form", u"Advance", None))
        self.exit.setText(QCoreApplication.translate("Form", u"Exit", None))
    # retranslateUi

