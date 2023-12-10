# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip-check.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(569, 408)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_time_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_time_val.setGeometry(QtCore.QRect(30, 20, 121, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.lbl_time_val.setFont(font)
        self.lbl_time_val.setObjectName("lbl_time_val")
        self.lbl_date_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_date_val.setGeometry(QtCore.QRect(30, 50, 130, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_date_val.setFont(font)
        self.lbl_date_val.setObjectName("lbl_date_val")
        self.lbl_lastipcheck = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lastipcheck.setGeometry(QtCore.QRect(30, 320, 130, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastipcheck.setFont(font)
        self.lbl_lastipcheck.setObjectName("lbl_lastipcheck")
        self.lbl_last_ipcheck_time_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_last_ipcheck_time_val.setGeometry(QtCore.QRect(110, 330, 91, 16))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_last_ipcheck_time_val.setFont(font)
        self.lbl_last_ipcheck_time_val.setObjectName("lbl_last_ipcheck_time_val")
        self.lbl_lastip_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lastip_val.setGeometry(QtCore.QRect(220, 220, 131, 39))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_lastip_val.setFont(font)
        self.lbl_lastip_val.setObjectName("lbl_lastip_val")
        self.lbl_nextipcheck = QtWidgets.QLabel(self.centralwidget)
        self.lbl_nextipcheck.setGeometry(QtCore.QRect(30, 350, 131, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_nextipcheck.setFont(font)
        self.lbl_nextipcheck.setObjectName("lbl_nextipcheck")
        self.lbl_next_ipcheck_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_next_ipcheck_val.setGeometry(QtCore.QRect(110, 350, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_next_ipcheck_val.setFont(font)
        self.lbl_next_ipcheck_val.setObjectName("lbl_next_ipcheck_val")
        self.lbl_lastipsince = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lastipsince.setGeometry(QtCore.QRect(370, 230, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastipsince.setFont(font)
        self.lbl_lastipsince.setObjectName("lbl_lastipsince")
        self.lbl_lastip_since_time_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lastip_since_time_val.setGeometry(QtCore.QRect(410, 230, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(8)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setKerning(False)
        self.lbl_lastip_since_time_val.setFont(font)
        self.lbl_lastip_since_time_val.setObjectName("lbl_lastip_since_time_val")
        self.lbl_lastip_since_date_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_lastip_since_date_val.setGeometry(QtCore.QRect(470, 230, 71, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_lastip_since_date_val.setFont(font)
        self.lbl_lastip_since_date_val.setObjectName("lbl_lastip_since_date_val")
        self.lbl_upsince = QtWidgets.QLabel(self.centralwidget)
        self.lbl_upsince.setGeometry(QtCore.QRect(420, 10, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_upsince.setFont(font)
        self.lbl_upsince.setObjectName("lbl_upsince")
        self.lbl_upsince_time_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_upsince_time_val.setGeometry(QtCore.QRect(420, 20, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setKerning(False)
        self.lbl_upsince_time_val.setFont(font)
        self.lbl_upsince_time_val.setObjectName("lbl_upsince_time_val")
        self.lbl_upsince_date_val = QtWidgets.QLabel(self.centralwidget)
        self.lbl_upsince_date_val.setGeometry(QtCore.QRect(420, 50, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        self.lbl_upsince_date_val.setFont(font)
        self.lbl_upsince_date_val.setObjectName("lbl_upsince_date_val")
        self.btn_set_interval = QtWidgets.QPushButton(self.centralwidget)
        self.btn_set_interval.setGeometry(QtCore.QRect(470, 340, 41, 23))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.btn_set_interval.setFont(font)
        self.btn_set_interval.setCheckable(False)
        self.btn_set_interval.setObjectName("btn_set_interval")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(370, 350, 61, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(80, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lineEdit.setFont(font)
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.lineEdit.setObjectName("lineEdit")
        self.lbl_s = QtWidgets.QLabel(self.centralwidget)
        self.lbl_s.setGeometry(QtCore.QRect(440, 350, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_s.setFont(font)
        self.lbl_s.setObjectName("lbl_s")
        self.lbl_ipcheckevery = QtWidgets.QLabel(self.centralwidget)
        self.lbl_ipcheckevery.setGeometry(QtCore.QRect(370, 320, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.lbl_ipcheckevery.setFont(font)
        self.lbl_ipcheckevery.setObjectName("lbl_ipcheckevery")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 100, 151, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../Pictures/check.PNG"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lbl_current_ip = QtWidgets.QLabel(self.centralwidget)
        self.lbl_current_ip.setGeometry(QtCore.QRect(230, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.lbl_current_ip.setFont(font)
        self.lbl_current_ip.setObjectName("lbl_current_ip")
        self.btn_domains = QtWidgets.QPushButton(self.centralwidget)
        self.btn_domains.setGeometry(QtCore.QRect(440, 290, 75, 23))
        self.btn_domains.setObjectName("btn_domains")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 569, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionMy_Help = QtWidgets.QAction(MainWindow)
        self.actionMy_Help.setObjectName("actionMy_Help")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_as = QtWidgets.QAction(MainWindow)
        self.actionSave_as.setObjectName("actionSave_as")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionMy_Help)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.lbl_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.lbl_lastipcheck.setText(_translate("MainWindow", "Last ip-check:"))
        self.lbl_last_ipcheck_time_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastip_val.setText(_translate("MainWindow", "88.223.66.89"))
        self.lbl_nextipcheck.setText(_translate("MainWindow", "Next ip-check"))
        self.lbl_next_ipcheck_val.setText(_translate("MainWindow", "TextLabel"))
        self.lbl_lastipsince.setText(_translate("MainWindow", "Since:"))
        self.lbl_lastip_since_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.lbl_lastip_since_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.lbl_upsince.setText(_translate("MainWindow", "Up since:"))
        self.lbl_upsince_time_val.setText(_translate("MainWindow", "00:00:00"))
        self.lbl_upsince_date_val.setText(_translate("MainWindow", "12.12.1923"))
        self.btn_set_interval.setText(_translate("MainWindow", "Set"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>test</p></body></html>"))
        self.lbl_s.setText(_translate("MainWindow", "s."))
        self.lbl_ipcheckevery.setText(_translate("MainWindow", "IP-check every:"))
        self.lbl_current_ip.setText(_translate("MainWindow", "Current IP"))
        self.btn_domains.setText(_translate("MainWindow", "Domains"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionMy_Help.setText(_translate("MainWindow", "My Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_as.setText(_translate("MainWindow", "Save as..."))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
