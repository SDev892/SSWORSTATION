# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sswEpMBgG.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateEdit,
    QFontComboBox, QFrame, QGridLayout, QGroupBox,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1208, 844)
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        MainWindow.setPalette(palette)
        self.actionCreate_new_invoice = QAction(MainWindow)
        self.actionCreate_new_invoice.setObjectName(u"actionCreate_new_invoice")
        self.actionOpen_Invoices = QAction(MainWindow)
        self.actionOpen_Invoices.setObjectName(u"actionOpen_Invoices")
        self.actionimport_stock_file_SSW_Type = QAction(MainWindow)
        self.actionimport_stock_file_SSW_Type.setObjectName(u"actionimport_stock_file_SSW_Type")
        self.actionimport_stock_file_Ai_Check = QAction(MainWindow)
        self.actionimport_stock_file_Ai_Check.setObjectName(u"actionimport_stock_file_Ai_Check")
        self.actionBuy_Invoices = QAction(MainWindow)
        self.actionBuy_Invoices.setObjectName(u"actionBuy_Invoices")
        self.actionSell_Invoices = QAction(MainWindow)
        self.actionSell_Invoices.setObjectName(u"actionSell_Invoices")
        self.actionStock_Items = QAction(MainWindow)
        self.actionStock_Items.setObjectName(u"actionStock_Items")
        self.actionGraph_Creator = QAction(MainWindow)
        self.actionGraph_Creator.setObjectName(u"actionGraph_Creator")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Window, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush)
        self.stackedWidget.setPalette(palette1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.gridLayout_5 = QGridLayout(self.page_3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setSpacing(10)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(20, 20, 20, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.logoname = QLabel(self.page_3)
        self.logoname.setObjectName(u"logoname")
        self.logoname.setStyleSheet(u"font: 600 36pt \"Rubik\";\n"
"\n"
"color: rgb(77, 77, 77);")
        self.logoname.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.logoname, 0, 0, 1, 1, Qt.AlignmentFlag.AlignTop)

        self.stockshow = QPushButton(self.page_3)
        self.stockshow.setObjectName(u"stockshow")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.stockshow.sizePolicy().hasHeightForWidth())
        self.stockshow.setSizePolicy(sizePolicy)
        self.stockshow.setMinimumSize(QSize(800, 60))
        self.stockshow.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.stockshow, 3, 0, 1, 1)

        self.NewInvoice = QPushButton(self.page_3)
        self.NewInvoice.setObjectName(u"NewInvoice")
        self.NewInvoice.setMinimumSize(QSize(0, 60))
        self.NewInvoice.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.NewInvoice, 1, 0, 1, 1)

        self.invoicesshow = QPushButton(self.page_3)
        self.invoicesshow.setObjectName(u"invoicesshow")
        self.invoicesshow.setMinimumSize(QSize(0, 60))
        self.invoicesshow.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_4.addWidget(self.invoicesshow, 2, 0, 1, 1)

        self.appinformation = QLabel(self.page_3)
        self.appinformation.setObjectName(u"appinformation")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.appinformation.sizePolicy().hasHeightForWidth())
        self.appinformation.setSizePolicy(sizePolicy1)
        self.appinformation.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_4.addWidget(self.appinformation, 5, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_4, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_3)
        self.InvoiceCreator = QWidget()
        self.InvoiceCreator.setObjectName(u"InvoiceCreator")
        self.gridLayout_7 = QGridLayout(self.InvoiceCreator)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.freeeditcheckbox = QCheckBox(self.InvoiceCreator)
        self.freeeditcheckbox.setObjectName(u"freeeditcheckbox")

        self.gridLayout_6.addWidget(self.freeeditcheckbox, 3, 0, 1, 1)

        self.frame = QFrame(self.InvoiceCreator)
        self.frame.setObjectName(u"frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy2)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_3 = QGroupBox(self.frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 80))
        self.gridLayout_16 = QGridLayout(self.groupBox_3)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_15 = QGridLayout()
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.label_15 = QLabel(self.groupBox_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_15, 2, 1, 1, 1)

        self.vatline = QLineEdit(self.groupBox_3)
        self.vatline.setObjectName(u"vatline")
        self.vatline.setReadOnly(True)

        self.gridLayout_15.addWidget(self.vatline, 2, 2, 1, 1)

        self.discountline = QLineEdit(self.groupBox_3)
        self.discountline.setObjectName(u"discountline")
        self.discountline.setReadOnly(True)

        self.gridLayout_15.addWidget(self.discountline, 1, 2, 1, 1)

        self.Htline = QLineEdit(self.groupBox_3)
        self.Htline.setObjectName(u"Htline")
        self.Htline.setReadOnly(True)

        self.gridLayout_15.addWidget(self.Htline, 0, 2, 1, 1)

        self.label_13 = QLabel(self.groupBox_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_13, 0, 1, 1, 1)

        self.ttcline = QLineEdit(self.groupBox_3)
        self.ttcline.setObjectName(u"ttcline")
        self.ttcline.setReadOnly(True)

        self.gridLayout_15.addWidget(self.ttcline, 3, 2, 1, 1)

        self.label_14 = QLabel(self.groupBox_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_14, 1, 1, 1, 1)

        self.label_16 = QLabel(self.groupBox_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_15.addWidget(self.label_16, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_2, 2, 0, 1, 1)


        self.gridLayout_16.addLayout(self.gridLayout_15, 0, 0, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_3, 1, 0, 1, 1)

        self.invoicecreatetable = QTableWidget(self.frame)
        if (self.invoicecreatetable.columnCount() < 7):
            self.invoicecreatetable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.invoicecreatetable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.invoicecreatetable.setObjectName(u"invoicecreatetable")
        self.invoicecreatetable.setGridStyle(Qt.PenStyle.DashLine)
        self.invoicecreatetable.setSortingEnabled(False)
        self.invoicecreatetable.horizontalHeader().setVisible(True)
        self.invoicecreatetable.horizontalHeader().setCascadingSectionResizes(False)
        self.invoicecreatetable.horizontalHeader().setHighlightSections(False)
        self.invoicecreatetable.horizontalHeader().setProperty("showSortIndicator", False)
        self.invoicecreatetable.horizontalHeader().setStretchLastSection(True)
        self.invoicecreatetable.verticalHeader().setVisible(False)
        self.invoicecreatetable.verticalHeader().setCascadingSectionResizes(True)
        self.invoicecreatetable.verticalHeader().setHighlightSections(False)
        self.invoicecreatetable.verticalHeader().setProperty("showSortIndicator", False)
        self.invoicecreatetable.verticalHeader().setStretchLastSection(False)

        self.gridLayout_9.addWidget(self.invoicecreatetable, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.frame, 4, 0, 1, 1)

        self.invoiceinfo = QGroupBox(self.InvoiceCreator)
        self.invoiceinfo.setObjectName(u"invoiceinfo")
        self.invoiceinfo.setMinimumSize(QSize(0, 80))
        self.gridLayout_13 = QGridLayout(self.invoiceinfo)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.compnayname = QLineEdit(self.invoiceinfo)
        self.compnayname.setObjectName(u"compnayname")

        self.gridLayout_12.addWidget(self.compnayname, 1, 1, 1, 1)

        self.label_5 = QLabel(self.invoiceinfo)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_12.addWidget(self.label_5, 1, 0, 1, 1)

        self.invoiceno = QLineEdit(self.invoiceinfo)
        self.invoiceno.setObjectName(u"invoiceno")

        self.gridLayout_12.addWidget(self.invoiceno, 0, 1, 1, 1)

        self.companyaddress = QLineEdit(self.invoiceinfo)
        self.companyaddress.setObjectName(u"companyaddress")

        self.gridLayout_12.addWidget(self.companyaddress, 2, 1, 1, 1)

        self.label_4 = QLabel(self.invoiceinfo)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_12.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_7 = QLabel(self.invoiceinfo)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_12.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_11 = QLabel(self.invoiceinfo)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_12.addWidget(self.label_11, 1, 4, 1, 1)

        self.label_9 = QLabel(self.invoiceinfo)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_12.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_8 = QLabel(self.invoiceinfo)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_12.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_10 = QLabel(self.invoiceinfo)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_12.addWidget(self.label_10, 0, 4, 1, 1)

        self.customername = QLineEdit(self.invoiceinfo)
        self.customername.setObjectName(u"customername")

        self.gridLayout_12.addWidget(self.customername, 0, 3, 1, 1)

        self.label_6 = QLabel(self.invoiceinfo)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_12.addWidget(self.label_6, 2, 0, 1, 1)

        self.label_12 = QLabel(self.invoiceinfo)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_12.addWidget(self.label_12, 2, 4, 1, 1)

        self.invoicedate = QDateEdit(self.invoiceinfo)
        self.invoicedate.setObjectName(u"invoicedate")
        self.invoicedate.setMinimumDate(QDate(1800, 9, 14))
        self.invoicedate.setCalendarPopup(True)

        self.gridLayout_12.addWidget(self.invoicedate, 0, 5, 1, 1)

        self.customeraddress = QLineEdit(self.invoiceinfo)
        self.customeraddress.setObjectName(u"customeraddress")

        self.gridLayout_12.addWidget(self.customeraddress, 1, 3, 1, 1)

        self.PONUMBER = QLineEdit(self.invoiceinfo)
        self.PONUMBER.setObjectName(u"PONUMBER")

        self.gridLayout_12.addWidget(self.PONUMBER, 2, 3, 1, 1)

        self.adddesignfile = QPushButton(self.invoiceinfo)
        self.adddesignfile.setObjectName(u"adddesignfile")
        self.adddesignfile.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_12.addWidget(self.adddesignfile, 2, 5, 1, 1)

        self.duedate = QDateEdit(self.invoiceinfo)
        self.duedate.setObjectName(u"duedate")
        self.duedate.setCalendarPopup(True)

        self.gridLayout_12.addWidget(self.duedate, 1, 5, 1, 1)


        self.gridLayout_13.addLayout(self.gridLayout_12, 0, 0, 1, 1)

        self.pushButton_9 = QPushButton(self.invoiceinfo)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_13.addWidget(self.pushButton_9, 1, 0, 1, 1)


        self.gridLayout_6.addWidget(self.invoiceinfo, 0, 0, 1, 1)

        self.fileedit = QGroupBox(self.InvoiceCreator)
        self.fileedit.setObjectName(u"fileedit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.fileedit.sizePolicy().hasHeightForWidth())
        self.fileedit.setSizePolicy(sizePolicy3)
        self.fileedit.setMinimumSize(QSize(0, 50))
        self.gridLayout_11 = QGridLayout(self.fileedit)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_10 = QGridLayout()
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.undo = QPushButton(self.fileedit)
        self.undo.setObjectName(u"undo")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.undo.sizePolicy().hasHeightForWidth())
        self.undo.setSizePolicy(sizePolicy4)
        self.undo.setMinimumSize(QSize(60, 0))
        self.undo.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.undo, 0, 4, 1, 1)

        self.label_3 = QLabel(self.fileedit)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 500 9pt \"Rubik\";")

        self.gridLayout_10.addWidget(self.label_3, 0, 10, 1, 1)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer, 0, 8, 1, 1)

        self.saveinvoicebutton = QPushButton(self.fileedit)
        self.saveinvoicebutton.setObjectName(u"saveinvoicebutton")
        sizePolicy4.setHeightForWidth(self.saveinvoicebutton.sizePolicy().hasHeightForWidth())
        self.saveinvoicebutton.setSizePolicy(sizePolicy4)
        self.saveinvoicebutton.setMinimumSize(QSize(60, 0))
        self.saveinvoicebutton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.saveinvoicebutton, 0, 3, 1, 1)

        self.print = QPushButton(self.fileedit)
        self.print.setObjectName(u"print")
        sizePolicy4.setHeightForWidth(self.print.sizePolicy().hasHeightForWidth())
        self.print.setSizePolicy(sizePolicy4)
        self.print.setMinimumSize(QSize(60, 0))
        self.print.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.print, 0, 2, 1, 1)

        self.additem = QPushButton(self.fileedit)
        self.additem.setObjectName(u"additem")
        sizePolicy4.setHeightForWidth(self.additem.sizePolicy().hasHeightForWidth())
        self.additem.setSizePolicy(sizePolicy4)
        self.additem.setMinimumSize(QSize(60, 0))
        self.additem.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 18pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.additem, 0, 0, 1, 1)

        self.fontsizecombo = QComboBox(self.fileedit)
        self.fontsizecombo.setObjectName(u"fontsizecombo")

        self.gridLayout_10.addWidget(self.fontsizecombo, 0, 11, 1, 1)

        self.redo = QPushButton(self.fileedit)
        self.redo.setObjectName(u"redo")
        sizePolicy4.setHeightForWidth(self.redo.sizePolicy().hasHeightForWidth())
        self.redo.setSizePolicy(sizePolicy4)
        self.redo.setMinimumSize(QSize(60, 0))
        self.redo.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.redo, 0, 5, 1, 1)

        self.chngeprice = QPushButton(self.fileedit)
        self.chngeprice.setObjectName(u"chngeprice")
        sizePolicy4.setHeightForWidth(self.chngeprice.sizePolicy().hasHeightForWidth())
        self.chngeprice.setSizePolicy(sizePolicy4)
        self.chngeprice.setMinimumSize(QSize(120, 0))
        self.chngeprice.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.chngeprice, 0, 6, 1, 1)

        self.minesitem = QPushButton(self.fileedit)
        self.minesitem.setObjectName(u"minesitem")
        sizePolicy4.setHeightForWidth(self.minesitem.sizePolicy().hasHeightForWidth())
        self.minesitem.setSizePolicy(sizePolicy4)
        self.minesitem.setMinimumSize(QSize(60, 0))
        self.minesitem.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.minesitem, 0, 1, 1, 1)

        self.fontedit = QFontComboBox(self.fileedit)
        self.fontedit.setObjectName(u"fontedit")

        self.gridLayout_10.addWidget(self.fontedit, 0, 9, 1, 1)

        self.modifytableheaderbutton = QPushButton(self.fileedit)
        self.modifytableheaderbutton.setObjectName(u"modifytableheaderbutton")
        sizePolicy2.setHeightForWidth(self.modifytableheaderbutton.sizePolicy().hasHeightForWidth())
        self.modifytableheaderbutton.setSizePolicy(sizePolicy2)
        self.modifytableheaderbutton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_10.addWidget(self.modifytableheaderbutton, 0, 7, 1, 1)


        self.gridLayout_11.addLayout(self.gridLayout_10, 0, 0, 1, 1)


        self.gridLayout_6.addWidget(self.fileedit, 1, 0, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_6, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.InvoiceCreator)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_18 = QGridLayout(self.page_4)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_17 = QGridLayout()
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.groupBox_4 = QGroupBox(self.page_4)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy5)
        self.groupBox_4.setMinimumSize(QSize(0, 80))
        self.gridLayout_20 = QGridLayout(self.groupBox_4)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.gridLayout_19 = QGridLayout()
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.deleteiteminvoicestockbutton = QPushButton(self.groupBox_4)
        self.deleteiteminvoicestockbutton.setObjectName(u"deleteiteminvoicestockbutton")
        sizePolicy4.setHeightForWidth(self.deleteiteminvoicestockbutton.sizePolicy().hasHeightForWidth())
        self.deleteiteminvoicestockbutton.setSizePolicy(sizePolicy4)
        self.deleteiteminvoicestockbutton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.deleteiteminvoicestockbutton, 0, 1, 1, 1)

        self.importstock = QPushButton(self.groupBox_4)
        self.importstock.setObjectName(u"importstock")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.importstock.sizePolicy().hasHeightForWidth())
        self.importstock.setSizePolicy(sizePolicy6)
        self.importstock.setMinimumSize(QSize(300, 0))
        self.importstock.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.importstock, 0, 2, 1, 1)

        self.createinvoicefrominvoicefile = QPushButton(self.groupBox_4)
        self.createinvoicefrominvoicefile.setObjectName(u"createinvoicefrominvoicefile")
        sizePolicy6.setHeightForWidth(self.createinvoicefrominvoicefile.sizePolicy().hasHeightForWidth())
        self.createinvoicefrominvoicefile.setSizePolicy(sizePolicy6)
        self.createinvoicefrominvoicefile.setMinimumSize(QSize(300, 0))
        self.createinvoicefrominvoicefile.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.createinvoicefrominvoicefile, 0, 4, 1, 1)

        self.addstockbutton = QPushButton(self.groupBox_4)
        self.addstockbutton.setObjectName(u"addstockbutton")
        sizePolicy4.setHeightForWidth(self.addstockbutton.sizePolicy().hasHeightForWidth())
        self.addstockbutton.setSizePolicy(sizePolicy4)
        self.addstockbutton.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.addstockbutton, 0, 0, 1, 1)

        self.editbuttonstockinvoice = QPushButton(self.groupBox_4)
        self.editbuttonstockinvoice.setObjectName(u"editbuttonstockinvoice")
        sizePolicy4.setHeightForWidth(self.editbuttonstockinvoice.sizePolicy().hasHeightForWidth())
        self.editbuttonstockinvoice.setSizePolicy(sizePolicy4)
        self.editbuttonstockinvoice.setStyleSheet(u"QPushButton{\n"
"	color:white;\n"
"	background-color: rgb(64, 64, 76);\n"
"	border:2px solid rgb(145, 145, 170);\n"
"	font: 13pt \"Rubik\";\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton::hover{\n"
"	\n"
"	background-color: rgb(83, 83, 99);\n"
"\n"
"}\n"
"QPushButton::focus{\n"
"	border:3px solid rgb(188, 188, 222);\n"
"}\n"
"\n"
"")

        self.gridLayout_19.addWidget(self.editbuttonstockinvoice, 0, 3, 1, 1)


        self.gridLayout_20.addLayout(self.gridLayout_19, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.groupBox_4, 0, 0, 1, 1)


        self.gridLayout_18.addLayout(self.gridLayout_17, 0, 0, 1, 1)

        self.stocktable = QTableWidget(self.page_4)
        self.stocktable.setObjectName(u"stocktable")

        self.gridLayout_18.addWidget(self.stocktable, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_4)

        self.gridLayout_2.addWidget(self.stackedWidget, 0, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1208, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuPreference = QMenu(self.menubar)
        self.menuPreference.setObjectName(u"menuPreference")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuPreference.menuAction())
        self.menuFile.addAction(self.actionCreate_new_invoice)
        self.menuFile.addAction(self.actionOpen_Invoices)
        self.menuFile.addAction(self.actionimport_stock_file_SSW_Type)
        self.menuFile.addAction(self.actionimport_stock_file_Ai_Check)
        self.menuView.addAction(self.actionBuy_Invoices)
        self.menuView.addAction(self.actionSell_Invoices)
        self.menuView.addAction(self.actionStock_Items)
        self.menuView.addAction(self.actionGraph_Creator)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionCreate_new_invoice.setText(QCoreApplication.translate("MainWindow", u"Create new invoice", None))
        self.actionOpen_Invoices.setText(QCoreApplication.translate("MainWindow", u"Open Invoices", None))
        self.actionimport_stock_file_SSW_Type.setText(QCoreApplication.translate("MainWindow", u"import stock file (SSW Type)", None))
        self.actionimport_stock_file_Ai_Check.setText(QCoreApplication.translate("MainWindow", u"import stock file (Ai Check)", None))
        self.actionBuy_Invoices.setText(QCoreApplication.translate("MainWindow", u"Buy Invoices", None))
        self.actionSell_Invoices.setText(QCoreApplication.translate("MainWindow", u"Sell Invoices", None))
        self.actionStock_Items.setText(QCoreApplication.translate("MainWindow", u"Stock Items", None))
        self.actionGraph_Creator.setText(QCoreApplication.translate("MainWindow", u"Graph Creator", None))
        self.logoname.setText(QCoreApplication.translate("MainWindow", u"Saad Studio\n"
"WorkStation", None))
        self.stockshow.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        self.NewInvoice.setText(QCoreApplication.translate("MainWindow", u"Create New Invoice", None))
        self.invoicesshow.setText(QCoreApplication.translate("MainWindow", u"Invoices", None))
        self.appinformation.setText(QCoreApplication.translate("MainWindow", u"App Version 1.0 / Youtube : Saad Studios / Found a bugs? contact: saadstudios2008@gmail.com  / Donate: paypal.me/saadstudio", None))
        self.freeeditcheckbox.setText(QCoreApplication.translate("MainWindow", u"Enable Free Editing", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"TVA/VAT", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Total HT", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Discount/Remise", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Total TTC", None))
        ___qtablewidgetitem = self.invoicecreatetable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Reference", None));
        ___qtablewidgetitem1 = self.invoicecreatetable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem2 = self.invoicecreatetable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Qty.", None));
        ___qtablewidgetitem3 = self.invoicecreatetable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Unit Price", None));
        ___qtablewidgetitem4 = self.invoicecreatetable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Discount", None));
        ___qtablewidgetitem5 = self.invoicecreatetable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Total Ht.", None));
        ___qtablewidgetitem6 = self.invoicecreatetable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Total TTC", None));
        self.invoiceinfo.setTitle(QCoreApplication.translate("MainWindow", u"INVOICE INFO", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Company", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Invoice No.", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Customer name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Invoice Due Date", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"PO Number (OPT)", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Customer Address", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Invoice Date", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Company address", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Invoice design file ", None))
        self.adddesignfile.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"Save Invoice Data", None))
        self.fileedit.setTitle(QCoreApplication.translate("MainWindow", u"File Edits", None))
        self.undo.setText(QCoreApplication.translate("MainWindow", u"< Undo", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Font Size", None))
        self.saveinvoicebutton.setText(QCoreApplication.translate("MainWindow", u"Save File", None))
        self.print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.additem.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.redo.setText(QCoreApplication.translate("MainWindow", u"Redo >", None))
        self.chngeprice.setText(QCoreApplication.translate("MainWindow", u"Change Price", None))
        self.minesitem.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.modifytableheaderbutton.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.deleteiteminvoicestockbutton.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.importstock.setText(QCoreApplication.translate("MainWindow", u"Import Stock (csv, xlsx, ...) File", None))
        self.createinvoicefrominvoicefile.setText(QCoreApplication.translate("MainWindow", u"Create Invoice from a file", None))
        self.addstockbutton.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.editbuttonstockinvoice.setText(QCoreApplication.translate("MainWindow", u"Edit Data", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPreference.setTitle(QCoreApplication.translate("MainWindow", u"Preference", None))
    # retranslateUi

