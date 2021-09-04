# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacevVsZah.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1228, 797)
        MainWindow.setStyleSheet(u"border:none;\n"
"background-color: rgb(255, 255, 255);\n"
"     font-size:20px;\n"
"     color:rgb(255,255,255);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color:rgb(24,24,36);\n"
"background-color: rgb(0, 0, 0);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SideMenuBar_container_frame = QFrame(self.centralwidget)
        self.SideMenuBar_container_frame.setObjectName(u"SideMenuBar_container_frame")
        self.SideMenuBar_container_frame.setMaximumSize(QSize(200, 16777215))
        self.SideMenuBar_container_frame.setStyleSheet(u"background-color: rgb(9,5,13);")
        self.SideMenuBar_container_frame.setFrameShape(QFrame.StyledPanel)
        self.SideMenuBar_container_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.SideMenuBar_container_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.side_menu_frame = QFrame(self.SideMenuBar_container_frame)
        self.side_menu_frame.setObjectName(u"side_menu_frame")
        self.side_menu_frame.setMinimumSize(QSize(200, 0))
        self.side_menu_frame.setMaximumSize(QSize(200, 16777215))
        self.side_menu_frame.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.side_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.side_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.side_menu_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.frame = QFrame(self.side_menu_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 15)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: italic 14pt \"aakar\";")

        self.horizontalLayout_3.addWidget(self.label, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")
        self.label_3.setPixmap(QPixmap(u":/newPrefix/icons8-jacket-50.png"))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setPixmap(QPixmap(u":/newPrefix/icon_imgs/icons8-jacket-50.png"))

        self.horizontalLayout_3.addWidget(self.label_2)


        self.verticalLayout_3.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.side_menu_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 0))
        self.toolBox.setCursor(QCursor(Qt.OpenHandCursor))
        self.toolBox.setStyleSheet(u"height: 100px;\n"
"\n"
"QToolBox{\n"
"	background-color:rgb(24,24,36);\n"
"text-align:left;\n"
"}\n"
"\n"
"QToolBox::Tab {\n"
"	border-radius: 5px;\n"
"	background-color: rgb(17,16, 26);\n"
"	text-align:left;\n"
"}")
        self.toolBox.setFrameShape(QFrame.NoFrame)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 182, 200))
        self.verticalLayout_7 = QVBoxLayout(self.page)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.pushButton_7 = QPushButton(self.frame_9)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy2)
        self.pushButton_7.setMaximumSize(QSize(102, 29))
        self.pushButton_7.setStyleSheet(u"font: 0 10pt \"Cantarell\";")

        self.verticalLayout_8.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMaximumSize(QSize(102, 29))
        self.pushButton_8.setStyleSheet(u"font: 0 10pt \"Cantarell\";")

        self.verticalLayout_8.addWidget(self.pushButton_8)


        self.verticalLayout_7.addWidget(self.frame_9, 0, Qt.AlignHCenter|Qt.AlignTop)

        icon = QIcon()
        icon.addFile(u":/newPrefix/icon_imgs/icons8-home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon, u"Home")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 182, 200))
        self.pushButton_9 = QPushButton(self.page_2)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(30, 0, 102, 29))
        self.pushButton_9.setStyleSheet(u"font: 0 10pt \"Cantarell\";")
        self.pushButton_10 = QPushButton(self.page_2)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(30, 40, 102, 29))
        self.pushButton_10.setStyleSheet(u"font: 0 10pt \"Cantarell\";")
        icon1 = QIcon()
        icon1.addFile(u":/newPrefix/icon_imgs/icons8-member-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon1, u"Customers")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 182, 200))
        self.pushButton_15 = QPushButton(self.page_3)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(20, 10, 102, 29))
        self.pushButton_15.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        self.pushButton_16 = QPushButton(self.page_3)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(20, 50, 102, 29))
        self.pushButton_16.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        icon2 = QIcon()
        icon2.addFile(u":/newPrefix/icon_imgs/icons8-mobile-order-128.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_3, icon2, u"Order")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 182, 200))
        self.pushButton_12 = QPushButton(self.page_4)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(30, 40, 102, 29))
        self.pushButton_12.setMaximumSize(QSize(102, 29))
        self.pushButton_12.setStyleSheet(u"font: 0 10pt \"Cantarell\";")
        self.pushButton_13 = QPushButton(self.page_4)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(30, 80, 102, 29))
        self.pushButton_13.setMaximumSize(QSize(102, 29))
        self.pushButton_13.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        self.pushButton_14 = QPushButton(self.page_4)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(30, 120, 102, 29))
        self.pushButton_14.setMaximumSize(QSize(102, 29))
        self.pushButton_14.setStyleSheet(u"font: 0 10pt \"Cantarell\";")
        self.pushButton_11 = QPushButton(self.page_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(30, 0, 102, 29))
        self.pushButton_11.setMaximumSize(QSize(102, 29))
        self.pushButton_11.setStyleSheet(u"font: 0 10pt \"Cantarell\";")
        icon3 = QIcon()
        icon3.addFile(u":/newPrefix/icon_imgs/icons8-product-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_4, icon3, u"Products")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setGeometry(QRect(0, 0, 182, 200))
        self.pushButton_17 = QPushButton(self.page_5)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(30, 10, 102, 29))
        self.pushButton_17.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        self.pushButton_18 = QPushButton(self.page_5)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(30, 50, 102, 29))
        self.pushButton_18.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        self.toolBox.addItem(self.page_5, icon1, u"Employees")
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setGeometry(QRect(0, 0, 182, 200))
        self.pushButton_19 = QPushButton(self.page_6)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(30, 10, 102, 29))
        self.pushButton_19.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        self.pushButton_20 = QPushButton(self.page_6)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(30, 50, 102, 29))
        self.pushButton_20.setStyleSheet(u"font: 0 12pt \"Cantarell\";")
        icon4 = QIcon()
        icon4.addFile(u":/newPrefix/icon_imgs/icons8-depot-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_6, icon4, u"Distributors")

        self.verticalLayout_4.addWidget(self.toolBox, 0, Qt.AlignTop)


        self.verticalLayout_3.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.side_menu_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.frame_3)
        self.pushButton.setObjectName(u"pushButton")
        icon5 = QIcon()
        icon5.addFile(u":/newPrefix/icon_imgs/gnome_logout.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon5)
        self.pushButton.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.pushButton, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout_2.addWidget(self.side_menu_frame)


        self.horizontalLayout.addWidget(self.SideMenuBar_container_frame)

        self.main_body = QFrame(self.centralwidget)
        self.main_body.setObjectName(u"main_body")
        self.main_body.setStyleSheet(u"background-color: rgb(219, 219, 219);")
        self.main_body.setFrameShape(QFrame.StyledPanel)
        self.main_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_body)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.main_body)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy3)
        self.header_frame.setMinimumSize(QSize(300, 45))
        self.header_frame.setStyleSheet(u"background-color:rgb(9,5,13);")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_4 = QFrame(self.header_frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.OpenHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/newPrefix/icon_imgs/icons8-menu-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.horizontalLayout_9.addWidget(self.pushButton_5, 0, Qt.AlignLeft|Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.header_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.lineEdit = QLineEdit(self.frame_5)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy4)
        font = QFont()
        font.setFamily(u"Cantarell")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit.setStyleSheet(u"font: 0 12pt \"Cantarell\";\n"
"border-bottom-color: rgb(255, 255, 255);\n"
"")
        self.lineEdit.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.lineEdit, 0, Qt.AlignVCenter)

        self.pushButton_4 = QPushButton(self.frame_5)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.OpenHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/newPrefix/icon_imgs/icons8-search-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon7)
        self.pushButton_4.setIconSize(QSize(28, 28))

        self.horizontalLayout_8.addWidget(self.pushButton_4, 0, Qt.AlignVCenter)


        self.horizontalLayout_5.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.header_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.OpenHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/newPrefix/icon_imgs/user-16.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon8)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_7.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.OpenHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/newPrefix/icon_imgs/icons8-notification-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon9)
        self.pushButton_3.setIconSize(QSize(26, 26))

        self.horizontalLayout_7.addWidget(self.pushButton_3, 0, Qt.AlignRight|Qt.AlignTop)


        self.horizontalLayout_5.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignVCenter)

        self.main_body_contents = QFrame(self.main_body)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy1.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy1)
        self.main_body_contents.setStyleSheet(u"background-color: rgb(23, 23, 23);")
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.main_body_contents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.verticalLayout.addWidget(self.main_body_contents)

        self.footer = QFrame(self.main_body)
        self.footer.setObjectName(u"footer")
        self.footer.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.footer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_7)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4, 0, Qt.AlignBottom)


        self.horizontalLayout_6.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.footer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(460, -10, 41, 41))
        sizePolicy4.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy4)
        self.pushButton_6.setAutoFillBackground(False)
        icon10 = QIcon()
        icon10.addFile(u":/newPrefix/icon_imgs/exit.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon10)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_6.addWidget(self.frame_8)

        self.size_grip = QFrame(self.footer)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.size_grip)


        self.verticalLayout.addWidget(self.footer)


        self.horizontalLayout.addWidget(self.main_body)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(5)
        self.toolBox.layout().setSpacing(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Shop Name", None))
        self.label_3.setText("")
        self.label_2.setText("")
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Daily report", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Home", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Lists", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Customers", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.pushButton_16.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("MainWindow", u"Order", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Catalog", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"something", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"something", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("MainWindow", u"Products", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.pushButton_18.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_5), QCoreApplication.translate("MainWindow", u"Employees", None))
        self.pushButton_19.setText(QCoreApplication.translate("MainWindow", u"List", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_6), QCoreApplication.translate("MainWindow", u"Distributors", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.pushButton_5.setText("")
        self.lineEdit.setText(QCoreApplication.translate("MainWindow", u"search", None))
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Moderen ui v 7.7.7", None))
        self.pushButton_6.setText("")
    # retranslateUi

