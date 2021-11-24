# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pic1spcMVT.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLineEdit, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTableView, QVBoxLayout, QWidget, QMessageBox)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(743, 498)
        self.actionABOUT = QAction(MainWindow)
        self.actionABOUT.setObjectName(u"actionABOUT")
        self.actionTODO = QAction(MainWindow)
        self.actionTODO.setObjectName(u"actionTODO")
        self.actionTODO2 = QAction(MainWindow)
        self.actionTODO2.setObjectName(u"actionTODO2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_4 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pushButton = QPushButton(self.groupBox)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setAutoFillBackground(False)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 11)
        self.horizontalLayout_2.setStretch(2, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 20, 0, 200)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.ipt_person = QLineEdit(self.groupBox)
        self.ipt_person.setObjectName(u"ipt_person")

        self.horizontalLayout.addWidget(self.ipt_person)

        self.btn_search = QPushButton(self.groupBox)
        self.btn_search.setObjectName(u"btn_search")

        self.horizontalLayout.addWidget(self.btn_search)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 6)
        self.horizontalLayout.setStretch(2, 5)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 10)

        self.horizontalLayout_4.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_3 = QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.groupBox_2)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_4.addWidget(self.groupBox_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 743, 22))
        self.menuPEOPLE = QMenu(self.menubar)
        self.menuPEOPLE.setObjectName(u"menuPEOPLE")
        self.menuTRAILS = QMenu(self.menubar)
        self.menuTRAILS.setObjectName(u"menuTRAILS")
        self.menuRESULTS = QMenu(self.menubar)
        self.menuRESULTS.setObjectName(u"menuRESULTS")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPEOPLE.menuAction())
        self.menubar.addAction(self.menuTRAILS.menuAction())
        self.menubar.addAction(self.menuRESULTS.menuAction())
        self.menuPEOPLE.addAction(self.actionABOUT)
        self.menuTRAILS.addAction(self.actionTODO)
        self.menuRESULTS.addAction(self.actionTODO2)

        self.retranslateUi(MainWindow)
        self.btn_search.clicked.connect(MainWindow.print_search)
        self.actionABOUT.triggered.connect(MainWindow.print_about)
        self.actionTODO.triggered.connect(MainWindow.print_todo)
        self.actionTODO2.triggered.connect(MainWindow.print_todo2)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi



    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionABOUT.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
        self.actionTODO.setText(QCoreApplication.translate("MainWindow", u"TODO", None))
        self.actionTODO2.setText(QCoreApplication.translate("MainWindow", u"TODO2", None))
        self.groupBox.setTitle("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"INSERT/MODIFY PERSON", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"SEARCH", None))
        self.groupBox_2.setTitle("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"LAST NAME", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"FIRST NAME", None))
        self.menuPEOPLE.setTitle(QCoreApplication.translate("MainWindow", u"PEOPLE", None))
        self.menuTRAILS.setTitle(QCoreApplication.translate("MainWindow", u"TRAILS", None))
        self.menuRESULTS.setTitle(QCoreApplication.translate("MainWindow", u"RESULTS", None))
    # retranslateUi

